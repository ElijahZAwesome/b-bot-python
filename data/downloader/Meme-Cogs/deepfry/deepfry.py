import discord
from discord.ext import commands
import os
import asyncio
from cogs.utils.dataIO import dataIO
import PIL
from PIL import Image
import glob, os
from PIL import ImageEnhance
from PIL import ImageColor
from PIL import ImageFilter
import requests
from io import BytesIO

WINDOWS_OS = os.name == 'nt'

class DeepFry:
    """Deep fries images"""

    def __init__(self, bot):
        self.bot = bot
        if not os.path.exists("data/deepfry"):
            os.makedirs("data/deepfry")
        self.path = os.path.join("data", "deepfry")

        
    @commands.command(pass_context=True)
    async def deepfry(self, ctx, user=None):
        """Will deep fry any image link given. (Adds absurd saturation, etc)"""
        
        url = None
        if user is None:
            user = ctx.message.author
        elif len(ctx.message.mentions):
            user = ctx.message.mentions[0]
        else:
            url = user
        if type(user) == discord.User or type(user) == discord.Member:
            if user.avatar:
                avatar = 'https://discordapp.com/api/users/' + user.id + '/avatars/' + user.avatar + '.jpg'
                response = requests.get(avatar)
                image = Image.open (BytesIO(response.content))
            else:
                avatar = user.default_avatar_url
                response = requests.get(avatar)
                image = Image.open (BytesIO(response.content))
        else:
            response = requests.get(url)
            image = Image.open (BytesIO(response.content))

        id = ctx.message.author.id
        channel = ctx.message.channel
        

        contrast = ImageEnhance.Contrast( image )
        brightness = ImageEnhance.Brightness( image )
        sharpness = ImageEnhance.Sharpness( image )
        saturation = ImageEnhance.Color( image )
        image = sharpness.enhance(5.0)
        image = brightness.enhance( 1.5 )
        image = contrast.enhance( 5.0 )
        image = saturation.enhance( 7.0 )
        image = image.filter(ImageFilter.GaussianBlur(1))
        image = image.convert("RGB")
        image.save(self.path + "/" + id + ".jpg", quality=8)
        await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
        os.remove(self.path + "/" + id + ".jpg")
        
    @commands.command(pass_context=True)
    async def customfry(self, ctx, user, contrast, saturation, sharpness, brightness, blur):
        """Will deep fry any image link given. with custom filters"""
        
        url = None
        if user is None:
            user = ctx.message.author
        elif len(ctx.message.mentions):
            user = ctx.message.mentions[0]
        else:
            url = user
        if type(user) == discord.User or type(user) == discord.Member:
            if user.avatar:
                avatar = 'https://discordapp.com/api/users/' + user.id + '/avatars/' + user.avatar + '.jpg'
                response = requests.get(avatar)
                image = Image.open (BytesIO(response.content))
            else:
                avatar = user.default_avatar_url
                response = requests.get(avatar)
                image = Image.open (BytesIO(response.content))
        else:
            response = requests.get(url)
            image = Image.open (BytesIO(response.content))

        id = ctx.message.author.id
        channel = ctx.message.channel
        

        contrastenhance = ImageEnhance.Contrast( image )
        brightnessenhance = ImageEnhance.Brightness( image )
        sharpnessenhance = ImageEnhance.Sharpness( image )
        saturationenhance = ImageEnhance.Color( image )
        if "." not in contrast:
            contrast = contrast + ".0"
        if "." not in saturation:
            saturation = saturation + ".0"
        if "." not in sharpness:
            sharpness = sharpness + ".0"
        if "." not in brightness:
            brightness = brightness + ".0"
        image = sharpnessenhance.enhance(float(sharpness))
        image = brightnessenhance.enhance( float(brightness) )
        image = contrastenhance.enhance( float(contrast) )
        image = saturationenhance.enhance( float(saturation) )
        image = image.filter(ImageFilter.GaussianBlur(int(blur)))
        image = image.convert("RGB")
        image.save(self.path + "/" + id + ".jpg", quality=8)
        await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
        os.remove(self.path + "/" + id + ".jpg")
        
    @commands.command(pass_context=True)
    async def destroy(self, ctx, user=None):
        """Will deep fry any image link given, but to such an extreme degree that its no longer recognizable"""
        
        url = None
        if user is None:
            user = ctx.message.author
        elif len(ctx.message.mentions):
            user = ctx.message.mentions[0]
        else:
            url = user
        if type(user) == discord.User or type(user) == discord.Member:
            if user.avatar:
                avatar = 'https://discordapp.com/api/users/' + user.id + '/avatars/' + user.avatar + '.jpg'
                response = requests.get(avatar)
                image = Image.open (BytesIO(response.content))
            else:
                avatar = user.default_avatar_url
                response = requests.get(avatar)
                image = Image.open (BytesIO(response.content))
        else:
            response = requests.get(url)
            image = Image.open (BytesIO(response.content))
    
        id = ctx.message.author.id
        channel = ctx.message.channel
            
        contrast = ImageEnhance.Contrast( image )
        brightness = ImageEnhance.Brightness( image )
        sharpness = ImageEnhance.Sharpness( image )
        saturation = ImageEnhance.Color( image )
        image = sharpness.enhance(5.0)
        image = brightness.enhance( 1.5 )
        image = contrast.enhance( 5.0 )
        image = saturation.enhance( 7.0 )
        image = image.filter(ImageFilter.GaussianBlur(1))
        image = image.convert("RGB")
        image.save(self.path + "/" + id + ".jpg", quality=1)
        image = Image.open (self.path + "/" + id + ".jpg")
            
        contrast = ImageEnhance.Contrast( image )
        brightness = ImageEnhance.Brightness( image )
        sharpness = ImageEnhance.Sharpness( image )
        saturation = ImageEnhance.Color( image )
        image = sharpness.enhance(5.0)
        image = brightness.enhance( 1.5 )
        image = contrast.enhance( 5.0 )
        image = saturation.enhance( 7.0 )
        image = image.filter(ImageFilter.GaussianBlur(2))
        image = image.convert("RGB")
        image.save(self.path + "/" + id + ".jpg", quality=1)
        image = Image.open (self.path + "/" + id + ".jpg")
            
        contrast = ImageEnhance.Contrast( image )
        brightness = ImageEnhance.Brightness( image )
        sharpness = ImageEnhance.Sharpness( image )
        saturation = ImageEnhance.Color( image )
        image = sharpness.enhance(5.0)
        image = brightness.enhance( 1.5 )
        image = contrast.enhance( 5.0 )
        image = saturation.enhance( 7.0 )
        image = image.filter(ImageFilter.GaussianBlur(1))
        image = image.convert("RGB")
        image.save(self.path + "/" + id + ".jpg", quality=1)
        image = Image.open (self.path + "/" + id + ".jpg")
            
        contrast = ImageEnhance.Contrast( image )
        brightness = ImageEnhance.Brightness( image )
        sharpness = ImageEnhance.Sharpness( image )
        saturation = ImageEnhance.Color( image )
        image = sharpness.enhance(5.0)
        image = brightness.enhance( 1.5 )
        image = contrast.enhance( 5.0 )
        image = saturation.enhance( 7.0 )
        image = image.filter(ImageFilter.GaussianBlur(1))
        image = image.convert("RGB")
        image.save(self.path + "/" + id + ".jpg", quality=1)
        await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
        os.remove(self.path + "/" + id + ".jpg")

def setup(bot):
    bot.add_cog(DeepFry(bot))
