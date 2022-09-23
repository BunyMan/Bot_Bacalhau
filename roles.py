# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    roles.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jbuny-fe <jbuny-fe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/30 11:31:29 by jbuny-fe          #+#    #+#              #
#    Updated: 2022/09/23 15:40:29 by jbuny-fe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import discord
from config import *

class MyClient(discord.Client):
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 1018245915712180285

    
    
    async def on_ready(self):
        print("Ready")

    async def on_raw_reaction_add(self, payload):
        if payload.message_id != self.target_message_id:
            return
        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name == "💪":
            role = discord.utils.get(guild.roles, name="BIXO")
            await payload.member.add_roles(role)
            print(f"Gave role {role} to {payload.member}")
        if payload.emoji.name == "🏓":
            role = discord.utils.get(guild.roles, name="Ball master")
            await payload.member.add_roles(role)
        if payload.emoji.name == "🐍":
            role = discord.utils.get(guild.roles, name="PyThOn BrOs")
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        if payload.message_id != self.target_message_id:
            return
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == "💪":
            role = discord.utils.get(guild.roles, name="BIXO")
            await member.remove_roles(role)
        if payload.emoji.name == "🏓":
            role = discord.utils.get(guild.roles, name="Ball master")
            await member.remove_roles(role)
        if payload.emoji.name == "🐍":
            role = discord.utils.get(guild.roles, name="PyThOn BrOs")
            await member.remove_roles(role)

    

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)

client.run('Haha no token for you')
