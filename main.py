import discord
import os
import random

ELON_RESPONSES = [
	"Interesting",
	"Concerning",
	"True",
	"Looking into this",
	"Absolutely",
	"Cool",
	"Wow",
	"Very concerning",
	"Exactly",
	"Yes",
	"Yup",
	"!",
	"🎯",
	"🤣🤣🤣",
	"🤣🤣",
	"🤣",
	"😂",
	"💯",
	"🔥",
	"👀",
	"🤔",
]

BOT_ALLOWLIST = [
	1000157420024254464,  # deanifier
	862143718421037066,  # wikidumb
]

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f'We have logged in as {client.user} ({len(client.guilds)} guilds)')

@client.event
async def on_message(message: discord.Message):
	if message.author.bot and message.author.id not in BOT_ALLOWLIST:
		return
	
	if random.randint(0, 99) > 0 and not os.getenv("ELON_FORCE"):  # 1/100
		return
	
	await message.reply(random.choice(ELON_RESPONSES))

token = os.getenv("ELON_TOKEN")

if not token:
	raise Exception("no token")

client.run(token)
