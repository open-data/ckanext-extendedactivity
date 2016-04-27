#!/usr/bin/env python
# encoding: utf-8
__all__ = ('IActivity', 'ActivityPlugin')

import ckan.plugins as p
import ckan.lib.activity_streams as act
from ckan.plugins.interfaces import Interface


class IActivity(Interface):
    def string_icons(self, string_icons):
        raise NotImplementedError

    def snippet_functions(self, snippet_functions):
        raise NotImplementedError

    def string_functions(self, string_functions):
        raise NotImplementedError


class ActivityPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IActions)

    def get_actions(self):
        return {}

    def update_config(self, config):
        for plugin in p.PluginImplementations(IActivity):
            try:
                plugin.string_icons(act.activity_stream_string_icons)
            except NotImplementedError:
                pass

            try:
                plugin.snippet_functions(act.activity_snippet_functions)
            except NotImplementedError:
                pass

            try:
                plugin.string_functions(act.activity_stream_string_functions)
            except NotImplementedError:
                pass