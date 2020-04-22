import os
import sys
import time

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

redirect_url = ngrok.connect(port, "http")
print("Redirect URL is", redirect_url)

client = OAuthZoomClient(client_id, client_secret, port, redirect_url, browser_path)

user_response = client.user.get(id='me')
print(client.user.get(id='me'))
user = json.loads(user_response.content)
print(user)
print ('---------------------------------------------------------------------------------')

#START
print('Hello! I am botm1. Today we will be exploring some of my features ;]')
time.sleep(2)
print("Loading our test channels...")
client.chat_channels.create(name="test_leave_join", type=1, members=[])
time.sleep(2)
client.chat_channels.create(name="test_invite_remove", type=1, members=[])
time.sleep(2)
client.chat_channels.create(name="test_chat_messages", type=1, members=[])
time.sleep(2)

#LIST CHANNELS
continue_program = input("\nOkay Zoomer, first we will show you a list of my current channels. Enter 'y' to continue: ")
while continue_program != 'y':
    continue_program = input("Enter 'y' to continue: ")
print("\nHere are all of the channels I have currently: ")
channels = json.loads(client.chat_channels.list().content)["channels"]
for c in channels:
   print(c)
time.sleep(2)

#CREATE CHANNEL
print("\nNow, let's create a new channel! We'll make it private so our secrets are safe :^]")
new_channel = input("Enter the name of our new channel: ")
ch_type = 1
members = []
client.chat_channels.create(name=new_channel, type=ch_type, members=members)
print("\nHere are all of the channels I have now:")
channels = json.loads(client.chat_channels.list().content)["channels"]
for c in channels:
    print(c)
    if new_channel in c.values():
        cid_new_channel = to_channel=c["id"]
print("\nNotice yours has been added!")
time.sleep(2)

#GET CHANNEL
print("\nLet's GET the channel we just created and display its info.")
print("\nHere is your channel:")
print(client.chat_channels.get_channel(channel_id=cid_new_channel).content)
time.sleep(2)

#UPDATE CHANNEL
print("\nLet's update the name of this channel.")
new_channel_name = input("Enter a new name: ")
client.chat_channels.update(name=new_channel_name, channel_id=cid_new_channel)
time.sleep(2)
print("\nHere is your channel now:")
print(client.chat_channels.get_channel(channel_id=cid_new_channel).content)
time.sleep(2)

#DELETE CHANNEL
print("\nTime to say goodbye to our channel :c")
continue_program2 = input("Enter 'y' to delete: ")
while continue_program2 != 'y':
    continue_program2 = input("Enter 'y' to delete: ")
client.chat_channels.delete(channel_id=cid_new_channel)
print("\n3, 2, 1... POOF! The channel has been removed.")
print("\nHere are all of the channels I have now:")
channels = json.loads(client.chat_channels.list().content)["channels"]
for c in channels:
    print(c)
print("\nNotice yours has been deleted!")
time.sleep(2)

#LEAVE/JOIN CHANNEL
print("\nNow we're going to leave and rejoin one of my channels: test_leave_join")
continue_program3 = input("Enter 'y' to continue: ")
while continue_program3 != 'y':
    continue_program3 = input("Enter 'y' to continue: ")
time.sleep(2)
print("\nHere are all of the channels I have before leaving:")
channels = json.loads(client.chat_channels.list().content)["channels"]
for c in channels:
    print(c)
    if "test_leave_join" in c.values():
        cid_leave_join = to_channel=c["id"]
time.sleep(2)
print("\nNow we'll leave...")
client.chat_channels.leave(channel_id=cid_leave_join)
print("\nHere are all of the channels I have after leaving:")
channels = json.loads(client.chat_channels.list().content)["channels"]
for c in channels:
    print(c)
time.sleep(2)
print("\nNow we'll attempt to rejoin the channel...")
#Following message will return unable to join because there was only 1 member in channel before bot left
print(client.chat_channels.join(channel_id=cid_leave_join).content)
print("\nHere are all of the channels I have after attmpting to re-join:")
#Create channel for us to test invite remove
time.sleep(2)
channels = json.loads(client.chat_channels.list().content)["channels"]
for c in channels:
    print(c)
    if "test_invite_remove" in c.values():
        cid_invite_remove = to_channel=c["id"]
time.sleep(2)

#LIST/INVITE/REMOVE MEMBER
print("\nNext we're going to invite then remove a member in the channel: test_invite_remove")
continue_program4 = input("Enter 'y' to continue: ")
while continue_program4 != 'y':
    continue_program4 = input("Enter 'y' to continue: ")
for c in channels:
    print(c)
    if "test_invite_remove" in c.values():
        cid_invite_remove = to_channel=c["id"]
time.sleep(2)
print("\nFirst, we'll list the current members in the channel: test_invite_remove:")
print(client.chat_channels.list_members(channel_id=cid_invite_remove).content)
print("\nNow inviting member with email: andradam@uci.edu...")
members.append({"email": "andradam@uci.edu"})
client.chat_channels.invite(channel_id=cid_invite_remove, members=members)
print("\nHere is a list of members after the invite:")
print(client.chat_channels.list_members(channel_id=cid_invite_remove).content)
time.sleep(2)
print("\nNow we will remove this member")
current_members = json.loads(client.chat_channels.list_members(channel_id=cid_invite_remove).content)["members"]
for m in current_members:
    if "andradam@uci.edu" in m.values():
        member_id = m["id"]
client.chat_channels.remove_member(channel_id=cid_invite_remove, id=member_id)
time.sleep(2)
print("\nHere is a list of members after the removing the member:")
print(client.chat_channels.list_members(channel_id=cid_invite_remove).content)
time.sleep(2)

#LIST CHAT MESSAGES
print("\nNow let's list the chat messages in the channel: test_chat_messages")
continue_program5 = input("Enter 'y' to continue: ")
while continue_program5 != 'y':
    continue_program5 = input("Enter 'y' to continue: ")
time.sleep(2)
channels = json.loads(client.chat_channels.list().content)["channels"]
for c in channels:
    if "test_chat_messages" in c.values():
        cid_chat_messages = to_channel=c["id"]
time.sleep(2)
client.chat_messages.post(to_channel=cid_chat_messages, message="test message")
time.sleep(2)
messages = json.loads(client.chat_messages.list(user_id="me", to_channel=cid_chat_messages).content)["messages"]
for m in messages:
   print(m)
time.sleep(2)

#SEND MESSAGE
print("\nTime to send a message")
message_to_send = input("Enter a (unique) message: ")
client.chat_messages.post(to_channel=cid_chat_messages, message=message_to_send)
print('\nMessage has been sent')
time.sleep(2)
print("\nHere is the list of messages in the channel now: ")
messages = json.loads(client.chat_messages.list(user_id="me", to_channel=cid_chat_messages).content)["messages"]
time.sleep(2)
for m in messages:
    print(m)
    if message_to_send in m.values():
        message_id = m["id"]
        print(message_id)
time.sleep(2)

#UPDATE MESSAGE
print("\nNow we'll update a our unique message")
new_message = input("Enter in a new message to update our previous one: ")
client.chat_messages.update(message_id=message_id, message=new_message, to_channel=cid_chat_messages)
print('\nMessage has been updated')
time.sleep(2)
print("\nHere is the list of messages in the channel now: ")
messages = json.loads(client.chat_messages.list(user_id="me", to_channel=cid_chat_messages).content)["messages"]
for m in messages:
    print(m)
print("Notice our message has now been updated")
time.sleep(2)

#DELETE MESSAGE
print("\nFinally, let's delete your message. Don't worry your secret is safe with me :X")
continue_program6 = input("Enter 'y' to delete: ")
while continue_program6 != 'y':
    continue_program6 = input("Enter 'y' to delete: ")
client.chat_messages.delete(to_channel=cid_chat_messages, message_id=message_id)
print('\nMessage has been deleted')
time.sleep(2)
print("\nHere is the list of messages in the channel now: ")
messages = json.loads(client.chat_messages.list(user_id="me", to_channel=cid_chat_messages).content)["messages"]
for m in messages:
    print(m)
print("\nNotice your message has been deleted")

#END
time.sleep(2)
print("\nWell, it's been fun. Thanks for testing out these features with me!")
time.sleep(2)
print("Goodbye")

