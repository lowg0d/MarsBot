import os
from mars.main import Bot
from mars import __version__

if __name__ == '__main__':
    os.system('cls')
    
    botapp = Bot()
    botapp.start()