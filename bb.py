# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    BB.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jbuny-fe <jbuny-fe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/30 11:31:29 by jbuny-fe          #+#    #+#              #
#    Updated: 2022/05/26 15:40:29 by jbuny-fe         ###   ########.fr        #
#    Updated: 2022/05/26 15:17:08 by jbuny-fe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import discord
from config import *
import datetime
import os
import sys
import time
import toml
import threading
import requests
import json
import traceback

# bot = commands.Bot(command_prefix="bacalhau", description="Bacalhau_demolhado")

intents = discord.Intents.all()
intents.members = True

client = discord.Client(intents=intents)
thanks = ["thank you", "thank u", "thanks", "thx", "obrigado", "obrigada", ]
bacalhau = ["bacalhau", "Bacalhau"]
sorry = ["Sorry", "sorry", "desculpa", "Desculpa", "I'm sorry", "im sorry", "Im sorry"]
gm = ["gm", "good morning", "Bom dia", "bom dia"]
hey = ["hey", "hello", "heyy", "Boas", "boas", "ola", "olá", "Ola", "Olá", "oi", "Oi", "hi", "Hi", "hey there", 
        "Hey there", "hey there!", "Hey there!", "hey there!!", "Hey there!!", "hey there!!!", "Hey there!!!", "hey there!!!!", 
        "Hey there!!!!", "hey there!!!!!", "Hey there!!!!!", "hey there!!!!!!", "Hey there!!!!!!", "hey there!!!!!!!", "Hey there!!!!!!!",
         "hey there!!!!!!!!", "Hey there!!!!!!!!", "hey there!!!!!!!!!", "Hey there!!!!!!!!!", "hey there!!!!!!!!!!", "Hey there!!!!!!!!!!", 
         "hey there!!!!!!!!!!!", "Hey there!!!!!!!!!!!", "hey there!!!!!!!!!!!!", "Hey there!!!!!!!!!!!!", "hey there!!!!!!!!!!!!!", "Hey there!!!!!!!!!!!!!",
          "hey there!!!!!!!!!!!!!!", "Hey there!!!!!!!!!!!!!!", "hey there!!!!!!!!!!!!!!!", "Hey there!!!!!!!!!!!!!!!", "hey there!!!!!!!!!!!!!!!!", "Hey there!!!!!!!!!!!!!!!!"]
links = ["I NEED THE LINKS", "bacalhau.links", "UNLIMITED POWER", "GIMME THE LINKS", "links?", "links", "LINKS", "links please", "links please?", "links please!"]
login = ["login?", "passe da conta", "qual é a pass", "qual é o login", "login", "password", "pass", "passe", "passe da conta?"]

def timer():  # starts once the program is started
    try:
        with open('time_keeper', 'r') as f:  # opens a time_keeper file if it already exists
            tk = toml.load(f)
            seconds = tk["seconds"]
            f.close()
            while True:
                time.sleep(1)
                seconds += 1
                global time_active  # time active to show in the console
                time_active = (str(int(seconds)))
                if stop == True: 
                    break
                with open('time_keeper',
                          'w') as tk:  # updates the time_keeper file so that is doesn't loose time once the program
                    # is closed
                    tk.write('seconds = ' + str(seconds) + '\n')
                    tk.close()
    except:  # Creates a new time_keeper file if one isn't found
        with open("time_keeper", 'w') as f:
            s = 0
            f.write('seconds = ' + str(int(s)) + '\n')
            f.close()


# funciton that checks for an active internet connection
def is_connected():
    try:
        requests.get('https://google.com')
        return True
    except:
        return False

@client.event
async def on_ready():
    channel = client.get_channel(977697637350375464)
    print("bacalhau is starting up! ⚡️")
    await channel.send("Starting up! ⚡️")
    log_exists = os.path.exists("Log")
    if log_exists == True:
        print("Log file found! ✅")
        await channel.send("Log file found! ✅")
    else:
        print("No log file found❌, creating a log file📝")
        await channel.send("No log file found❌, creating a log file📝")
        try:
            with open("log", 'w') as log:
                log.write("Log file started on" + str(datetime.now()) + "\n")
            print("Log file successfully created! ✅")
            await channel.send("Log file successfully created! ✅")
        except:
            print("Unable to create a log file, please check permissions and space left on device.❌")
            await channel.send("Unable to create a log file, please check permissions and space left on device.❌")
            pass
    await channel.send("All systems online, bacalhau is up and swimming :person_swimming:")
    print('{0.user} is now online! ✅\n'.format(client))

async def responses(message, userid, user):
    Admins = [692424917995618384, 695668988444672100] #El Madeirense, Noah🖕
    if message.author == client.user:
        return
    for word in thanks:
        if word in message.content.lower():
            thanks_true = True
            break
        else:
            thanks_true = False
    for word in bacalhau:
        if word in message.content.lower():
            bacalhau_true = True
            break
        else:
            bacalhau_true = False
    for word in sorry:
        if word in message.content.lower():
            sorry_true = True
            break
        else:
            sorry_true = False
    for word in gm:
        if word in message.content.lower():
            gm_true = True
            break
        else:
            gm_true = False
    for word in hey:
        if word in message.content.lower():
            hey_true = True
            break
        else:
            hey_true = False
    for word in links:
        if word in message.content:
            linkss = True
            break
        else:
            linkss = False
    for word in login:
        if word in message.content:
            loginn = True
            break
        else:
            loginn = False
    if message.content.startswith(("hello there", "Hello there")):
        await message.channel.send("General Kenobi")
    if hey_true and bacalhau_true:
        await message.channel.send("Hey there! " + f"<@{userid}>" + ". What's up?👋")
    if message.content.startswith(('bacalhau.help', "bacalhau.help")):
        embed=discord.Embed(title="**Here are a few commands you can use with me:**",
        description="**User commands:**\n\
                **   - bacalhau.progress -->** Shows the current Journey progress in time %\n\
                **   - bacalhau.uptime -->** Shows how long I've been awake for\n\
                **   - bacalhau.take five -->** I'll go to sleep for five minutes, in case you want to say my name without calling me\n\
        **Admin only commands:**\n\
                **   - bacalhau.purge -->** Deletes all the messages in the current channel\n\
                **   - bacalhau.log-file -->** Sends the last 10 messages in the log file\n\
                **   - bacalhau.reboot -->** Reboots me in case I'm doing something I'm not supposed to \n\
                **   - bacalhau.STOP! -->** Completely shuts me down, should only be used as a last resort \n",
        color=discord.Color.blue())
        await message.channel.send("Heyy " + f"<@{userid}>" + "\n",embed=embed)
    if message.content.startswith("bacalhau.git"):
        embed=discord.Embed(title="Bacalhau on GitHub",
        url="https://github.com/BunyMan/Bot_Bacalhau.git",
        description="Hey " +f"<@{userid}>" + ", here's what makes me work and down here are my creators 👇",
        color=discord.Color.blue())
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/25/25231.png")
        await message.channel.send(embed=embed)
        embed=discord.Embed(title="BunyMan's GitHub",
        url="https://github.com/BunyMan",
        description="⚡️kachow⚡️",
        color=discord.Color.blue())
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/25/25231.png")
        await message.channel.send(embed=embed)
        embed=discord.Embed(title="GlitchyMako's GitHub",
        url="https://github.com/GlitchyMako",
        description="I'm a Game Developer in Progress 🐺",
        color=discord.Color.blue())
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/25/25231.png")
        await message.channel.send(embed=embed)
    if userid in Admins and message.content.startswith(("bacalhau.reboot", "bacalhau.reboot", "bacalhau, reboot")):
        await message.channel.send("Rebooting process inicialized! ❌ bacalhau will be down for a few seconds")
        print("bacalhau is rebooting...")
        await message.channel.send("Shutting down... <:codhold:977712053101928448>")
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif user not in Admins and message.content.startswith(("bacalhau.reboot", "bacalhau.reboot", "bacalhau, reboot")):
        await message.channel.send("Hey " + f"<@{userid}>"+ ", that's an admin only command!")
    if userid in Admins and message.content.startswith(("bacalhau, go to sleep", "Bacalhau, go to sleep")):
        await message.channel.send("I'll be back!")
        activity = discord.Game(name="Dead")
        await client.change_presence(status=discord.Status.idle, activity=activity)
        time.sleep(300)
        await message.channel.send("My 5 minutes are up, I'm back!")
    elif user not in Admins and message.content.startswith(("bacalhau.take five", "bacalhau, take five")):
        await message.channel.send("Hey " + f"<@{userid}>"+ ", that's an admin only command!")
    if message.content.startswith("bacalhau.uptime") or message.content.startswith("bacalhau.uptime"):
        with open("time_keeper", 'r') as f:
            tk = toml.load(f)
            seconds = tk["seconds"]
            f.close()
            await message.channel.send("I've been awake for " + str(seconds) + " seconds, now do the math.")
    if message.content.startswith("bacalhau.norris"):
        response = requests.get("https://api.chucknorris.io/jokes/random")
        json_data = json.loads(response.text)
        quote = json_data["value"]
        await message.channel.send(str(quote))
    if user in Admins and message.content.startswith(("bacalhau.log-file", "bacalhau.log-file")):
        with open("Log") as f:
            for line in (f.readlines() [-10:]):
                await message.channel.send(line)
        await message.channel.send(line)
    elif user not in Admins and message.content.startswith(("bacalhau.log-file", "bacalhau.log-file")):
        await message.channel.send("Hey, " + f"<@{userid}>" + ", only admins can use that command!")
    if "bacalhau?" in message.content or "Bacalhau?" in message.content:
        await message.channel.send("Still swimming... 🤖")
    if gm_true:
        await message.channel.send("Good morning!! <:codthink:977711037287632996>")
    if thanks_true and bacalhau_true:
        await message.channel.send("<:uwu:977715133113577492>")
    if sorry_true and bacalhau_true:
        await message.channel.send("No problem, " + f"<@{userid}>" + ". Don't worry about it!")
    if message.content.startswith("ping") or message.content.startswith("Ping"):
        await message.channel.send("pong 🏓")
    if userid in Admins and message.content.startswith("bacalhau.purge") or message.content.startswith("Bacalhau.purge"):
        await message.channel.send("🐟")
        time.sleep(1)
        await message.channel.purge()
        os.system("clear")
        print("Channel was purged!")
    elif user not in Admins and message.content.startswith("bacalhau.purge") or message.content.startswith("Bacalhau.purge"):
        await message.channel.send("Hey, " + f"<@{userid}>" + ", only admins can use that command!")
    if "fuck bacalhau" in message.content:
        await message.channel.send("<:middlepepe:977715133491064952>")
    if message.content.startswith("bacalhau.level"):
        with open("Log", 'r') as f:
            data = f.read()
            count = data.count(user)
            level = int(count / 30) 
            msg = await message.channel.send("Heyyy " + f"<@{userid}>" + ", you're currently at level **" + str(level) + "**. \nThe more messages you send, the higher your level gets!")
            await msg.add_reaction("👍")
            await msg.add_reaction("🖕")
            #await message.add_reaction("😱")
    if "Nice" in message.content or "nice" in message.content or "noice" in message.content:
        await message.channel.send("Podes crer que é nice!")
    if message.content.startswith("bacalhau.terminal"):
        while True:
            msg = input("input message to send: ")
            if msg == "end" or msg == "":
                await message.channel.send("Chat with terminal has ended")
                break
            else:
                await message.channel.send(msg)
    if linkss:
        await message.channel.send("<https://pin.it/684ijga>")
        await message.channel.send("<https://azgaar.github.io/Fantasy-Map-Generator/>")
        await message.channel.send("<https://www.aiva.ai/>")
        await message.channel.send("<https://www.nuclino.com/>")
        await message.channel.send("<https://assetstore.unity.com/?gclid=EAIaIQobChMIyafvuKSI-gIVzpBoCR2YKgYqEAAYASAAEgLtV_D_BwE&gclsrc=aw.ds>")
    if loginn:
        await message.channel.send("Pede os dados de login a um membro da board")
    if message.content == "🖕":
        await message.add_reaction("🖕")
               
@client.event
async def on_message(message):
    print(message.content)
    activity = discord.Game(name="Master Baiter")
    await client.change_presence(status=discord.Status.online, activity=activity)
    threading.Thread(target=timer).start()
    user = message.author.name
    userid = message.author.id
    Admins = ["El Madeirense", "Garrett"]
    global stop
    stop = False
    try:
        try:
            with open("Log", 'a') as log:
                log.write(user + " --> on " + str(datetime.datetime.now()) + " -->  " + str(message.content) + "\n")
                log.close
        except:
            print("Unable to write to log file ❌")
        try:
            print(user + " --> on " + str(datetime.datetime.now()) + " --> '" + str(message.content) + "'")
        except:
            print(user)
    except:
        print("Couldn't get username")
    if user in Admins and message.content.startswith("bacalhau.STOP!") or message.content.startswith("Bacalhau.STOP!") or message.content.startswith("bacalhau, STOP!") or message.content.startswith("bacalhau, STOP!"):
        await message.channel.send("<:codhold:977712053101928448>")
        stop = True
        time.sleep(1)
        exit()
    elif user not in Admins and message.content.startswith("bacalhau.STOP!") or message.content.startswith("bacalhau.STOP!") or message.content.startswith("bacalhau, STOP!") or message.content.startswith("bacalhau, STOP!"):
        await message.channel.send("Hey " + f"<@{userid}>" + ", only admins can use that command!")
    try:
        if is_connected():
            await responses(message, userid, user)
        else:
            print("Not connected to internet ❌")
    except Exception:
        await message.channel.send(f"<@{userid}>" + " Oops, that didn't work! Please report this :)")
        print("Warning, something failed. Please check for user report.")
        traceback.print_exc()

@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edited a message.\n'
        f'The original message was: {before.content}\n'
    )

@client.event
async def on_reaction_add(reaction, user, userid):
    # bacalhau = 973565627291820042
    if str(user) != "Bacalhau#6891":
        if reaction.emoji == "🖕":
            await reaction.message.channel.send(f"{userid} 🖕")
        #await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')
        print(str(reaction.emoji))

client.run('OTczNTY1NjI3MjkxODIwMDQy.GVL7cp.pdUGL8WLhbZZPVksyXskgI8R4Kf4ZYCwH1zgN8') #fake token btw
