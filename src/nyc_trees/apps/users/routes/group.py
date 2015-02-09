# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from django.contrib.auth.decorators import login_required

from django_tinsel.decorators import route, render_template, string_to_response
from django_tinsel.utils import decorate as do

from apps.core.decorators import group_request, group_admin_do

from apps.users.views import group as v


render_follow_button = render_template('groups/partials/follow_button.html')


group_list_page = route(GET=do(render_template('groups/list.html'),
                               v.group_list_page))

group_detail = route(GET=do(group_request,
                            render_template('groups/detail.html'),
                            v.group_detail))

group_territory_geojson = route(GET=do(group_request,
                                       string_to_response("application/json"),
                                       v.group_territory_geojson))

group_edit = group_admin_do(render_template('groups/settings.html'),
                            route(GET=v.edit_group,
                                  POST=v.update_group_settings))

follow_group = do(
    login_required,
    group_request,
    route(GET=v.redirect_to_group_detail,
          POST=do(render_follow_button, v.follow_group)))

unfollow_group = do(
    login_required,
    group_request,
    route(GET=v.redirect_to_group_detail,
          POST=do(render_follow_button, v.unfollow_group)))

# TODO: should this have group_admin
start_group_map_print_job = route(POST=v.start_group_map_print_job)

edit_user_mapping_priveleges = group_admin_do(
    render_template('groups/partials/grant_access_button.html'),
    route(PUT=v.give_user_mapping_priveleges,
          DELETE=v.remove_user_mapping_priveleges))
