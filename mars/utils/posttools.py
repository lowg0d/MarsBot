import hikari
import datetime
import mars.utils.cc as cc

def embed(tittle_, description_, url_, footer_, img_, thumbnail_, video_):
    
    
    embed = hikari.Embed(title=tittle_,
                          description=description_,
                          url=url_,
                          color=cc.main_color)
    embed.set_footer(footer_)
    
    if img_ != None: 
        embed.set_image(img_)
    
    if thumbnail_ != None: 
        embed.set_thumbnail(thumbnail_)
    
    return embed

def bug_fix_post(tittle_, description_, url_, img_, thumbnail_, plugin_, version_):
    
    embed = hikari.Embed(title=f"[{cc.bug_two_emoji}] {tittle_}",
                          description=description_,
                          url=url_,
                          color=cc.bug_fix_color,
                          timestamp=datetime.datetime.now(tz=datetime.timezone.utc))
    
    embed.set_footer(f"plugin bug fix ({str(plugin_)} {str(version_)})")
    
    if img_ != None: 
        embed.set_image(img_)
    
    if thumbnail_ != None: 
        embed.set_thumbnail(thumbnail_)
    
    return embed

def new_feature_post(tittle_, description_, url_, img_, thumbnail_, plugin_, version_):
    
    embed = hikari.Embed(title=f"[{cc.star_emoji}] {tittle_}",
                          description=description_,
                          url=url_,
                          color=cc.new_feature_color,
                          timestamp=datetime.datetime.now(tz=datetime.timezone.utc))
    
    embed.set_footer(f"plugin new feature ({str(plugin_)} {str(version_)})")
    
    if img_ != None: 
        embed.set_image(img_)
    
    if thumbnail_ != None: 
        embed.set_thumbnail(thumbnail_)
    
    return embed

def update_post(tittle_, description_, url_, img_, thumbnail_, plugin_, version_):
    
    embed = hikari.Embed(title=f"[{cc.update_emoji}] {tittle_}",
                          description=description_,
                          url=url_,
                          color=cc.update_color,
                          timestamp=datetime.datetime.now(tz=datetime.timezone.utc))
    
    embed.set_footer(f"plugin update ({str(plugin_)} {str(version_)})")
    
    if img_ != None: 
        embed.set_image(img_)
    
    if thumbnail_ != None: 
        embed.set_thumbnail(thumbnail_)
    
    return embed


def about_post(tittle_, description_, url_, img_, thumbnail_, plugin_, version_, features_title, commands_title,
               features_, commands_, plugin_emoji_, plugin_emoji_id):
    
    brand_emoji = cc.emoji(plugin_emoji_, plugin_emoji_id)
    
    embed = hikari.Embed(title=f"{brand_emoji} {tittle_}",
                          description=f"{description_}\n",
                          url=url_,
                          color=cc.main_color,
                          timestamp=datetime.datetime.now(tz=datetime.timezone.utc))
    
    embed.set_footer(f"plugin information - ({str(plugin_)} {str(version_)})")
    
    embed.add_field(name=f"{features_title}", value=f"```{features_}```", inline=True)
    embed.add_field(name=f"{commands_title}", value=f"```{commands_}```", inline=True)
    
    
    if img_ != None: 
        embed.set_image(img_)
    
    if thumbnail_ != None: 
        embed.set_thumbnail(thumbnail_)
    
    return embed