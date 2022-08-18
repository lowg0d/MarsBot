from email.mime import image
import hikari
import lightbulb
from mars.utils import cc
import mars.utils.posttools as postt
import mars.managers.plugin_mg as plmg
import mars.managers.logging_mg as logs

##################################################################

plugin = lightbulb.Plugin("ping_cmd")

##################################################################
# COMMAND GROUP

@plugin.command
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role),
                      lightbulb.has_roles(cc.developer_role),lightbulb.has_roles(cc.owner_role))
@lightbulb.command('post', 'create a new post.')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def post_command_group(ctx: lightbulb.Context) -> None:
    pass

########################################################################
# POST EMBED
@post_command_group.child
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role), 
                      lightbulb.has_roles(cc.developer_role),lightbulb.has_roles(cc.owner_role))
@lightbulb.option("title",  "tittle of the strat post", type=str, required=True)
@lightbulb.option("description",  "description og the strat post", type=str, required=False, default=None)
@lightbulb.option("img",  "attached img", type=str, required=False, default=None)
@lightbulb.option("video",  "attached video", type=str, required=False, default=None)
@lightbulb.option("thumbnail",  "post thumbnail", type=str, required=False, default=None)
@lightbulb.option("url",  "url of what do you want to post", type=str, required=False, default="")
@lightbulb.option("footer",  "url of what do you want to post", type=str, required=False, default="discord.orbitdev.net")
@lightbulb.option("channel", "Select channel", hikari.TextableGuildChannel, 
                  required=True, channel_types=[hikari.ChannelType.GUILD_TEXT], default=None)
@lightbulb.option("everyone",  "mention everyone", type=str, default="False", choices=["True", "False"])
@lightbulb.command('embed', 'publish a new embed.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:
    ####################################
    # options
    opt_title = ctx.options.title
    opt_information = ctx.options.description
    opt_url = ctx.options.url
    opt_img = ctx.options.img
    opt_thumbnail = ctx.options.thumbnail 
    opt_footer = ctx.options.footer
    opt_channel = ctx.options.channel
    opt_everyone = ctx.options.everyone
    opt_video = ctx.options.video
    
    ####################################
    # save command executor id and name
    command_executor = ctx.author
    command_executor_id = command_executor.id

    ####################################
    # send the message
    
    # ping everyone
    if opt_everyone == "True":
        await ctx.bot.rest.create_message(opt_channel, f"{cc.pin_emoji} ||@everyone||", mentions_everyone=True)
    
    embed_post = postt.embed(opt_title, opt_information, opt_url, opt_footer, opt_img, opt_thumbnail, opt_video)
    embed_message = await ctx.bot.rest.create_message(opt_channel, embed_post, mentions_everyone=True)        
        
    ####################################
    #get message needed properties
    
    message_id = embed_message.id
    message_channel_id = embed_message.channel_id
    message_link = f"https://discord.com/channels/953062983687372830/{message_channel_id}/{message_id}" 
    
    ####################################
    
    confirmation_msg = hikari.Embed(title=f"{cc.correct_emoji} Sucesfully posted new embed message",
                          description=f"""
**Title:** ```{opt_title}```
**Description:** ```{opt_information}```
**Everyone:** ```{opt_everyone}```

>>> {cc.channel_emoji} <#{message_channel_id}>
{cc.link_emoji} [Go To Message]({message_link})
""",
                          color=cc.correct_color,
                          url=message_link)

    await ctx.respond(confirmation_msg, flags=hikari.MessageFlag.EPHEMERAL)
    
    logs.out(f'"post embed" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')

########################################################################
# POST IMAGE
@post_command_group.child
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role), 
                      lightbulb.has_roles(cc.developer_role),lightbulb.has_roles(cc.owner_role))
@lightbulb.option("img",  "attached img", type=str, required=True, default=None)
@lightbulb.option("channel", "Select channel", hikari.TextableGuildChannel, 
                  required=True, channel_types=[hikari.ChannelType.GUILD_TEXT], default=None)
@lightbulb.command('image', 'publish a new embed image.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:
    ####################################
    # options
    opt_img = ctx.options.img
    opt_channel = ctx.options.channel

    embed_post = hikari.Embed(color=cc.main_color)
    embed_post.set_image(opt_img)
    embed_message = await ctx.bot.rest.create_message(opt_channel, embed_post)
    message_id = embed_message.id
    message_channel_id = embed_message.channel_id
    message_link = f"https://discord.com/channels/953062983687372830/{message_channel_id}/{message_id}" 
        
    confirmation = hikari.Embed(title=f"{cc.correct_emoji} Sucesfully posted new embed image.", 
                                description=f">>> {cc.link_emoji} [Go To Message]({message_link}) ")    

########################################################################

# POST BUGFIX
@post_command_group.child
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role), 
                      lightbulb.has_roles(cc.developer_role),lightbulb.has_roles(cc.owner_role))
@lightbulb.option("title",  "tittle of the strat post", type=str, required=True)
@lightbulb.option("description",  "description og the strat post", type=str, required=False, default=" ")
@lightbulb.option("plugin",  "plugin to update", type=str, required=True, choices=plmg.list_plugins().values())
@lightbulb.option("img",  "attached img", type=str, required=False, default=None)
@lightbulb.option("thumbnail",  "post thumbnail", type=str, required=False, default=None)
@lightbulb.option("url",  "url of what do you want to post", type=str, required=False, default="")
@lightbulb.command('bugfix', 'post bug fix xd')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:
    
    ####################################
    # options
    opt_title = ctx.options.title
    opt_information = ctx.options.description
    opt_url = ctx.options.url
    opt_img = ctx.options.img
    opt_thumbnail = ctx.options.thumbnail 
    opt_plugin = ctx.options.plugin
    
    pl_version = plmg.get_from_plugin("version", str(opt_plugin))
    
    ########################################################################
    
    message_embed = postt.bug_fix_post(opt_title, opt_information, opt_url, opt_img, opt_thumbnail, opt_plugin, pl_version)
    update_channel_id = plmg.get_from_plugin("update_id", str(opt_plugin))
    
    ########################################################################
    
    embed_message = await ctx.bot.rest.create_message(update_channel_id, message_embed)
    
    message_id = embed_message.id
    message_channel_id = embed_message.channel_id
    message_link = f"https://discord.com/channels/953062983687372830/{message_channel_id}/{message_id}" 
    
    ########################################################################
    
    confirmation_msg = hikari.Embed(title=f"{cc.correct_emoji} Sucesfully posted new bug fix for **{opt_plugin}-{pl_version}**", description=f"""
**Title:** ```{opt_title}```
**Description:** ```{opt_information}```

>>> {cc.channel_emoji} <#{message_channel_id}>
{cc.link_emoji} [Go To Message]({message_link})
""")
    
    await ctx.respond(confirmation_msg, flags=hikari.MessageFlag.EPHEMERAL)
    
    ########################################################################
    
    logs.out(f'"plugin bugfix" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')

########################################################################
# POST UPDATE
@post_command_group.child
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role), 
                      lightbulb.has_roles(cc.developer_role),lightbulb.has_roles(cc.owner_role))
@lightbulb.option("title",  "tittle of the strat post", type=str, required=True)
@lightbulb.option("description",  "description og the strat post", type=str, required=False, default=" ")
@lightbulb.option("plugin",  "plugin to update", type=str, required=True, choices=plmg.list_plugins().values())
@lightbulb.option("img",  "attached img", type=str, required=False, default=None)
@lightbulb.option("thumbnail",  "post thumbnail", type=str, required=False, default=None)
@lightbulb.option("url",  "url of what do you want to post", type=str, required=False, default="")
@lightbulb.command('update', 'post bug fix xd')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:
    ####################################
    # options
    opt_title = ctx.options.title
    opt_information = ctx.options.description
    opt_url = ctx.options.url
    opt_img = ctx.options.img
    opt_thumbnail = ctx.options.thumbnail 
    opt_plugin = ctx.options.plugin
    
    pl_version = plmg.get_from_plugin("version", str(opt_plugin))
    
    ########################################################################
    
    message_embed = postt.update_post(opt_title, opt_information, opt_url, opt_img, opt_thumbnail, opt_plugin, pl_version)
    update_channel_id = plmg.get_from_plugin("update_id", str(opt_plugin))
    
    ########################################################################
    
    embed_message = await ctx.bot.rest.create_message(update_channel_id, message_embed)
    
    message_id = embed_message.id
    message_channel_id = embed_message.channel_id
    message_link = f"https://discord.com/channels/953062983687372830/{message_channel_id}/{message_id}" 
    
    ########################################################################
    
    confirmation_msg = hikari.Embed(title=f"{cc.correct_emoji} Sucesfully posted new plugin update for **{opt_plugin}-{pl_version}**", description=f"""
**Title:** ```{opt_title}```
**Description:** ```{opt_information}```

>>> {cc.channel_emoji} <#{message_channel_id}>
{cc.link_emoji} [Go To Message]({message_link})
""")
    
    await ctx.respond(confirmation_msg, flags=hikari.MessageFlag.EPHEMERAL)
    
    ########################################################################

    logs.out(f'"plugin update" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')

########################################################################
# POST NEW FEATURE
@post_command_group.child
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role), 
                      lightbulb.has_roles(cc.developer_role),lightbulb.has_roles(cc.owner_role))
@lightbulb.option("title",  "tittle of the strat post", type=str, required=True)
@lightbulb.option("description",  "description og the strat post", type=str, required=False, default=" ")
@lightbulb.option("plugin",  "plugin to update", type=str, required=True, choices=plmg.list_plugins().values())
@lightbulb.option("img",  "attached img", type=str, required=False, default=None)
@lightbulb.option("thumbnail",  "post thumbnail", type=str, required=False, default=None)
@lightbulb.option("url",  "url of what do you want to post", type=str, required=False, default="")
@lightbulb.command('newfeature', 'post bug fix xd')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:
    
    ####################################
    # options
    opt_title = ctx.options.title
    opt_information = ctx.options.description
    opt_url = ctx.options.url
    opt_img = ctx.options.img
    opt_thumbnail = ctx.options.thumbnail 
    opt_plugin = ctx.options.plugin
    
    pl_version = plmg.get_from_plugin("version", str(opt_plugin))
    
    ########################################################################
    
    message_embed = postt.new_feature_post(opt_title, opt_information, opt_url, opt_img, opt_thumbnail, opt_plugin, pl_version)
    update_channel_id = plmg.get_from_plugin("update_id", str(opt_plugin))
    
    ########################################################################
    
    embed_message = await ctx.bot.rest.create_message(update_channel_id, message_embed)

    message_id = embed_message.id
    message_channel_id = embed_message.channel_id
    message_link = f"https://discord.com/channels/953062983687372830/{message_channel_id}/{message_id}" 
    
    ########################################################################
    
    confirmation_msg = hikari.Embed(title=f"{cc.correct_emoji} Sucesfully posted new feature for **{opt_plugin}-{pl_version}**", description=f"""
**Title:** ```{opt_title}```
**Description:** ```{opt_information}```

>>> {cc.channel_emoji} <#{message_channel_id}>
{cc.link_emoji} [Go To Message]({message_link})
""")
    
    await ctx.respond(confirmation_msg, flags=hikari.MessageFlag.EPHEMERAL)

    ########################################################################
    
    logs.out(f'"plugin update" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')
    
########################################################################
# POST ABOUT
@post_command_group.child
@lightbulb.add_checks(lightbulb.has_roles(cc.admin_role), 
                      lightbulb.has_roles(cc.developer_role),lightbulb.has_roles(cc.owner_role))
@lightbulb.option("title",  "tittle of the strat post", type=str, required=True)
@lightbulb.option("features_title",  "tittle of the strat post", type=str, required=True)
@lightbulb.option("commands_title",  "tittle of the strat post", type=str, required=True)
@lightbulb.option("title",  "tittle of the strat post", type=str, required=True)
@lightbulb.option("features",  "tittle of the strat post", type=str, required=True)
@lightbulb.option("commands",  "tittle of the strat post", type=str, required=True)
@lightbulb.option("emoji",  "tittle of the strat post", type=str, required=True)
@lightbulb.option("emoji_id",  "tittle of the strat post", type=str, required=True)
@lightbulb.option("description",  "description og the strat post", type=str, required=False, default=" ")
@lightbulb.option("plugin",  "plugin to update", type=str, required=True, choices=plmg.list_plugins().values())
@lightbulb.option("img",  "attached img", type=str, required=False, default=None)
@lightbulb.option("thumbnail",  "post thumbnail", type=str, required=False, default=None)
@lightbulb.option("url",  "url of what do you want to post", type=str, required=False, default="")
@lightbulb.command('about', 'post about text')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def presence_command_group(ctx: lightbulb.Context) -> None:
    ####################################
    # options
    opt_title = ctx.options.title
    opt_information = ctx.options.description
    opt_url = ctx.options.url
    opt_img = ctx.options.img
    opt_thumbnail = ctx.options.thumbnail 
    opt_plugin = ctx.options.plugin
    opt_features_title = ctx.options.features_title
    opt_commands_title = ctx.options.commands_title
    opt_features = ctx.options.features
    opt_commands = ctx.options.commands
    opt_emoji = ctx.options.emoji
    opt_emoji_id = ctx.options.emoji_id
    
    pl_version = plmg.get_from_plugin("version", str(opt_plugin))
    
    reformated_commands = str(opt_commands).replace("$", """
                                                    """)
    
    reformated_features = str(opt_features).replace("$", """
                                                    """)
    
    ########################################################################
    
    message_embed = postt.about_post(opt_title, opt_information, opt_url, opt_img, opt_thumbnail, 
                                     opt_plugin, pl_version, opt_features_title, opt_commands_title,
                                     reformated_features, reformated_commands, opt_emoji, opt_emoji_id)

    about_channel_id = plmg.get_from_plugin("about_id", str(opt_plugin))
    
    ########################################################################
    
    embed_message = await ctx.bot.rest.create_message(about_channel_id, message_embed)

    message_id = embed_message.id
    message_channel_id = embed_message.channel_id
    message_link = f"https://discord.com/channels/953062983687372830/{message_channel_id}/{message_id}" 
    
    ########################################################################
    
    confirmation_msg = hikari.Embed(title=f"{cc.correct_emoji} Sucesfully posted new feature for **{opt_plugin}-{pl_version}**", description=f"""
**Title:** ```{opt_title}```
**Description:** ```{opt_information}```

>>> {cc.channel_emoji} <#{message_channel_id}>
{cc.link_emoji} [Go To Message]({message_link})
""")
    
    await ctx.respond(confirmation_msg, flags=hikari.MessageFlag.EPHEMERAL)

    ########################################################################
    
    logs.out(f'"plugin update" command executed by (@{ctx.author.username}) at (#{ctx.get_channel()})', 'debug')

"""
########################################################################
# POST AIM-ROUTINE

@post_command_group.child
@lightbulb.add_checks(lightbulb.has_roles(admin_role))
@lightbulb.option("title",  "tittle of the aim-routine post", type=str)
@lightbulb.option("description",  "description of the aim-routine post", type=str)
@lightbulb.option("program",  "program to do the aim-routine", type=str, choices=aim_programs)
@lightbulb.option("url",  "url of the aim-routine", type=str)
@lightbulb.command('aimrutine', 'command to add aim-routine to aim-routines channel.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def presence_command_group(ctx):
    option_title = ctx.options.title
    option_information = ctx.options.description
    option_url = ctx.options.url
    option_Program = ctx.options.program

    command_executor = ctx.author
    command_executor_id = command_executor.id


    component = ctx.bot.rest.build_action_row().add_select_menu(
        "testing").set_max_values(len(agents))

    for agent in agents:
        component = component.add_option(str(agent), f"testing{agent}").add_to_menu()

    component = component.add_to_container()


    def check(event: hikari.InteractionCreateEvent):
       # conditions to check if the interaction was on the component you wanted
        event = ctx.bot.rest.wait_for(hikari.InteractionCreateEvent, predicate=check)


    await ctx.respond(f">>> **choose agent/s**", component=component,
                      flags=hikari.MessageFlag.EPHEMERAL)
""
    embed1 = hikari.Embed(title=f":blue_book: {option_title}",
                          description=f"{option_information}\n\n**Program: **```{option_Program}```\n**Sender: **<@{command_executor_id}>\n\n{link_emoji} [Go To Website]({option_url})",
                          url=f"{option_url}",
                          color="008cff").set_thumbnail(generate_qr(option_url, "discord_addstrat_thumbnail"))

    try:
        message = await ctx.bot.rest.create_message(aim_routine_channel, embed1)

    except:
        await ctx.respond(send_error,
                          flags=hikari.MessageFlag.EPHEMERAL)

    message_id = message.id
    message_channel_id = message.channel_id
    message_link = f"https://discord.com/channels/953062983687372830/{message_channel_id}/{message_id}"

    embed2 = hikari.Embed(title=f":white_check_mark: Sucesfully posted new micro",
                          description=f"**Title:** ```{option_title}```\n**Description:** ```{option_information}```\n**Posted:** <#{message_channel_id}>\n**Message**: [click here]({message_link})",
                          color="88ff00",
                          url=message_link)
""
    await ctx.respond(embed2,
                      flags=hikari.MessageFlag.EPHEMERAL)

########################################################################
# POST INFO
@post_command_group.child
@lightbulb.add_checks(lightbulb.has_roles(admin_role))
@lightbulb.option("url",  "url of what do you want to sare")
@lightbulb.option("description",  "url of what do you want to sare")
@lightbulb.option("title",  "url of what do you want to sare")
@lightbulb.option("footer",  "url of what do you want to sare", required=False, default="", type=str)
@lightbulb.option("channel", "Select channel", hikari.TextableGuildChannel, required=False, channel_types=[hikari.ChannelType.GUILD_TEXT], default=None)
@lightbulb.command('info', 'send info.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def presence_command_group(ctx):
    link = ctx.options.url
    short_link = short_url(ctx.options.url)
    description = ctx.options.description
    title = ctx.options.title
    footer = ctx.options.footer
    channel = ctx.options.channel

    if channel == None:
        channel = ctx.channel_id

    embed1 = hikari.Embed(title=f"{title}",
                          description=f"*>>> {description}*\n{link_emoji} {short_link}",
                          color=embed_color,
                          url=f"{link}").set_thumbnail(generate_qr(link, "discord_postinfo_thumbnail"))

    embed1.set_footer(f"AdderX Division - {footer}")

    message = await ctx.bot.rest.create_message(channel, embed1)
    message_id = message.id
    message_channel_id = message.channel_id
    message_link = f"https://discord.com/channels/953062983687372830/{message_channel_id}/{message_id}"

    embed2 = hikari.Embed(title=f"{correct_emoji} Sucesfully posted",
                          color="88ff00",
                          url=message_link)

    embed2.add_field("Post Title", f">>> {title}")
    embed2.add_field("Post Description", f">>> {description}")
    embed2.add_field("Message", f"{channel_emoji} <#{message_channel_id}>\n{link_emoji} [Go To Message]({message_link})")


    await ctx.respond(embed2,
                      flags=hikari.MessageFlag.EPHEMERAL)

########################################################################

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)

##################################################################
"""
def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)
    