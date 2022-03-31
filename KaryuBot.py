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
import glossary

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

async def checkPirate():
    await bot.wait_until_ready()
    isSent = False
    guild_name = discord.utils.get(bot.guilds, name="Dragon Project")
    channel = discord.utils.get(guild_name.text_channels, name="pirate-ping")
    while True:
        currentTime = datetime.utcnow()
        currentMinute = currentTime.minute
        if currentMinute == 59 and not isSent:
            await channel.send("<@&616691697254006815> Pirate Loot will be resetting in a minute")
            isSent = True
        elif currentMinute != 59 and isSent:
            isSent = False
        else:
            pass
        await asyncio.sleep(10) #perform check every 10 sec

async def checkHalfPrice():
    await bot.wait_until_ready()
    isSent = False
    guild_name = discord.utils.get(bot.guilds, name="Dragon Project")
    channel = discord.utils.get(guild_name.text_channels, name="hunters-lounge")
    while True:
        currentTime = datetime.utcnow()
        currentHour = currentTime.hour
        weekday = currentTime.weekday()
        if weekday == 2:
            if currentHour == 0 and not isSent:
                await channel.send("Ability half price starts. Time to waste your gold.\n金を捧げよ！ <:GoldCoin:350488194732785665>")
                isSent = True
            elif currentHour != 0 and isSent:
                isSent = False
            else:
                pass
        else:
            pass
        await asyncio.sleep(60) #perform check every minute

#welcome message
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


guild_name = ["testing","OP Clan","New Dawn","[DPG] Rain"]
guild_len = len(guild_name)
chan_name = ["announce-test","bingo-tower-list","guides","guides"]

#post dp-gloabl-info posts in other server
@bot.event
async def on_message(msg):
    if (msg.channel.id == 470713934517764117 or author.id == 241918719507431425):
        wholemsg = "**" + msg.author.name + "** posted in __" + msg.guild.name + "__'s <#470713934517764117>:\n\n" + msg.content
        guild_list = []
        chan_list = []
        for x in range(guild_len):
            guild_list.append(discord.utils.get(bot.guilds, name=guild_name[x]))
            chan_list.append(discord.utils.get(guild_list[x].text_channels, name=chan_name[x]))
            try:
                if bot.user.id != msg.author.id:
                    await chan_list[x].send(wholemsg)
                    if not msg.attachments:
                        pass
                    else:
                        for y in msg.attachments:
                            await chan_list[x].send(y.url)
            except Exception as e:
                print(e)



    await bot.process_commands(msg)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#miscellaneous commands

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def abcdefg(ctx):
    currentTime = datetime.utcnow()
    await ctx.send(currentTime)

@bot.command()
async def atest(ctx, *a):
    msg = list(a)
    await ctx.send(a)

@bot.command()
async def listtest(ctx):
    abcde = ['a','b','c','d','e']
    for x in abcde:
        await ctx.send(x)

@bot.command()
async def getname(ctx):
    arole = ctx.author.roles
    await ctx.send(arole)
    for x in arole:
        await ctx.send(x.name)

@bot.command()
async def getrolelist(ctx):
    try:
        alist = ctx.author.roles
        await ctx.send(alist)
    except Exception as e:
        print(e)

@bot.command()
async def getguild(ctx):
    guild_ls = ctx.author.guild
    await ctx.send(guild_ls)

@bot.command()
async def checkattach(ctx):
    if not ctx.message.attachments:
        await ctx.send("no attachment")
    else:
        try:
            for x in ctx.message.attachments:
                print(x.url)
        except Exception as e:
            print("can't print attachment list")
            print(e)

@bot.command()
async def displayName(ctx):
    await ctx.send(ctx.author.name)



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
    emb.add_field(name = "Role command:", value = "`.addrole <role>` and `.removerole <role>`\nAvailable roles: `tower`, `br`, `expo`, `carry`, `pirate`",inline=False)
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

@bot.command(aliases=["ticket"])
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

g_list = glossary.get_glossary()
g_key = list(g_list)
@bot.command()
async def glossary(ctx, *a):
    not_found = []
    whole = " ".join(a)
    whole = whole.lower()
    split_a = whole.split(",")
    for glos in split_a:
        if glos[0] == " ":
            glos = glos[1:]
        if glos in g_key:
            glos_emb = discord.Embed(description=g_list[glos], colour=0xFFFFFF)
            name = "What does '" + glos + "' mean?"
            glos_emb.set_author(name=name, icon_url="https://cdn.discordapp.com/attachments/470713810232147988/512477914755760157/Igneel.png")
            await ctx.send(embed = glos_emb)
        else:
            word = "`"+glos+"` "
            not_found.append(word)
    if len(not_found) != 0:
        abc = ""
        for x in not_found:
            abc += x
        await ctx.send("I can't find a definition for the following:" + abc)


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
    startMsg = "Time remaining until ability half price "
    if weekday == 2:
        a = "ends: "
        startMsg = "Ability half price in progress!\n" + startMsg
        remainDay = 0
    else:
        a = "starts: "
    msg = startMsg + a + str(remainDay) + " day(s), " + str(remainHour) + " hour(s) and " + str(remainMinute) + " minute(s)"
    await ctx.send(msg)
    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#database search command

channelWhiteList = ["behemoth-magi-hub","bot_testing","executive-room","general-testing"]

@bot.command(aliases=["behemoth","bhm"])
async def behe(ctx, *a):
    memRole = ctx.author.roles
    memRoleName = list()
    for xyz in memRole:
        memRoleName.append(xyz.name)
    if (ctx.channel.name in channelWhiteList) or ("Moderators" in memRoleName):
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


@bot.command(aliases=["weap","weapon"])
async def wep(ctx, *a):
    memRole = ctx.author.roles
    memRoleName = list()
    for xyz in memRole:
        memRoleName.append(xyz.name)
    if (ctx.channel.name in channelWhiteList) or ("Moderators" in memRoleName):
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

@bot.command(aliases=["armour","arm"])
async def armor(ctx, *a):
    memRole = ctx.author.roles
    memRoleName = list()
    for xyz in memRole:
        memRoleName.append(xyz.name)
    if (ctx.channel.name in channelWhiteList) or ("Moderators" in memRoleName):
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
    memRole = ctx.author.roles
    memRoleName = list()
    for xyz in memRole:
        memRoleName.append(xyz.name)
    if (ctx.channel.name in channelWhiteList) or ("Moderators" in memRoleName):
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
        await ctx.send("Please use this function in <#470713716573208576>")

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
        await ctx.send("Please use this function in <#470713716573208576>")

@addclass.error
async def adderror(ctx,error):
    await ctx.send(error)

#add and remove roles (for tower, br, expo and general)

role_list = ["Tower Elevator", "BR Maniac", "Crystal Farmer", "Carry Master", "Pirate Ping"]
tower_list = ["tower elevator", "tower", "elevator", "beast tower"]
br_list = ["br", "battle royale", "battle", "royale", "maniac", "br maniac"]
expo_list = ["expo", "expedition", "farmer", "crystal", "crystal farmer"]
carry_list = ["carry master", "carry", "master"]
pirate_list = ["pirate ping", "pirate", "ping", "pp"]

#add role
@bot.command()
async def addrole(ctx, *a):
    msgInput = " ".join(a)
    msg = msgInput.lower()
    member = ctx.message.author
    if (ctx.channel.name == "weapon-class") or (ctx.channel.name == "bot_testing"):
        if (msg in tower_list) or (msg in br_list) or (msg in expo_list) or (msg in carry_list) or (msg in pirate_list):
            if msg in tower_list:
                role_num = 0
            elif msg in br_list:
                role_num = 1
            elif msg in expo_list:
                role_num = 2
            elif msg in carry_list:
                role_num = 3
            elif msg in pirate_list:
                role_num = 4
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
        msg = "Please use this function in <#470713716573208576>"
        await ctx.send(msg)

#remove role
@bot.command()
async def removerole(ctx, *a):
    msgInput = " ".join(a)
    msg = msgInput.lower()
    member = ctx.message.author
    if (ctx.channel.name == "weapon-class") or (ctx.channel.name == "bot_testing"):
        if (msg in tower_list) or (msg in br_list) or (msg in expo_list) or (msg in carry_list) or (msg in pirate_list):
            if msg in tower_list:
                role_num = 0
            elif msg in br_list:
                role_num = 1
            elif msg in expo_list:
                role_num = 2
            elif msg in carry_list:
                role_num = 3
            elif msg in pirate_list:
                role_num = 4
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
        msg = "Please use this function in <#470713716573208576>"
        await ctx.send(msg)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#behemoth simulation
sim_s_behe_end_msg = {"B":"Try harder next time <a:WHALEHARD:462505685800845312>",
                     "A":"At least a tiny step to LB a SS gear <:heyooo:382266699065589760>",
                     "S":"Oh you thought the gold circle will give you a SS? But it's just another LB fodder ( ͡° ͜ʖ ͡°)",
                     "SS":"What is this luck? <:slimeWut:472120440119099392>",
                     "SSS":"Nani!? Did you tamed Axel? <:dpcongrats:482206735852109852> anyway"}
sim_s_magi_end_msg = {"B":"Try harder next time <a:WHALEHARD:462505685800845312>",
                     "A":"At least a tiny step to awaken a SS magi <:heyooo:454450358257844224>",
                     "S":"Oh you thought the gold lottery machine will give you a SS? But it's just another awakening fodder ( ͡° ͜ʖ ͡°)",
                     "SS":"What is this luck? <:slimeWut:472120440119099392>",
                     "SSS":"Wew, that's some insane ~~whale~~ luck power there"}
sim_m_end_msg = ["RNG machine is working as usual huh? Try to <a:WHALEHARD:462505685800845312> next time",
                 "You got lucky there with 1 SS. Why not pull moar? <:hue:620811525241962515>",
                 "Guess you told Boldon to roll a lot of Luck ability on your gear? <:boldonstare:382267568435625985>",
                 "Did you bribe RNG? <:slimeWut:472120440119099392>",
                 "Oh no. Look behind you. A salt hill is coming\nhttps://gfycat.com/EssentialShortHypsilophodon"]

def formatSim(msg):
    result = msg.split(",")
    fin = ""
    count = 1
    for x in result:
        fin += x
        if count%3 == 0:
            fin += "\n"
        else:
            fin += "\t"
        count += 1
    return fin

def endMsg(msg, abc):
    result = msg.split(",")
    ss_count = 0
    sss_count = 0
    for x in result:
        if x == "SS":
            ss_count+=1
        elif x == "SSS":
            sss_count+=1
        else:
            pass
    if sss_count >= 1:
        endmsg = "Time to flex those SSS {0} <:Gem:350488158170775552> <:Gem:350488158170775552> <:Gem:350488158170775552>".format(abc)
    else:
        endmsg = sim_m_end_msg[ss_count]
    return endmsg

sim_channel = ["bot-playroom","bot_testing"]

@bot.command()
async def behesim(ctx, count: str, step: int = 1):
    memRole = ctx.author.roles
    memRoleName = list()
    for xyz in memRole:
        memRoleName.append(xyz.name)
    if (ctx.channel.name in sim_channel) or ("Moderators" in memRoleName):
        sim_result = ""
        sim_count = 0
        if count == "single":
            sim_result += summon_sim(1)
            msg = ("**{0}** snapped finger at the banner and...."
                    "\n\n**" + sim_result + " ** behemoth came out!\n" + sim_s_behe_end_msg[sim_result]).format(ctx.message.author.name)
            await ctx.send(msg)
        elif count == "multi":
            if (step >= 1) and (step <= 5):
                while sim_count != 10:
                    sim_result += (summon_sim(step)+",")
                    sim_count += 1
                fsim = formatSim(sim_result)
                if "SSS" in fsim:
                    sim_result += "SSS"
                elif "SS" in fsim:
                    sim_result += "SS"
                else:
                    sim_result += summon_sim_last(step)
                msg = ("**{0}** snapped finger at the banner with {1}\% SS rate and...."
                       "\n\n**" + formatSim(sim_result) + "**\nbehemoths pop out!!!\n" + endMsg(sim_result,"gear")).format(ctx.message.author.name,(step+2))
                await ctx.send(msg)
            else:
                await ctx.send("The step you entered doesn't look right")
    else:
        await ctx.send("Please go to <#470713788291874837> to play with the summon simulation")
@behesim.error
async def behesim_error(ctx,error):
    await ctx.send("Try again and state if you want single or multi summon, and enter a valid step number if it's multi pull\nFull command looks like this: `.behesim <single/multi> <step>`")
    print(error)

@bot.command()
async def magisim(ctx, count: str):
    memRole = ctx.author.roles
    memRoleName = list()
    for xyz in memRole:
        memRoleName.append(xyz.name)
    if (ctx.channel.name in sim_channel) or ("Moderators" in memRoleName):
        sim_result = ""
        sim_count = 0
        if count == "single":
            sim_result += summon_sim(1)
            msg = ("**{0}** kicked off Pikke and spin the lottery machine...."
                    "\n\n**" + sim_result + " ** magi came out!\n" + sim_s_magi_end_msg[sim_result]).format(ctx.message.author.name)
            await ctx.send(msg)
        elif count == "multi":
            while sim_count != 10:
                sim_result += (summon_sim(1)+",")
                sim_count += 1
            fsim = formatSim(sim_result)
            if "SSS" in fsim:
                sim_result += "SSS"
            elif "SS" in fsim:
                sim_result += "SS"
            else:
                sim_result += summon_sim_last(1)
            msg = ("**{0}** kicked off Pikke and spin the lottery machine...."
                   "\n\n**" + formatSim(sim_result) + "**\nmagis pop out!!!\n" + endMsg(sim_result,"magi")).format(ctx.message.author.name)
            await ctx.send(msg)
    else:
        await ctx.send("Please go to <#470713788291874837> to play with the summon simulation")
@magisim.error
async def magisim_error(ctx,error):
    await ctx.send("Try again and state if you want single or multi summon\nFull command looks like this: `.magisim <single/multi>`")

def summon_sim(step):
    rand_rate = random.randint(1,100)
    SSS = 1
    SS = SSS + 3
    while step != 1:
        SS += 1
        step -= 1
    S = SS+15
    A = S+55
    if (rand_rate <= SSS):
        return "SSS"
    elif (rand_rate <= SS):
        return "SS"
    elif (rand_rate <= S):
        return "S"
    elif (rand_rate <= A):
        return "A"
    else:
        return "B"

def summon_sim_last(step):
    rand_rate = random.randint(1,100)
    SSS = 1
    SS = 3
    while step != 1:
        SS += 1
        step -= 1
    if (rand_rate <= SSS):
        return "SSS"
    elif (rand_rate <= SSS+SS):
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

def renew_meme():
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
    renew_meme()
    emb = (discord.Embed(title="List of memes", description= (meme_help), colour=0xFF0000))
    await ctx.send(embed=emb)

@bot.command(aliases=meme_list_key)
async def meme(ctx):
    renew_meme()
    meme_list = meme_command.get_meme()
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
        print(error)

respondMsg = {"love":"<:heart:1234>"}
rMsgKey = respondMsg.keys()

#try respond message
#@bot.event
#async def on_message(message):
#    msg = message.content
#    msg = msg.split(" ")
#    if bot.user.id != message.author.id:
#        for x in msg:
#            if x in rMsgKey:
#                await message.channel.send(respondMsg[msg])
#                pass

#    await bot.process_commands(message)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#run bot

#karyu token
#bot.loop.create_task(checkPirate())
#bot.loop.create_task(checkHalfPrice())
bot.run(secrets.getToken())
