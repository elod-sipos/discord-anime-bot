import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pyautogui

BOT_TOKEN = ""
CHANNEL_ID = 

bot = commands.Bot(command_prefix = "{", intents = discord.Intents.all())





@bot.event
async def on_ready():
    print("hewwo :3")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("```info```")

# Code by MaxJ02 #
@bot.command()
async def anime(ctx):
    driver = webdriver.Chrome()
    driver.get("https://myanimelist.net/topanime.php?type=bypopularity")
    driver.set_window_size(2560, 1080)
    time.sleep(3)
    pyautogui.moveTo(400,400, duration = 1)
    pyautogui.typewrite(["enter"])
    time.sleep(3)
    driver.save_screenshot("screenshot.png")
    await ctx.send(file = discord.File("screenshot.png"))
# #

@bot.command()
async def anime1(ctx):
    driver = webdriver.Chrome()
    driver.get("https://myanimelist.net/topanime.php?type=bypopularity")
    wait = WebDriverWait(driver, 10)
    name = driver.find_element(By.CSS_SELECTOR, 'h3.hoverinfo_trigger a')
    await ctx.send(name.text)

 

bot.run(BOT_TOKEN)
