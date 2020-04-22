Hello there!

I have written instructions for my botm1.py to go through all library functions required
for milestone 1.

Here are some setup steps to get it working (hopefully) properly:

1) Ensure that the bot.ini file includes your own client_id and client_secret obtained 
from zoom. The current id and secret are from my gmail test bot and the bot will not be able
to function unless you have login access to my account. So please test the bot with yours :]
1) Please move to the ../zoomapi directory in your terminal
2) Enter the command: python3 bots/botm1.py
3) If the program begins smoothly, follow the further instructions
provided by my bot. Most entries are 'y' to continue exhibiting another feature and entering
names for things like channels and messages.

Notes:
            
- We use sleeps in between API calls to ensure each is called properly
- For the join function, a 400 error message will return stating that we could
not join the chananel. This is because only the bot was in that channel before leaving and
subsequently trying to rejoin. The function does work as intended though with the error being
expected.

Thank you, and enjoy :]