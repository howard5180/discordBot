import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import random
import myUtilities
import secrets
import meme_command
import funfact
from datetime import datetime

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_member_join(member):
    welcome_msg_start = ["<:dphello:365891704013979648> **<@{0}>**! Welcome to Dragon Project Community Server. Here's something you can do:",
                         "As **<@{0}>** walks in the deep forest, an old gateway appeared with a wooden sign in front of it saying:\n\nWelcome to Dragon Project Community Server:",
                         "Ding Dong! Pizzaman **<@{0}>** arrived the door of Dragon Project Community Server and saw a sign:\n\nHey there!",
                         "Woosh! **<@{0}>** got transported through the portal immediately when opening the letter that says:\n\nWelcome!"]
    welcome_msg_core = ("\n1. Spend some time to read <#470713924325474304>;"
                        "\n2. Register a class in <#470713716573208576>;"
                        "\n3. If you are new to the game, definitely check out <#470713961768026152>"
                        "\n4. Quick browse on <#470713900690833412> and <#470713934517764117> to get hold of new stuffs"
                        "\n5. Say a hi in <#470713608838578176>"
                        "\nIf you have any questions, you may ask the `@Moderators` through PMs.")
    welcome_msg_end = ["\nEnjoy your stay ~~and hope you pull As and Bs in gacha~~ <a:WHALEHARD:462505685800845312>",
                       "\n\nThe gateway suddenly opens....",
                       "\n\nSo......Where is my pizza? :pizza:",
                       "\n\n...and got teleported into the server"]
    serverchannel = member.guild.get_channel(525710866860081185)
    msg_rand = random.randint(0,3)
    msg = (welcome_msg_start[msg_rand]+welcome_msg_core+welcome_msg_end[msg_rand]).format(member.id)
    try:
        await serverchannel.send(msg)
    except Exception:
        pass

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#miscellaneous commands

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def atest(ctx, *a):
    await ctx.send(a)

bot.remove_command('help') #to overwrite discord.py's help

@bot.command()
async def help(ctx):
    #help message
    emb = (discord.Embed(title="Karyu Help", description="Need some help on what commands I have? Read the following:", colour=0xFFFFFF))
    emb.set_thumbnail(url = "https://cdn.discordapp.com/attachments/349266633476538368/469151696048750593/stmp_10000018.png")
    emb.add_field(name = "Database command:", value = "`.db`", inline=False)
    emb.add_field(name = "Behemoth general information:", value = "`.behe <behemoth name>` or `.behe <element type weapon>`", inline=True)
    emb.add_field(name = "Magi information", value = "`.magi <magi name>`", inline=True)
    emb.add_field(name = "Weapon information:", value = "`.wep <behemoth name>`", inline=True)
    emb.add_field(name = "Armor information:", value = "`.armor <behemoth name>`", inline=True)
    emb.add_field(name = "Class command:", value = "`.addclass <class>` and `.removeclass <class>`\nAvailable class: `sns` `gs` `spear` `db` `bow`", inline=False)
    emb.add_field(name = "Role command:", value = "`.addrole <role>` and `.removerole <role>`\nAvailable roles: `tower`, `br`, `expo`, `carry`",inline=False)
    emb.add_field(name = "Behemoth Summon simulation:", value = "`.behesim single` or `.behesim multi <step number>` \nP.S. Step is default as 1 if not specified", inline=False)
    emb.add_field(name = "Magi Summon simulation:", value = "`.magisim <single/multi>`", inline=False)
    emb.add_field(name = "List of meme command:", value = "`.memelist`", inline=True)
    emb.add_field(name = "Random Dragon Project fun fact:", value = "`.funfact`", inline=True)
    emb.add_field(name = "JP event schedule (made by Algor):", value = "`.scheduledb`", inline=True)
    emb.add_field(name = "Shishui's blog:", value = "`.blog`", inline=True)
    emb.add_field(name = "Server invite link:", value = "`.invite`", inline=True)
    emb.add_field(name = "Redemption link:", value = "`.redeem`", inline=True)
    emb.add_field(name = "Support ticket:", value = "`.support`", inline=True)
    await ctx.send(embed=emb)

@bot.command()
async def db(ctx):
    front_msg = ["That effort to summon the Bible is looking bad, but since I'm generous so here you go:\n",
                 "Here is the link to the database:\n",
                 "Thanks for using the express service! Here's the Bible you ordered:\n",
                 "Moshi moshi, database desu:\n",
                 "Suddenly a wind blew up, and a Bible link lands in front of you:\n"]
    random_msg_num = random.randint(0,4)
    msg = front_msg[random_msg_num]+"https://docs.google.com/spreadsheets/d/1iMoiSjTbahFxfOyU4F4_xOWtS3Va22_J1tyizyDltNU/edit?usp=sharing"
    await ctx.send(msg)

@bot.command()
async def invite(ctx):
    msg = ("Here's the invite link to the server:\n"
            "https://discord.gg/HQM6YVX"
            "\nIf link isn't working, tell the moderators through DM and we'll solve it ASAP <a:WHALEHARD:462505685800845312>")
    await ctx.send(msg)

@bot.command()
async def ratingdb(ctx):
    msg = ("Ratings for magi and gears done by Karyu:"
           "\nhttps://docs.google.com/spreadsheets/d/1tbtBT7ty_KDU8phvCzETXnFvFh_YWMp4yKgsjDE8c20/edit?usp=sharing")
    await ctx.send(msg)

@bot.command()
async def redeem(ctx):
    msg = ("Here is the redeem website:"
           "\nhttps://dp.gogame.net/redemption/"
           "\nMake sure to check the codes in <#470713900690833412> too.")
    await ctx.send(msg)

@bot.command()
async def support(ctx):
    msg = ("Planning to fire a lot of tickets to gogame? Here you go:"
           "\nhttps://support.gogame.net/hc/en-us/requests/new?ticket_form_id=114093964114")
    await ctx.send(msg)

fact = funfact.get_ff()
@bot.command()
async def funfact(ctx):
    num = random.randrange(0,len(fact))
    ff_emb = discord.Embed(description=fact[num],colour=0xFFFFFF)
    ff_emb.set_author(name="Did you know?", icon_url="https://cdn.discordapp.com/attachments/470713810232147988/512477914755760157/Igneel.png")
    ff_emb.set_thumbnail(url="https://images-ext-1.discordapp.net/external/lhqaE-HJIhURlR7v9LsjxZsyOhsemu4FjxV-pmwnUWg/https/cdn.discordapp.com/attachments/349266633476538368/469151696048750593/stmp_10000018.png")
    await ctx.send(embed = ff_emb)

@bot.command()
async def scheduledb(ctx):
    msg = ("Following database is the schedule of events that occured in JP according to behemoth banner release (credits to Algor)"
           "\nPlease note that just take these as reference, don't assume it must appear at the same period in future"
           "\nhttps://docs.google.com/spreadsheets/d/10QlMCTN3Rgm-ptDJDCTvPn7lhW93adJMHc_jRfAu4Wc/edit#gid=0")
    await ctx.send(msg)

@bot.command()
async def blog(ctx):
    msg = ("Check out Shishui's blog for events and guides (beginners recommended):"
            "\nhttp://dp-shishui.blogspot.com/")
    await ctx.send(msg)

@bot.command()
async def reroll(ctx):
    currentTime = datetime.utcnow()
    currentHour = currentTime.hour
    currentMinute = currentTime.minute
    weekday = currentTime.weekday()
    if weekday < 2:
        remainDay = 1 - weekday
    else:
        remainDay = 8 - weekday
    remainHour = 23 - currentHour
    remainMinute = 59 - currentMinute
    startMsg = "There are "
    if remainDay == 1:
        dayMsg = str(remainDay) + " day"
    elif remainDay == 0:
        dayMsg = " "
    else:
        dayMsg = str(remainDay) + " days"
    if remainHour == 1:
        hourMsg = str(remainHour) + " hour and "
        dayMsg += ", "
    elif remainHour == 0:
        hourMsg = " "
    else:
        hourMsg = str(remainHour) + " hours and "
        dayMsg += ", "
    if remainMinute == 1:
        minMsg = str(remainMinute) + " minute"
        if remainDay != 0 or remainHour != 0:
            startMsg = "There is "
    elif remainMinute == 0:
        minMsg = "less than a minute"
        if remainDay != 0 or remainHour != 0:
            startMsg = "There is "
    else:
        minMsg = str(remainMinute) + " minutes"
    if weekday == 2:
        msg = startMsg + hourMsg +  minMsg + " until ability half price ends"
    else:
        msg = startMsg + dayMsg + hourMsg + minMsg + " until ability half price starts"
    await ctx.send(msg)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#database search command
@bot.command()
async def behe(ctx, *a):
    if (ctx.channel.name == "behemoth-magi-hub") or (ctx.channel.name == "bot_testing") or (ctx.channel.name == "executive-room") or (ctx.channel.name == "general-testing"):
        i = 0
        joinedInput = " ".join(a)
        filteredInput = myUtilities.filterInput(joinedInput)
        inputWordArray = filteredInput.split()

        attributesArray = myUtilities.matchWeaponAttributes(inputWordArray)
        for key, content in attributesArray.items():
            if (content):
                i+=1

        if (i > 1):
            queryResults = myUtilities.fetchBehemothByTypeDB(attributesArray)
        else:
            queryResults = myUtilities.fetchBehemothDB(filteredInput)

        if (len(queryResults) > 0 and len(queryResults) <= 10):
            embed = myUtilities.behemothEmbedGenerator(queryResults, filteredInput)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Behemoth not found.")
    else:
        await ctx.send("Please use the search function in <#470713661447471104>")


@bot.command()
async def wep(ctx, *a):
    if (ctx.channel.name == "behemoth-magi-hub") or (ctx.channel.name == "bot_testing") or (ctx.channel.name == "executive-room") or (ctx.channel.name == "general-testing"):
        joinedInput = " ".join(a)
        filteredInput = myUtilities.filterInput(joinedInput)
        queryResults = myUtilities.fetchWeaponDB(filteredInput)

        if (len(queryResults) == 1):
            embed = myUtilities.weaponEmbed(queryResults)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Behemoth not found.")
    else:
        await ctx.send("Please use the search function in <#470713661447471104>")

@bot.command()
async def armor(ctx, *a):
    if (ctx.channel.name == "behemoth-magi-hub") or (ctx.channel.name == "bot_testing") or (ctx.channel.name == "executive-room") or (ctx.channel.name == "general-testing"):
        joinedInput = " ".join(a)
        filteredInput = myUtilities.filterInput(joinedInput)
        queryResults = myUtilities.fetchArmorDB(filteredInput)

        if (len(queryResults) == 4):
            embed = myUtilities.armorEmbed(queryResults)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Behemoth not found.")
    else:
        await ctx.send("Please use the search function in <#470713661447471104>")

@bot.command()
async def magi(ctx, *a):
    if (ctx.channel.name == "behemoth-magi-hub") or (ctx.channel.name == "bot_testing") or (ctx.channel.name == "executive-room") or (ctx.channel.name == "general-testing"):
        joined = " ".join(a)
        filteredInput = myUtilities.filterInput(joined)
        queryResults = myUtilities.fetchMagiDB(filteredInput)

        if (len(queryResults) > 0 and len(queryResults) <= 10):
            embed = myUtilities.magiEmbedGenerator(queryResults, filteredInput)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Magi not found.")
    else:
        await ctx.send("Please use the search function in <#470713661447471104>")
    
@armor.error
async def armor_on_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="The correct syntax is:", colour=discord.Colour(0xff0000), description="`?armor [Behemoth's name]`")
        await ctx.send(embed=embed)
    raise error

@wep.error
async def weapon_on_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="The correct syntax is:", colour=discord.Colour(0xff0000), description="`?weapon [Behemoth's name]`")
        await ctx.send(embed=embed)
    raise error

@behe.error
async def behemoth_on_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="The correct syntax is:", colour=discord.Colour(0xff0000), description="`?behemoth [Behemoth's name]`")
        await ctx.send(embed=embed)
    raise error

@magi.error
async def magi_on_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="The correct syntax is:", colour=discord.Colour(0xff0000), description="`?magi [Magi's name]`")
        await ctx.send(embed=embed)
    raise error

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#adding and removing class roles

classes_dict = {"sns":"Sword & Shield","gs":"Great Sword","spear":"Spear","db":"Dual Blades","bow":"Bow"}
classes_dict_key = classes_dict.keys()

class_list = ["Sword & Shield", "Great Sword", "Spear", "Dual Blades", "Bow"]
sns_list = ["sns", "snc", "sword & shield", "sword and shield", "shield"]
gs_list = ["gs", "great sword", "great", "greatsword"]
spear_list = ["spear", "sp"]
db_list = ["db", "dual blades", "dual swords", "dual blade", "dual sword", "dual", "dualblade", "dualblades", "dblades", "dbs"]
bow_list = ["bow"]

#add class
@bot.command()
async def addclass(ctx,*a):
    msgInput = " ".join(a)
    msg = msgInput.lower()
    member = ctx.message.author
    if (ctx.channel.name == "weapon-class") or (ctx.channel.name == "bot_testing"):
        if (msg in sns_list) or (msg in gs_list) or (msg in spear_list) or (msg in db_list) or (msg in bow_list):
            if msg in sns_list:
                class_num = 0
            elif msg in gs_list:
                class_num = 1
            elif msg in spear_list:
                class_num = 2
            elif msg in db_list:
                class_num = 3
            elif msg in bow_list:
                class_num = 4
            roleID = discord.utils.get(ctx.guild.roles, name = class_list[class_num])
            if roleID in member.roles:
                msg = "You already have the " + class_list[class_num] + " class"
                await ctx.send(msg)
            else:
                msg = class_list[class_num] + " class is added"
                await member.add_roles(roleID)
                await ctx.send(msg)
        else:
            await ctx.send("It's an invalid class. For available classes please check `.help`")
    else:
        await ctx.send("You can't use this command here")

#remove class
@bot.command()
async def removeclass(ctx,*a):
    msgInput = " ".join(a)
    msg = msgInput.lower()
    member = ctx.message.author
    if (ctx.channel.name == "weapon-class") or (ctx.channel.name == "bot_testing"):
        if (msg in sns_list) or (msg in gs_list) or (msg in spear_list) or (msg in db_list) or (msg in bow_list):
            if msg in sns_list:
                class_num = 0
            elif msg in gs_list:
                class_num = 1
            elif msg in spear_list:
                class_num = 2
            elif msg in db_list:
                class_num = 3
            elif msg in bow_list:
                class_num = 4
            roleID = discord.utils.get(ctx.guild.roles, name = class_list[class_num])
            if roleID not in member.roles:
                msg = "You don't have the " + class_list[class_num] + " class"
                await ctx.send(msg)
            else:
                msg = class_list[class_num] + " class is removed"
                await member.remove_roles(roleID)
                await ctx.send(msg)
        else:
            await ctx.send("It's an invalid class. For available classes please check `.help`")
    else:
        await ctx.send("You can't use this command here")

@addclass.error
async def adderror(ctx,error):
    await ctx.send(error)

#add and remove roles (for tower, br, expo and general)

role_list = ["Tower Elevator", "BR Maniac", "Crystal Farmer", "Carry Master"]
tower_list = ["tower elevator", "tower", "elevator", "beast tower"]
br_list = ["br", "battle royale", "battle", "royale", "maniac", "br maniac"]
expo_list = ["expo", "expedition", "farmer", "crystal", "crystal farmer"]
carry_list = ["carry master", "carry", "master"]

#add role
@bot.command()
async def addrole(ctx, *a):
    msgInput = " ".join(a)
    msg = msgInput.lower()
    member = ctx.message.author
    if (ctx.channel.name == "weapon-class") or (ctx.channel.name == "bot_testing"):
        if (msg in tower_list) or (msg in br_list) or (msg in expo_list) or (msg in carry_list):
            if msg in tower_list:
                role_num = 0
            elif msg in br_list:
                role_num = 1
            elif msg in expo_list:
                role_num = 2
            elif msg in carry_list:
                role_num = 3
            roleID = discord.utils.get(ctx.guild.roles, name = role_list[role_num])
            if (roleID in member.roles):
                msg = "You already have the " + role_list[role_num] + " role"
                await ctx.send(msg)
            else:
                msg = role_list[role_num] + " role is added"
                await member.add_roles(roleID)
                await ctx.send(msg)
        else:
            msg = "It's an invalid role. For available roles please check `.help`"
    else:
        msg = "You can't use this command here"
        await ctx.send(msg)

#remove role
@bot.command()
async def removerole(ctx, *a):
    msgInput = " ".join(a)
    msg = msgInput.lower()
    member = ctx.message.author
    if (ctx.channel.name == "weapon-class") or (ctx.channel.name == "bot_testing"):
        if (msg in tower_list) or (msg in br_list) or (msg in expo_list) or (msg in carry_list):
            if msg in tower_list:
                role_num = 0
            elif msg in br_list:
                role_num = 1
            elif msg in expo_list:
                role_num = 2
            elif msg in carry_list:
                role_num = 3
            roleID = discord.utils.get(ctx.guild.roles, name = role_list[role_num])
            if (roleID not in member.roles):
                msg = "You don't have the " + role_list[role_num] + " role"
                await ctx.send(msg)
            else:
                msg = role_list[role_num] + " role is removed"
                await member.remove_roles(roleID)
                await ctx.send(msg)
        else:
            msg = "It's an invalid role. For available roles please check `.help`"
    else:
        msg = "You can't use this command here"
        await ctx.send(msg)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#behemoth simulation
sim_s_behe_end_msg = {"B":"Try harder next time <a:WHALEHARD:462505685800845312>",
                     "A":"At least a tiny step to LB a SS gear <:heyooo:382266699065589760>",
                     "S":"Oh you thought the gold circle will give you a SS? But it's just another LB fodder ( ͡° ͜ʖ ͡°)",
                     "SS":"What is this luck? <:slimeWut:472120440119099392>"}
sim_s_magi_end_msg = {"B":"Try harder next time <a:WHALEHARD:462505685800845312>",
                     "A":"At least a tiny step to awaken a SS magi <:heyooo:454450358257844224>",
                     "S":"Oh you thought the gold lottery machine will give you a SS? But it's just another awakening fodder ( ͡° ͜ʖ ͡°)",
                     "SS":"What is this luck? <:slimeWut:472120440119099392>"}
sim_m_end_msg = ["RNG machine is working as usual huh? Try to <a:WHALEHARD:462505685800845312> next time",
                 "You got lucky there with 1 SS. Why not pull moar? <:hue:454309821798154240>",
                 "Guess you told Boldon to roll a lot of Luck ability on your gear? <:boldonstare:382267568435625985>",
                 "Did you bribe RNG? <:slimeWut:472120440119099392>",
                 "Oh no. Look behind you. A salt hill is coming\nhttps://gfycat.com/EssentialShortHypsilophodon"]

@bot.command()
async def behesim(ctx, count: str, step: int = 1):
    if (ctx.message.channel.name == "bot-playroom") or (ctx.message.channel.name == "bot_testing"):
        sim_result = ""
        sim_count = 0
        if count == "single":
            sim_result += summon_sim(1)
            msg = ("**{0}** snapped finger at the banner and...."
                    "\n\n**" + sim_result + " rank** behemoth came out!\n" + sim_s_behe_end_msg[sim_result]).format(ctx.message.author.name)
            await ctx.send(msg)
        elif count == "multi":
            if (step >= 1) and (step <= 5):
                while sim_count != 10:
                    sim_result += (summon_sim(step)+", ")
                    sim_count += 1
                if "SS" in sim_result:
                    sim_result += "SS"
                else:
                    sim_result += summon_sim_last(step)
                SS_count = sim_result.count("SS")
                if SS_count >= 4:
                    SS_count = 4
                msg = ("**{0}** snapped finger at the banner with {1}\% SS rate and...."
                       "\n\n**" + sim_result + " rank** behemoths pop out!!!\n" + sim_m_end_msg[SS_count]).format(ctx.message.author.name,(step+2))
                await ctx.send(msg)
            else:
                await ctx.send("The step you entered doesn't look right")
    else:
        await ctx.send("Please go to <#470713788291874837> to play with the summon simulation")
@behesim.error
async def behesim_error(ctx,error):
    await ctx.send("Try again and state if you want single or multi summon, and enter a valid step number if it's multi pull")

@bot.command()
async def magisim(ctx, count: str):
    if ctx.message.channel.name == "bot-playroom":
        sim_result = ""
        sim_count = 0
        if count == "single":
            sim_result += summon_sim(1)
            msg = ("**{0}** kicked off Pikke and spin the lottery machine...."
                    "\n\n**" + sim_result + " rank** magi came out!\n" + sim_s_magi_end_msg[sim_result]).format(ctx.message.author.name)
            await ctx.send(msg)
        elif count == "multi":
            while sim_count != 10:
                sim_result += (summon_sim(1)+", ")
                sim_count += 1
            if "SS" in sim_result:
                sim_result += "SS"
            else:
                sim_result += summon_sim_last(1)
            SS_count = sim_result.count("SS")
            if SS_count >= 4:
                SS_count = 4
            msg = ("**{0}** kicked off Pikke and spin the lottery machine...."
                   "\n\n**" + sim_result + " rank** magis pop out!!!\n" + sim_m_end_msg[SS_count]).format(ctx.message.author.name)
            await ctx.send(msg)
    else:
        await ctx.send("Please go to <#470713788291874837> to play with the summon simulation")
@magisim.error
async def magisim_error(ctx,error):
    await ctx.send("Try again and state if you want single or multi summon")

def summon_sim(step):
    rand_rate = random.randint(1,100)
    SS = 3
    while step != 1:
        SS += 1
        step -= 1
    S = SS+15
    A = S+55
    if (rand_rate <= SS):
        return "SS"
    elif (rand_rate <= S):
        return "S"
    elif (rand_rate <= A):
        return "A"
    else:
        return "B"

def summon_sim_last(step):
    rand_rate = random.randint(1,100)
    SS = 3
    while step != 1:
        SS += 1
        step -= 1
    if (rand_rate <= SS):
        return "SS"
    else:
        return "S"
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#meme area
meme_list = meme_command.get_meme()
meme_list_key = list(meme_list)
meme_list_key.sort()
meme_help = ""
for x in meme_list_key:
    meme_help += "`"
    meme_help += x
    if meme_list_key.index(x) == (len(meme_list_key)-1):
        meme_help += "`"
    else:
        meme_help += "` | "

@bot.command()
async def memelist(ctx):
    emb = (discord.Embed(title="List of memes", description= (meme_help), colour=0xFF0000))
    await ctx.send(embed=emb)

@bot.command(aliases=meme_list_key)
async def meme(ctx):
    meme_msg = ctx.message.content[1:]
    if " " in meme_msg:
        meme_msg = meme_msg.split()
        meme_msg = meme_msg[0]
    m = meme_list[meme_msg]
    if (type(m) is list):
        a = random.randrange(len(m))
        m = m[a]
    emb_msg = discord.Embed()
    emb_msg.set_image(url=m)
    await ctx.send(embed=emb_msg)

@meme.error
async def meme_error(ctx,error):
    emb = (discord.Embed(title="List of memes", description= (meme_help), colour=0xFF0000))
    await ctx.send(embed=emb)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Linton Hue

hue_msg = ["Huueeee~\n\nLinton seems to be happy",
           "Hue!!!!!!\n\nLinton seems to be angry and screams sharply at you",
           "Hueee...\n\nLinton seems to be sad",
           "Huuueeee~\n\nLinton seems to be content",
           ".....\n\nLinton ignored you and flew away",
           "Hue Hue...\n\nLinton seems to be worried",
           "Hue Hue Hue!!\n\nLinton looks excited"]
hue_length = len(hue_msg)
@bot.command()
async def linton(ctx):
    msg = hue_msg[random.randrange(hue_length)]
    hue_emb = discord.Embed(description=msg, colour=0xFF7400)
    hue_emb.set_author(name="Linton", icon_url = "https://images-ext-2.discordapp.net/external/BEksDQuENdVNr3ywLvXNwoRlb3jqi5QN_RaUnx16cSo/https/dp.gogame.net/theme/img/en/chara7.png")
    hue_emb.set_thumbnail(url="https://images-ext-1.discordapp.net/external/szBAaIRXp_rIxcAT5mqxHnWwqPrMoEEQO_hKhOAeQZo/https/i.imgur.com/TiA4za3.png")
    await ctx.send(embed = hue_emb)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#try catch unregistered code

@bot.event
async def on_command_error(ctx,error):
    msg_content = ctx.message.content[1:]
    if " " in msg_content:
        msg_content = msg_content.split()
        msg_content = msg_content[0]
    if (not msg_content.isalpha()) or (msg_content == "behesim") or (msg_content == "magisim") or (msg_content == "meme"):
        pass
    else:    
        print("unregistered command: ",ctx.message.content)
        print("server: ",ctx.message.guild.name)
        print("channel: ",ctx.message.channel.name,"\n")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#run bot

#karyu token
bot.run(secrets.getToken())
