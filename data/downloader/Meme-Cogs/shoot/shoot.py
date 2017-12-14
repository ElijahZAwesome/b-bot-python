import discord
from discord.ext import commands
import random

class Shoot:
    """Allows you to shoot a user"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def shoot(self, ctx, user : discord.Member = None, everyone = None):
        """Will shoot the user specified, (be careful with that gun!)"""
        
        #Your code will go here
        if ctx.message.author.id != user.id:
            await self.bot.say(ctx.message.author.mention + " gunned down " + user.mention + " !")
        if ctx.message.author.id == user.id:
            if everyone == 'everyone':
                ##if school == 'school':
                ##    await self.bot.say(ctx.message.author.mention + " shot up the local school, killing hundreds.")
                ##else if school == 'server':
                ##    await self.bot.say(ctx.message.author.mention + " shot up the server.")
                ##else:
                await self.bot.say(ctx.message.author.mention + " shot up the server!")
            else:
                await self.bot.say(ctx.message.author.mention + " couldn't take it and shot themselves.")
                
    @commands.command(pass_context=True)
    async def dab(self, ctx, user : discord.Member=None):
        """Will create a scenario where the user is dabbed on"""
        
        #Your code will go here
        otherscenarios = [' was ambushed by dab ninjas and dabbed to death.', ' attempted to dab on someone, but dabbed on themselves instead.', ' got dabbed on real hard by a bully.', ' was dabbed on in their nightmares!', ' insulted a fandom so was inevitabally dabbed on.', ' was jump-dabbed on by Noah!', ' got dabbed on by Bill Gates.', ' fell down a flight of stairs due to a stern dabbing-on.', ' meme-d too hard and dabbed out of existence.', ' commited a meme-crime and was dabbed on by the dab-police.', ' dabbed at a mirror.', ' does the d se dab.', ' friccin dabs. Aw hecc', ' was hypnotized into dabbing']
        selfscenarios = ["'s dab backfired and hit themselves!", ' was called fat by two people online, so they dabbed on themselves.', ' dabbed off a bridge', ' summoned a dab-man to dab on themselves', ' was dabbed on in their sleep by Freddy Dabber!', ' took instant ~~suicide~~ dab pills.', ' was too meme-ish and died of dab-o-nitus.', ' did the wrong dab, fool']
        if user == None:
            await self.bot.say(ctx.message.author.mention + random.choice(selfscenarios))
        elif ctx.message.author.id != user.id:
            await self.bot.say(user.mention + random.choice(otherscenarios))
        elif ctx.message.author.id == user.id:
            await self.bot.say(ctx.message.author.mention + random.choice(selfscenarios))

def setup(bot):
    bot.add_cog(Shoot(bot))
