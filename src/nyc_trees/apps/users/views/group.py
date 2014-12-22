# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from apps.core.models import Group

from apps.users.forms import GroupSettingsForm
from apps.event.models import Event
from apps.event.event_list import EventList


def group_list_page(request):
    # TODO: implement
    pass


def group_detail(request, group_slug):
    group = get_object_or_404(Group, slug=group_slug)
    events = Event.objects.filter(group_id=group.pk, is_private=False)

    return {
        'group': group,
        'event_list': EventList.simple_context(request, events),
        # TODO: check if user is group admin or census admin
        'user_can_edit_group': True,
        'edit_url': reverse('group_edit', kwargs={'group_slug': group.slug})
    }


def edit_group(request, group_slug):
    group = get_object_or_404(Group, slug=group_slug)
    form = GroupSettingsForm(instance=group, label_suffix='')
    context = {
        'form': form,
        'group_slug': group_slug
    }
    return context


def update_group_settings(request, group_slug):
    group = get_object_or_404(Group, slug=group_slug)
    form = GroupSettingsForm(request.POST, instance=group)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(
            reverse('group_detail', kwargs={'group_slug': group_slug}))
    else:
        context = {
            'form': form,
            'group_slug': group_slug
        }
        return context


def follow_group(request, group_slug):
    # TODO: implement
    pass


def unfollow_group(request, group_slug):
    # TODO: implement
    pass


def start_group_map_print_job(request, group_slug):
    # TODO: implement
    pass


def give_user_mapping_priveleges(request, group_slug, username):
    # TODO: implement
    pass


def remove_user_mapping_priveleges(request, group_slug, username):
    # TODO: implement
    pass