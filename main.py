#   /$$                           /$$       /$$                           /$$ /$$                             /$$     /$$      
#  | $$                          | $$      | $$                          | $$| $$                            | $$    | $$      
#  | $$$$$$$   /$$$$$$  /$$$$$$$ | $$   /$$| $$   /$$  /$$$$$$   /$$$$$$ | $$| $$                  /$$$$$$  /$$$$$$  | $$$$$$$ 
#  | $$__  $$ |____  $$| $$__  $$| $$  /$$/| $$  /$$/ /$$__  $$ /$$__  $$| $$| $$                 /$$__  $$|_  $$_/  | $$__  $$
#  | $$  \ $$  /$$$$$$$| $$  \ $$| $$$$$$/ | $$$$$$/ | $$  \__/| $$  \ $$| $$| $$                | $$$$$$$$  | $$    | $$  \ $$
#  | $$  | $$ /$$__  $$| $$  | $$| $$_  $$ | $$_  $$ | $$      | $$  | $$| $$| $$                | $$_____/  | $$ /$$| $$  | $$
#  | $$$$$$$/|  $$$$$$$| $$  | $$| $$ \  $$| $$ \  $$| $$      |  $$$$$$/| $$| $$       /$$      |  $$$$$$$  |  $$$$/| $$  | $$
#  |_______/  \_______/|__/  |__/|__/  \__/|__/  \__/|__/       \______/ |__/|__/      |__/       \_______/   \___/  |__/  |__/






import os
import random
import discord



bot_token = os.environ['bot_token']
client = discord.Client()



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')



        

@client.event
async def on_message(message:discord.Message):
   
        if message.content == "greg":
            "do nothing"
        else:
            await message.delete()


if __name__ == '__main__':
    client.run(bot_token)
