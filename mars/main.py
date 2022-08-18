import os
import time
import hikari
import fnmatch
import lightbulb
import mars.managers.config_mg as config
import mars.managers.logging_mg as logs

##################################################################

token = config.get("token")
server_id = config.get("server_id")
extension_path = "./mars/extensions"

##################################################################

class Bot:
    def __init__(self):

        self.token = token
        self.bot = lightbulb.BotApp(
            token=self.token,
            default_enabled_guilds=(server_id),
            intents=hikari.Intents.ALL_UNPRIVILEGED)
    
    def start(self):
        
        logs.out("loading extensions", "debug")
        for f in os.listdir(extension_path):
            if fnmatch.fnmatch(f, '*.py'):
                time.sleep(0.2)
                extension = f.replace('.py', '')
                self.bot.load_extensions(f"mars.extensions.{extension}")
        self.run()
                
    def run(self):
        logs.out("starting the bot", "debug")
        self.bot.run()
        logs.out("bot stopped", "debug")
