import os

from dotenv import load_dotenv

load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


API_ID = int(os.environ.get("API_ID", "27639102"))
API_HASH = os.environ.get("API_HASH", "35142c1407be6264e68fb6bec5dcabd9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5625295308:AAFXY-GLROUI0HVY2fHouqwHkKZRrc0xIkE")
ADMINS = ([int(i.strip()) for i in os.environ.get("ADMINS").split(",")]if os.environ.get("ADMINS")else [])

DATABASE_NAME = os.environ.get("DATABASE_NAME", "MdiskConvertor")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Fileshare123:Fileshare123@cluster0.nqjle5f.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = int(os.environ.get("OWNER_ID", "5606411877"))  # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []


LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001834678099"))
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL")  # For Force Subscription
BROADCAST_AS_COPY = is_enabled((os.environ.get("BROADCAST_AS_COPY", "True")), True)
IS_PRIVATE = is_enabled(os.environ.get("IS_PRIVATE", "False"), "False")
SOURCE_CODE = os.environ.get("SOURCE_CODE", "https://github.com/kevinnadar22/URL-Shortener-V2")
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", "")
LINK_BYPASS = is_enabled((os.environ.get("LINK_BYPASS", "False")), False)
BASE_SITE = os.environ.get("BASE_SITE", "mdisklink.in")  # your shortener site domain


CHANNELS = is_enabled((os.environ.get("CHANNELS", "False")), True)
CHANNEL_ID = ([int(i.strip()) for i in os.environ.get("CHANNEL_ID").split(" ")]if os.environ.get("CHANNEL_ID")else [])

DE_BYPASS = ([i.strip() for i in os.environ.get("DE_BYPASS").split(",")]if os.environ.get("DE_BYPASS")else [])
DE_BYPASS.append("mdisk.me")

FORWARD_MESSAGE = is_enabled((os.environ.get("FORWARD_MESSAGE", "False")), False)  # true if forwardd message to converted by reposting the post


HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU = bool(HEROKU_API_KEY and HEROKU_APP_NAME)

REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", None)
REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", None)
REPLIT = (f"https://{REPLIT_APP_NAME.lower()}.{REPLIT_USERNAME}.repl.co"if REPLIT_APP_NAME and REPLIT_USERNAME else False)


KOYEB_USERNAME = os.environ.get("KOYEB_USERNAME", None)
KOYEB_APP_NAME = os.environ.get("KOYEB_APP_NAME", None)
KOYEB = (f"https://{KOYEB_APP_NAME}-{KOYEB_USERNAME}.koyeb.app/"if KOYEB_APP_NAME and KOYEB_USERNAME else False)

PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))

LOG_STR = "\nHeroku is {0}\n".format("Enabled" if HEROKU else "Disabled") + "Users {0} use this bot\n".format("cannot" if IS_PRIVATE else "can")
