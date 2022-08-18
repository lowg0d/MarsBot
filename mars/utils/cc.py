import hikari
import mars.config.inter as inter
import mars.managers.config_mg as config

##################################################################

#colors
main_color = config.get("color")
logo_url = config.get("logo_url")
wrong_color = inter.get_inter("wrong_color")
correct_color = inter.get_inter("correct_color")
about_color = inter.get_inter("about_color")
new_feature_color = inter.get_inter("new_feature_color")
update_color = inter.get_inter("update_color")
bug_fix_color = inter.get_inter("bug_fix_color")
server_id = config.get("server_id")

#socials
ip = config.get_two("socials","s_ip")
store = config.get_two("socials","s_store")
github = config.get_two("socials","s_github")
twitter = config.get_two("socials","s_twitter")

#roles
owner_role = config.get_two("roles","owner_role")
admin_role = config.get_two("roles","admin_role")
developer_role = config.get_two("roles","developer_role")

#channels
rules_channel = config.get_two("channels","rules_channel")
spoiler_channel = config.get_two("channels","spoiler_channel")
announcements_channel = config.get_two("channels","announcements_channel")

##################################################################

def emoji(name, iD):
    memoji = hikari.CustomEmoji(
            id=iD, name=name, is_animated=False)
    
    return memoji

##################################################################

pin_emoji = emoji("icons_pin", 996012073710538893) 
bug_emoji = emoji("icons_dgreen", 1002051631170461767)
link_emoji = emoji("icons_link", 1002053462248402965)
star_emoji = emoji("icons_shine1", 1002139038754545704) 
wrong_emoji = emoji("icons_wrong", 1002745153531953182) 
update_emoji = emoji("icons_update", 1002744582003490860) 
bug_two_emoji = emoji("icons_Bugs", 1002051031057846283) 
bug_emoji = emoji("icons_colorstaff", 996012064558567505) 
channel_emoji = emoji("icons_text", 996012059638644767)
correct_emoji = emoji("icons_Correct", 1002745115128889394)
verified_emoji = emoji("icons_colorserververified", 996012062826299424) 
settings_emoji = emoji("icons_settings", 1002052195329519706) 

##################################################################

error_msg = hikari.Embed(title=f"{wrong_emoji}  An error ocurred posting that.",
                          color=wrong_color)

##################################################################