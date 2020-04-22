import os
import sys


filename = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(1, filename)
from zoomapi import OAuthZoomClient

import json
from configparser import ConfigParser
from pyngrok import ngrok

parser = ConfigParser()
parser.read("bots/bot.ini")
client_id = parser.get("OAuth", "client_id")
client_secret = parser.get("OAuth", "client_secret")
port = parser.getint("OAuth", "port", fallback=4001)
browser_path = parser.get("OAuth", "browser_path")
print(f'id: {client_id} browser: {browser_path}')
#builds tunnel
redirect_url = ngrok.connect(port, "http")
print("Redirect URL is", redirect_url)
#establishes our client taking info from the ini file
client = OAuthZoomClient(client_id, client_secret, port, redirect_url, browser_path)

user_response = client.user.get(id='me')
user = json.loads(user_response.content)
print(user)
print ('---')


#get channel to join
# print(json.loads(client.meeting.list(user_id="me").content))
# client.chat_channels.list()
# channels = json.loads(client.chat_channels.list().content)["channels"]

#LIST CHANNELS
#print("HERE ARE ALL MY CHANNELS: ")
#for c in channels:
#    print(c)
#    if "test" in c.values():
#        print("Found channel test", c["id"])
#        cid = to_channel=c["id"]
#stop = False

#CREATE A CHANNEL

# stop = False
# while not stop:
#     ch_type = input("Type 1 for multi-zoom-account private channel\n"+
#                 "Type 2 for single-zoom-account private channel\n"+
#                 "Type 3 for public channel\n"+
#                 "Type 4 for new chat\n")
#     if int (ch_type) not in [1,2,3,4]:
#         print("Invalid entry, retry")
#     else:
#         stop = True
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
# print("Creating a channel")
# ch_name = "get_channel_test"
# ch_type = 1
# email = json.loads(client.user.get(id="me").content)["email"]
# members = []
# while len(ch_other_members) <= 5:
#     new_member = input("Enter email of additional members (up to 5) or 'done' to continue: ")
#     if new_member == "done":
#         break
#     else:
#         ch_other_members.append(new_member)
#         print(new_member + " added. ")
# print(client.chat_channels.create(name=ch_name, type=ch_type, members=members).content)
#
# channels = json.loads(client.chat_channels.list().content)["channels"]
#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
# while True:
#
#     #LEAVING
#     channels = json.loads(client.chat_channels.list().content)["channels"]
#     print("HERE ARE ALL MY CHANNELS BEFORE LEAVING: ")
#     for c in channels:
#         print(c)
#         if "test_join" in c.values():
#             print("MEMBERS: \n")
#             print(client.chat_channels.list_members(channel_id=c["id"]).content)
#
#     to_leave = input("Enter id of channel you wish to leave: ")
#     client.chat_channels.leave(channel_id=to_leave)
#
#     channels = json.loads(client.chat_channels.list().content)["channels"]
#     print("HERE ARE ALL MY CHANNELS AFTER LEAVING: ")
#     for c in channels:
#         print(c)
#         if "test_join" in c.values():
#             print("MEMBERS: \n")
#             print(client.chat_channels.list_members(channel_id=c["id"]).content)
#
#     #REJOINING
#     to_join = input("Enter id of channel you wish to join: ")
#     client.chat_channels.join(channel_id=to_join)
#
#     channels = json.loads(client.chat_channels.list().content)["channels"]
#     print("HERE ARE ALL MY CHANNELS: ")
#     for c in channels:
#         print(c)
#         if "test_join" in c.values():
#             print("MEMBERS: \n")
#             print(client.chat_channels.list_members(channel_id=c["id"]).content)
#
#     #REMOVING
#     to_remove_channel = input("Enter id of channel with member to remove: ")
#     to_remove_member = input("Enter id of member you wish to remove: ")
#     client.chat_channels.remove_member(channel_id=to_remove_channel, id=to_remove_member)
#
#     channels = json.loads(client.chat_channels.list().content)["channels"]
#     print("HERE ARE ALL MY CHANNELS AFTER REMOVING MEMBER ")
#     for c in channels:
#         if "test_join" in c.values():
#             print("MEMBERS: \n")
#             print(client.chat_channels.list_members(channel_id=c["id"]).content)
#
# stop = False

#GET CHANNEL
# select_channel = input("Enter channel_id of channel you want to get: ")
# print(client.chat_channels.get_channel(channel_id=select_channel).content)

#UPDATE CHANNEL
# update_channel_name = input("Enter new name for this channel: ")
# client.chat_channels.update(name=update_channel_name, channel_id=select_channel)
# print(client.chat_channels.get_channel(channel_id=select_channel).content)

#DELETE CHANNEL

# select_channel_toDelete = input("Enter channel_id of channel you want to delete: ")
# client.chat_channels.delete(channel_id=select_channel_toDelete)

#LIST MEMBERS OF CHANNEL
# select_channel_toListMembers = input("Enter channel_id of channel you want to see members of: ")
# print(client.chat_channels.list_members(channel_id=select_channel_toListMembers).content)

#INVITE CHANNEL MEMBERS
#must be in contact list*
# friend_to_invite = input("Enter email of friend you want to invite to channel")
# channel_to_invite = input("Enter channel_id you want to invite friend to")
# members.append({"email": friend_to_invite})
# client.chat_channels.invite(channel_id=channel_to_invite, members=members)

#POSTING A MESSAGE
#while not stop:
#    message = input("Enter message: ")
#    print(client.chat_messages.post(to_channel=cid, message=message))
#    if message == "stop":
#        stop = True


#LIST USER CHAT MESSAGES
#get the list of messages in our current channel
#messages = client.chat_messages.list(user_id="me", to_channel=cid)
#messages = json.loads(client.chat_messages.list(user_id="me", to_channel=cid).content)["messages"]
#for m in messages:
#    print(m)

#UPDATING A MESSAGE
#new_message_id = input("Enter message_id you would like to update: ")
#new_message = input("Enter updated message: ")
#client.chat_messages.update(message_id=new_message_id, message=new_message, to_channel=cid)

#DELETING A MESSAGE
#while not stop:
#    delete_message_id = input("Enter message_id you would like to delete: ")
#    client.chat_messages.delete(to_channel=cid, message_id=delete_message_id)
#    if delete_message_id == "stop":
#        stop = True