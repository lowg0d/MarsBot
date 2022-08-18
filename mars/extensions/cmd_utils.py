import hikari
import datetime
import lightbulb
from mars.utils import cc
from mars import __version__
import mars.managers.logging_mg as logs

##################################################################

plugin = lightbulb.Plugin("ping_cmd")

##################################################################

# PING COMMAND
@plugin.command
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role))
@lightbulb.command('ping', 'pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:
    await ctx.respond('Pong!', flags=hikari.MessageFlag.EPHEMERAL)

    logs.out(f'"ping" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')

# VERSION COMMAND
@plugin.command
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role))
@lightbulb.command('version', 'the version of the bot.')
@lightbulb.implements(lightbulb.SlashCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title=f"Bot Version  {cc.settings_emoji}",
                         description=f">>> **bot version:** ```{__version__}```\n**Author:** <@814476198733152266>",
                         color=cc.main_color)

    await ctx.respond(embed, flags=hikari.MessageFlag.EPHEMERAL)

    logs.out(f'"version" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')

# CLEAR COMMAND
@plugin.command
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role))
@lightbulb.option("count", "The amount of messages to clear.", type=int, max_value=100, min_value=1, required=False, default=10)
@lightbulb.command("clear", "Purge a certain amount of messages from a channel.", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def purge(ctx: lightbulb.SlashContext, count: int) -> None:
    if not ctx.guild_id:
        await ctx.respond("This command can only be used in a server.",
                          flags=hikari.MessageFlag.EPHEMERAL)
        return

    messages = (
        await ctx.app.rest.fetch_messages(ctx.channel_id)
        .take_until(lambda m: datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=14) > m.created_at)
        .limit(count))

    if messages:
        
        embed = hikari.Embed(title=f"{cc.correct_emoji}  [{len(messages)}] messages cleared.",
                          color=cc.correct_color)
        
        await ctx.app.rest.delete_messages(ctx.channel_id, messages)
        await ctx.respond(embed,
                          flags=hikari.MessageFlag.EPHEMERAL)

    else:
        
        embed = hikari.Embed(title=f"{cc.wrong_emoji}  Could not find any messages younger than 14 days!",
                    color=cc.wrong_color)
        
        await ctx.respond(embed,
                          flags=hikari.MessageFlag.EPHEMERAL)

    logs.out(f'"clear" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')

##################################################################

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)