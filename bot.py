import discord
from discord.ext import commands
from LOLstat import winRate
from LOLstat import pickRate
from LOLstat import banRate

client = commands.Bot(command_prefix='.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Tanklyn'))    
    print('Online!')

@client.command()
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name = 'Commands')
    embed.add_field(name = '.list', value = 'use with \'all\' to print all champions, or give a single letter' +
                                            ' to print champions whose name starts with that letter', inline = False)
    embed.add_field(name = '.winrate', value = 'Returns champion win rate on current patch', inline = False)
    embed.add_field(name = '.banrate', value = 'Returns champion ban rate on current patch', inline = False)
    embed.add_field(name = '.pickrate', value = 'Returns champion pick rate on current patch', inline = False)
    embed.add_field(name = '.ping', value = 'Returns server ping in ms', inline = False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'Server ping: {round(client.latency * 1000)}ms')

@client.command()
async def list(ctx,tag):
    await ctx.send(listChamps(openExcel(),tag))

@client.command()
async def winrate(ctx, *, champion):
    await ctx.send(winRate(champion))

@client.command()
async def pickrate(ctx, *, champion):
    await ctx.send(pickRate(champion))

@client.command()
async def banrate(ctx, *, champion):
    await ctx.send(banRate(champion))

#key for discord bot
client.run('#################################')
