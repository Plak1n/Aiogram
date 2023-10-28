from environs import Env 
from dataclasses import dataclass

@dataclass
class Bots:
    bot_token: str
    bot_owner_id: int
    
    
@dataclass
class Settings:
    bots: Bots
    
def get_settings(path: str):
    '''Get setting from the file in path'''
    env = Env()
    env.read_env(path)
    
    return Settings(
        bots=Bots(
            bot_token = env.str("BOT_TOKEN"),
            bot_owner_id = env.int("BOT_OWNER_ID")
        )
    )

settings = get_settings("config.txt")