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
    await channel.send("``` i am a bot that uses https://myanimelist.net :3\n cuwwent commwands: \n anime_top (number)\n anime_popular```")
    
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
async def anime_top(ctx, num: int):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(options = options)
    driver.get("https://myanimelist.net/topanime.php")
    top_names = ""
    count = 1
    num = int(num)
    top_name_elements = driver.find_elements(By.CSS_SELECTOR, "h3.hoverinfo_trigger a")
    for top_name_element in top_name_elements:
        if count > num:
            break
        elif num > 50:
            await ctx.send("cannot go above 50 :3")
            break
        top_names += str(count) + " " + top_name_element.text + "\n"
        count += 1
    await ctx.send("```Here is the list of the highest rated anime\n```" + "```" + top_names + "```")

@bot.command()
async def anime_popular(ctx):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(options = options)
    driver.get("https://myanimelist.net/topanime.php?type=airing")
    pop_output = ""
    pop_rank = ""
    count = 0
    pop_name_elements = driver.find_elements(By.CSS_SELECTOR, "h3.hoverinfo_trigger a")
    pop_rank_elements = driver.find_elements(By.CSS_SELECTOR, "td.score.ac.fs14 span.text.on.score-label")
    for pop_rank_element in pop_rank_elements:
        if count >15:
            break
        pop_rank += pop_rank_element.text + "\n"
        count += 1

    count = 0
    for pop_name_element, pop_rank_element in zip(pop_name_elements, pop_rank_elements):
        if count > 15:
            break
        pop_output += f"{pop_rank_element.text} {pop_name_element.text}\n"
        count += 1
    await ctx.send("```Here is a list of what is currently most popular :3\n```" + "```" + pop_output + "```")

bot.run(BOT_TOKEN)
