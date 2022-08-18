import hikari
import datetime
import lightbulb
from mars.utils import cc
import mars.managers.logging_mg as logs
import mars.utils.nettools as nets

##################################################################

plugin = lightbulb.Plugin("ping_cmd")

##################################################################

# STORE COMMAND
@plugin.command
@lightbulb.command('store', 'our store !')
@lightbulb.implements(lightbulb.SlashCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:

    store_qr = nets.generate_qr(cc.store)
    
    embed = hikari.Embed(title=f"{cc.verified_emoji} Oficial Store",
                          description=f"{cc.store}",
                          color=cc.main_color)
    embed.set_thumbnail(f"{store_qr}")

    try:
        await ctx.respond(embed,
                          flags=hikari.MessageFlag.EPHEMERAL)
    except:
        await ctx.respond(cc.error_msg,
                          flags=hikari.MessageFlag.EPHEMERAL)

    logs.out(f'"store" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')
                

# TWITTER COMMAND
@plugin.command
@lightbulb.command('twitter', 'our twitter !')
@lightbulb.implements(lightbulb.SlashCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:

    twitter_qr = nets.generate_qr(cc.twitter)

    embed = hikari.Embed(title=f"{cc.verified_emoji} Oficial Twitter",
                          description=f"{cc.twitter}",
                          color=cc.main_color)
    embed.set_thumbnail(f"{twitter_qr}")

    try:
        await ctx.respond(embed,
                          flags=hikari.MessageFlag.EPHEMERAL)
    except:
        await ctx.respond(cc.error_msg,
                          flags=hikari.MessageFlag.EPHEMERAL)

    logs.out(f'"twitter" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')


# GITHUB COMMAND
@plugin.command
@lightbulb.command('github', 'our github !')
@lightbulb.implements(lightbulb.SlashCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:

    github_qr = nets.generate_qr(cc.github)

    embed = hikari.Embed(title=f"{cc.verified_emoji} Oficial Github",
                          description=f"{cc.github}",
                          color=cc.main_color)
    embed.set_thumbnail(f"{github_qr}")

    try:
        await ctx.respond(embed,
                          flags=hikari.MessageFlag.EPHEMERAL)
    except:
        await ctx.respond(cc.error_msg,
                          flags=hikari.MessageFlag.EPHEMERAL)

    logs.out(f'"github" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')    


# IP COMMAND
@plugin.command
@lightbulb.command('ip', 'minecraft IP !')
@lightbulb.implements(lightbulb.SlashCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:

    embed = hikari.Embed(title=f"{cc.verified_emoji} Oficial Minecraft Server ip",
                          description=f"{cc.ip}",
                          color=cc.main_color)
    embed.set_thumbnail(f"{cc.logo_url}")

    try:
        await ctx.respond(embed,
                          flags=hikari.MessageFlag.EPHEMERAL)
    except:
        await ctx.respond(cc.error_msg,
                          flags=hikari.MessageFlag.EPHEMERAL)

    logs.out(f'"ip" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')             

##################################################################

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)