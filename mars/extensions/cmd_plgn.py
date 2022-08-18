import hikari
import lightbulb
from mars.utils import cc
import mars.managers.plugin_mg as plmg
import mars.managers.logging_mg as logs

########################################################################

plugin = lightbulb.Plugin("ping_cmd")

########################################################################
# COMMAND GROUP
@plugin.command
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role),
                      lightbulb.has_roles(cc.developer_role),lightbulb.has_roles(cc.owner_role))
@lightbulb.command('plugin', 'plugin main command.')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def plugin_command_group(ctx: lightbulb.Context) -> None:
    pass

########################################################################
# PLUGIN RELOAD
@plugin_command_group.child
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role), 
                      lightbulb.has_roles(cc.developer_role),lightbulb.has_roles(cc.owner_role))
@lightbulb.command('reload', 'list of all the plugins')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:    
    await ctx.bot.close()
    await ctx.bot.start()

    await ctx.respond(f"bot sucesfully reloaded", flags=hikari.MessageFlag.EPHEMERAL)


########################################################################
# CREATE PLUGIN
@plugin_command_group.child
@lightbulb.option("name",  "name of the plugin", type=str, required=True)
@lightbulb.option("version",  "version of the plugin", type=str, required=True)
@lightbulb.option("ffa",  "name of the plugin", type=str, required=False)
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role), 
                      lightbulb.has_roles(cc.developer_role),lightbulb.has_roles(cc.owner_role))
@lightbulb.command('create', 'create a new plugin.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:
    
    opt_name = ctx.options.name
    opt_version = ctx.options.version
    
    ########################################################################
    
    try:
        category = await ctx.bot.rest.create_guild_category(name=f"{opt_name}", guild=cc.server_id)     
        category_id = category.id
        
        about_channel = await ctx.bot.rest.create_guild_text_channel(name="about", guild=cc.server_id, category=category_id)   
        about_channel_id = about_channel.id
        
        update_channel = await ctx.bot.rest.create_guild_text_channel(name="updates", guild=cc.server_id, category=category_id)  
        update_channel_id = update_channel.id
        
        ########################################################################
        
        plmg.create_plugin(opt_name, category_id, about_channel_id, update_channel_id, opt_version)
        
        ########################################################################
        
        confirmation_msg = hikari.Embed(title=f"""
{cc.correct_emoji} sucesfully created the plugin ```{opt_name}```""", description=f"""

>>> {cc.channel_emoji} <#{about_channel_id}>
{cc.channel_emoji} <#{update_channel_id}>""",

                                    color=cc.correct_color) 
        await ctx.respond(confirmation_msg, flags=hikari.MessageFlag.EPHEMERAL) 
        
    except:
        confirmation_msg = hikari.Embed(title=f"{cc.wrong_color} an error occurred creating the plugin```{opt_name}```",
                                        color=cc.wrong_color) 
        await ctx.respond(confirmation_msg, flags=hikari.MessageFlag.EPHEMERAL) 
    
    logs.out(f'"plugin create" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')

########################################################################
# PLUGIN DELETE
@plugin_command_group.child
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role), 
                      lightbulb.has_roles(cc.developer_role),lightbulb.has_roles(cc.owner_role))
@lightbulb.option("plugin",  "plugin to delete", type=str, required=True, choices=plmg.list_plugins().values())
@lightbulb.command('delete', 'delete a plugins')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:
    
    ########################################################################
    
    await ctx.respond(f"deleting plugin: {str(plugin)}", flags=hikari.MessageFlag.EPHEMERAL)
    
    opt_plugin = ctx.options.plugin
    checked = plmg.check_plugin(str(opt_plugin))
    
    ########################################################################
    
    category_to_delete = plmg.get_from_plugin("category_id", str(opt_plugin))
    about_channel_to_delete = plmg.get_from_plugin("about_id", str(opt_plugin))
    update_channel_to_delete = plmg.get_from_plugin("update_id", str(opt_plugin))
    
    ########################################################################
    
    try:
        
        await ctx.bot.rest.delete_channel(about_channel_to_delete)
        await ctx.respond(f"about channel deleted of **{str(checked)}**", flags=hikari.MessageFlag.EPHEMERAL)
        await ctx.bot.rest.delete_channel(update_channel_to_delete)
        await ctx.respond(f"about channel deleted of **{str(checked)}**", flags=hikari.MessageFlag.EPHEMERAL)
        await ctx.bot.rest.delete_channel(category_to_delete)
        await ctx.respond(f"category of **{str(checked)}** deleted", flags=hikari.MessageFlag.EPHEMERAL)


        plmg.delete_plugin(str(checked))
       
        confirmation_msg = hikari.Embed(title=f"{cc.correct_emoji} sucesfully deleted the plugin ```{opt_plugin}```",
                                    color=cc.correct_color) 
        await ctx.respond(confirmation_msg, flags=hikari.MessageFlag.EPHEMERAL) 
    
    except:
        confirmation_msg = hikari.Embed(title=f"{cc.wrong_color} an error occurred deleteing the plugin```{opt_plugin}```",
                                        color=cc.wrong_color) 
        await ctx.respond(confirmation_msg, flags=hikari.MessageFlag.EPHEMERAL) 

    
        
    ########################################################################
    
    logs.out(f'"plugin delete" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')

########################################################################
# PLUGIN LIST
@plugin_command_group.child
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role), 
                      lightbulb.has_roles(cc.developer_role),lightbulb.has_roles(cc.owner_role))
@lightbulb.command('list', 'list of all the plugins')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:    
    plugins = plmg.list_plugins()
    
    ########################################################################
    
    counter = 0
    
    confirmation_msg = hikari.Embed(title=f"List of all the active plugins: ")
    
    for plugin in plmg.list_plugins().values():
        counter += 1
        pl_version = plmg.get_from_plugin("version", str(plugin))
        
        confirmation_msg.add_field(name=f"```{counter} | {plugin}```:", value=f"*version {pl_version}*", inline=False)  
        
    await ctx.respond(confirmation_msg, flags=hikari.MessageFlag.EPHEMERAL) 
        
    ########################################################################
    
    logs.out(f'"plugin list" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')

########################################################################

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)
    