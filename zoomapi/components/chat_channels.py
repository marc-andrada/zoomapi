<<<<<<< HEAD
"""Zoom.us REST API Python Client -- Chat Messages component"""

from zoomapi import util
from zoomapi.components import base

class ChatChannelsComponentV2(base.BaseComponent):
    """Component dealing with all chat channels related matters"""

    def list(self, **kwargs):
        return self.get_request("/chat/users/me/channels")

    def create(self, **kwargs):
        util.require_keys(kwargs, "name")
        util.require_keys(kwargs, "type")
        util.require_keys(kwargs, "members")
        return self.post_request("/chat/users/me/channels", data=kwargs)

    def get_channel(self, **kwargs):
        util.require_keys(kwargs, "channel_id")
        return self.get_request("/chat/channels/{}".format(kwargs.get("channel_id")), params=kwargs)

    def update(self, **kwargs):
        util.require_keys(kwargs, "channel_id")
        util.require_keys(kwargs, "name")
        return self.patch_request("/chat/channels/{}".format(kwargs.get("channel_id")), data=kwargs)

    def delete(self, **kwargs):
        util.require_keys(kwargs, "channel_id")
        return self.delete_request("/chat/channels/{}".format(kwargs.get("channel_id")), params=kwargs)

    def list_members(self, **kwargs):
        util.require_keys(kwargs, "channel_id")
        return self.get_request("/chat/channels/{}/members".format(kwargs.get("channel_id")), params=kwargs)

    def invite(self, **kwargs):
        util.require_keys(kwargs, "channel_id")
        util.require_keys(kwargs, "members")
        return self.post_request("/chat/channels/{}/members".format(kwargs.get("channel_id")), data=kwargs)

    def join(self, **kwargs):
        util.require_keys(kwargs, "channel_id")
        return self.post_request("/chat/channels/{}/members/me".format(kwargs.get("channel_id")), params=kwargs)

    def leave(self, **kwargs):
        util.require_keys(kwargs, "channel_id")
        return self.delete_request("/chat/channels/{}/members/me".format(kwargs.get("channel_id")), params=kwargs)

    def remove_member(self, **kwargs):
        util.require_keys(kwargs, "channel_id")
        util.require_keys(kwargs, "id")
        return self.delete_request("/chat/channels/{}/members/{}".format(kwargs.get("channel_id"), kwargs.get("id")),
                                   params=kwargs)


=======
"""Zoom.us REST API Python Client -- Chat Messages component"""

from zoomapi.util import Throttled
from zoomapi.components import base

class ChatChannelsComponentV2(base.BaseComponent):
    """Component dealing with all chat channels related matters"""

    @Throttled
    def list(self, **kwargs):
        return self.get_request("/chat/users/me/channels")

>>>>>>> 0ceec23a119c775f79313b89479fd2041085ab4a
