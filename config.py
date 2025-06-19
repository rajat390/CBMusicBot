import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQFxjfcAS8kiRAu9moRHy83V7iB5rhlUFwJhsI8UqpETC270mpv7N6KzLcyMXBRWT7poPHjrBIBRG3GR0ex4K2Uqys9x-ojEaOqcFJyHI9BHShT5Nv1IS5UJEp0PzJi_Q_5XS4IkKbE-vKyYsCrYgcfi5tWnytoijX8CIUEfmGNT5MeBtnWXsg5bN4xw-QKRfIk51PxCgpzb1Ew-mlGyGgAHUpmi2aErRn9_Ig4_a4sdOuygC2C0gFR7woeiqdDA7zkJ03Jm4jW4KjrqQOiVzd0L298pZZVQsWI59WJcfUkHqWw4wyDZAOGO1jqkdqK28Jx6x09NQzHYHXQUXJoAC8N12BM6cwAAAAE3MHqgAA")
BOT_TOKEN = getenv("7729314076:AAHgtHs-5hhEWBR8Es3IyFQkIfs_VQ3VxoM")
BOT_NAME = getenv("BOT_NAME", "BILLY MUSIC BOT")
BG_IMAGE = getenv("BG_IMAGE", "https://graph.org/file/c34fc9d62d93032868f02-ffd4f1f6e48434a23a.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://graph.org/file/c34fc9d62d93032868f02-ffd4f1f6e48434a23a.jpg")
AUD_IMG = getenv("AUD_IMG", "https://graph.org/file/c34fc9d62d93032868f02-ffd4f1f6e48434a23a.jpg")
QUE_IMG = getenv("QUE_IMG", "https://graph.org/file/c34fc9d62d93032868f02-ffd4f1f6e48434a23a.jpg")
API_ID = int(getenv("24219127"))
API_HASH = getenv("4ede46a38016f3574a35ab60055ce51a")
BOT_USERNAME = getenv("BOT_USERNAME", "music_tit_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Everything_is_okh")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CyberSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "CyberMusicProject")
OWNER_NAME = getenv("OWNER_NAME", "𝙅 𝙊 𝙃 𝙉 > 𝙒 𝙄 𝘾 𝙆") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("7390298763")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("mongodb+srv://rahucreate:rahucreate@cluster0.ohj4boi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("-1002821231421")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
