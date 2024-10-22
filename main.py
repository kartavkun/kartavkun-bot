from twitchio.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

tg = "https://t.me/kartaviykun"
spotify = "https://spoti.fi/3QHPOua"
twitter = "https://twitter.com"

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix='!', initial_channels=['kartav__'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')



    @commands.command()
    async def tg(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name} - {tg}')

    @commands.command()
    async def spotify(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name} Ссылка на мой профиль с плейлистами - {spotify}')

    @commands.command()
    async def twitter(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name} - {twitter}')



bot = Bot()
bot.run()
