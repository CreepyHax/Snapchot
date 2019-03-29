import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext.commands import has_permissions
import random
import asyncio
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get
from discord import Game
 
 
bot = commands.Bot(command_prefix='.')
Snapchot='522126161799544833'
start=time.time()
bot.remove_command('help')
status = ('.help for commands', 'https://snapgg.weebly.com', 'Subscribe: Snapchot SG', "2019 Special!")

players = {}


async def change_status():
    await bot.wait_until_ready()
    msgs = cycle(status)

    while not bot.is_closed:
        current_status = next(msgs)
        await bot.change_presence(game=discord.Game(name =current_status, type=1))
        await asyncio.sleep(10)





@bot.event
async def on_ready():
        print("later")





@bot.command(pass_context=True)
async def help(ctx):
	
        commands={}
        commands['.help:arrow_up_down:']='`Show List Command`'
        commands['.website:biohazard_sign:']='***My Official Website!***'
        commands['.nuke:ballot_box_with_check:']='***This Commands Only For Snapchot!***'
        commands['.lucky:left_luggage:']='***Who Lucky? w Will Use This Commands!***'
        commands['.invite:white_check_mark:']='***How To Invite Ppl***'
        commands['.dm:clinking_glass:']='***Dm People Only For Snapchot!***'
        commands['.ping:chart_with_upwards_trend:']='**Type .ping For Know How Many Your MS**'
        commands['.whogay:radioactive_sign:']='***Who Is Gay? Use This Command!***'
        commands['.imgay:radioactive_sign:']='**U Gay Or No? Use This Command!**'
        commands['.info:bar_chart:']='***Type info For About Me!***'
        commands['.userinfo:bar_chart:']='***Info About <user>***'
        commands['.uptime:chart_with_upwards_trend:']='***To Know How Many Uptime!***'
        commands['.botcount:chart_with_downwards_trend:']='***How Many My Bot Join Disocrd***'
        commands['.avatar:frame_with_picture:']='***For Show Avatar People!***'
        commands['.world:world_map:']='***Find World In Growtopia GAME!***'
        commands['.purge:arrow_forward:']='___Type .purge<Number>___'
        commands['.warn:warning:']='***Warn People Only For Snapchot!***'
        commands['.mute:warning:']='***Mute People Only For Snapchot!***'
        commands['.unmute:warning:']='***Unmute People Only For Snapchot!***'
        commands['.kick:warning:']='***Kick Only For Snapchot!***'
        commands['.ban:warning:']='***For Ban People Only For Snapchot!***'
        commands['.presence:pray:']='***Change Presence Only For Snapchot!***'

        msg=discord.Embed(title='******COMMAND LIST!******', description="***Create By Snapchot*** ",color=0xF35353)
        for command,description in commands.items():
            msg.add_field(name=command,value=description, inline=False)
        msg.add_field(name='******INFORMATION!******',value='_Thanks Add If You Added My Bot!_', inline=False)
        await bot.whisper(embed=msg)
        await bot.say('***Check*** ___Dm___ ***For Information*** :mailbox:')
        

@bot.command(pass_context=True)
async def invite():
	await bot.say('___HOW TO INVITE___ ***Invite Many People To Join My Discord Official*** : https://discord.gg/qdbyBP')
	
@bot.command()
async def website():
	await bot.say('***Check DM For Information :mailbox:***')
	await bot.whisper('||@everyone|| `This Is My Official Website About How To Add My Bot` https://snapgg.weebly.com')
	
@bot.command(pass_context = True)
async def nuke(ctx, type):
	if ctx.message.author.id==(Snapchot):
		
	    t = await bot.say('Nuking World ***Be Patient***')
	    await bot.edit_message(t,f'***{type}*** ***>>***  ***was nuked from orbit , it the only way to be sure . play nice everybody!***')
	
@bot.command()
async def lucky():
	lucky = random.choice(['Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Normal','Gold'])
	await bot.say(lucky)
	
@bot.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)
        
@bot.command(pass_context = True)
async def dm(ctx, member : discord.Member, *, content: str):
    await bot.send_message(member, content)
    await bot.say('***User Get Dm From Me!***')
    
@bot.command()
async def bdm():
	   await bot.say('@everyone If You New Here Can U Sub My Creator Channel : ***Snapchot SG***')
	
@bot.command()
async def ping():
	await bot.say('`999+ MS`')
	
@bot.command()
async def whogay():
	whogay = random.choice(['***YOUR MOM***','***YOUR FATHER***','***YOUR GF / BF***'])
	await bot.say(whogay)
	
@bot.command()
async def imgay():
	imgay = random.choice(['*1%*','*2%*','*3%*','*4%*','*5%*','6%','7%','8%','9%','10%','11%','12%','13%','14%','15%','16%','17%','18%','19%','20%','21%','22%','23%','24%','25%','26%','27%','28%','29%','30%','40%','41%','42%','43%','44%','45%','46%','47%','48%','49%','50%','51%','52%','53%','53%','54%','55%','56%','57%','58%','59%','60%','61%','62%','63%','64%','65%','66%','67%','68%','69%','70%','71%','72%','73%','74%','75%','76%','77%','78%','79%','80%','81%','82%','83%','84%','85%','86%','87%','88%','89%','90%','91%','92%','93%','94%','95%','96%','97%','98%','99%','*100%*'])
	await bot.say(imgay)
	
@bot.command()
async def info():
	await bot.say('___Create By : Snapchot___')
	await bot.say('`Since : 1945`')
	await bot.say('***And Now Snapchot With Your Mom :D***')
	
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)

    await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def uptime(ctx):
	now=time.time()
	sec=int(now-start)
	mins=int(sec//60)
	await bot.say('***Uptime is*** ___59___ ***seconds!***')
	
@bot.command()
async def botcount():
  	"""Bot Guild Count"""
  	await bot.say("***I'm in {} Servers!***".format(len(bot.servers)))
  	
@bot.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
    """User Avatar"""
    await bot.reply("{}".format(member.avatar_url))
    
@bot.command(pass_context = True)
async def world(ctx, type):
    await bot.say('***Successfully!!***')
    await bot.say('https://growtopiagame.com/worlds/'f'{type}.png')
	
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx,num:int):
	if ctx.message.author.id==(Snapchot):
		await bot.purge_from(ctx.message.channel,limit=num)
		await bot.say('***Text Has Been Cleared From Me***')
	else:
		await bot.say('___No Perms!___')
	
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def warn(ctx,target:discord.Member):
	if ctx.message.author.id==(Snapchot):
	  await bot.say(':white_check_mark:***User Has been Warned!***')
	else:
		await bot.say('***No Perms!***')
	await bot.send_message(target,'***Pls See The Rules Madafaqa***:mailbox:')
	
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def mute(ctx,target:discord.Member):
	if ctx.message.author.id==(Snapchot):
    	        role=discord.utils.get(ctx.message.author.server.roles,name='Muted')
	
	await bot.add_roles(target,role)
	await bot.say(target.mention +'***Was Muted!***')
	
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unmute(ctx,target:discord.Member):
	if ctx.message.author.id==(Snapchot):

    	        role=discord.utils.get(ctx.message.author.server.roles,name='Muted')

	await bot.remove_roles(target,role)
	await bot.say(target.mention +'***Has been unmuted!***')
	
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def kick(ctx, target: discord.Member):	
    await bot.kick(target)
    await bot.say(terget,':white_check_mark: ***User Has Been Kick From Discord!***')
 
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def ban(ctx, userName: discord.Member):
    await bot.ban(userName)
    await bot.say('***User Has Been Banned From Discord!***')
    
@bot.command(pass_context=True)
async def presence(ctx,text:str,type:int):
	if ctx.message.author.id==(Snapchot):
		await bot.change_presence(game=discord.Game(name=text,type=type))
		await bot.say('**Succesfully Presence Got Changed!**')
	else:
		await bot.say('***No Perms!***')
        
 
bot.loop.create_task(change_status())
bot.run("NTU5ODEzNDUzNDgxNTA4OTI2.D3q3Eg.abSmMYbOss9kpALq_aZhdzXGFAM")