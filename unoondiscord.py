import discord
import random
import time

# 自分のBotのアクセストークン
with open("bot.token") as tokenfile:
    TOKEN = tokenfile.read()

# 接続に必要なオブジェクトを生成
client = discord.Client()

roomlist = []
roommemberlist = []
roommemberid = []

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('UNO botがログインしました')
    

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    global roomlist,roommemberlist,roommemberid

    if message.author.bot:
        return

    if message.content.startswith("!!uno"):
        command = message.content[6:]

        if command.startswith("room"):

            roomsandmembers = []
            for x in range(len(roomlist)):
                eachroommember = ',' .join(roommemberlist[x])
                roomsandmembers.append(str(x) + " : " + roomlist[x] + "\n    [" + eachroommember + "]")
            
            roominfo = '\n' .join(roomsandmembers)

            embed = discord.Embed(title="現在作られているroom一覧です",description=roominfo,color=discord.Colour.from_rgb(255,0,0))
            await message.channel.send(embed=embed)

        if command.startswith("join"):

            error = False
            for x in range(len(roommemberid)):
                if message.author.id in roommemberid[x]:
                    error = True
            
            if error:
                await message.channel.send("あなたはすでにルームに参加しています")
            else:

                roomnum = command[5:]
                roomnum = int(roomnum)

                if roomnum > len(roomlist) or roomnum < 0:
                    await message.channel.send("正しい番号をひとつだけ入力してください")
                else:
                    roommemberid[roomnum].append(message.author.id)
                    roommemberlist[roomnum].append(message.author.name)

                    eachroommembernames = ', ' .join(roommemberlist[roomnum])

                    host = client.get_user(roommemberid[roomnum][0])

                    roomsandmembers = []
                    for x in range(len(roomlist)):
                        eachroommember = ',' .join(roommemberlist[x])
                        roomsandmembers.append(str(x) + " : " + roomlist[x] + "\n    [" + eachroommember + "]")

                    roominfo = '\n' .join(roomsandmembers)

                    embed = discord.Embed(title=message.author.name + "があなたのルームに参加しました",description=roominfo,color=discord.Colour.from_rgb(255,0,0))
                    await host.channel.send(embed=embed)
                    embed = discord.Embed(title=roomlist[roomnum] + "に参加しました！\n    [host : " + eachroommembernames + "]",description=roominfo,color=discord.Colour.from_rgb(255,0,0))
                    await message.channel.send(embed=embed)

                    #await host.send(message.author.name + "があなたのルームに参加しました")
                    #await message.channel.send(roomlist[roomnum] + "に参加しました！\n    [host : " + eachroommembernames + "]")



        if command.startswith("leave"):
            
            authorid = message.author.id
            roomnum = -1
            usernum = -1

            for x in range(len(roommemberid)):
                for y in range(len(roommemberid[x])):
                    if authorid == roommemberid[x][y]:
                        roomnum = x
                        usernum = y
            

            if roomnum == -1:
                await message.channel.send("あなたはルームに参加していません")
            else:

                await message.channel.send("あなたはルーム(" + roomlist[roomnum] + ")から退出しました")

                del roommemberid[roomnum][usernum]
                del roommemberlist[roomnum][usernum]

                if roommemberlist[roomnum] == []:
                    del roommemberlist[roomnum]
                    del roomlist[roomnum]
                    del roommemberid[roomnum]
                else:
                    newhost = client.get_user(roommemberid[roomnum][0])
                    await newhost.send(message.author.name + "があなたのルームから退出しました．現在あなたがホストです．")



        
        if command.startswith("make"):
            roomname = command[5:]
            hostname = message.author.name
            hostid = message.author.id

            error = -1

            for x in range(len(roommemberid)):
                if hostid in roommemberid[x]:
                    error = x
            
            if error != -1:
                await message.channel.send("あなたはすでにルーム(" + roomlist[error] + ")を作成済みです")
            else:
                roomlist.append(roomname)
                
                ex = []
                ex.append(hostname)
                roommemberlist.append(ex)

                ex = []
                ex.append(hostid)
                roommemberid.append(ex)

                await message.channel.send(roomlist[-1] + "を作成しました！")


        if command.startswith("start"):
            authorid = message.author.id
            roomnum = -1
            usernum = -1

            for x in range(len(roommemberid)):
                for y in range(len(roommemberid[x])):
                    if authorid == roommemberid[x][y]:
                        roomnum = x
                        usernum = y
            

            if roomnum == -1:
                await message.channel.send("あなたはルームに参加していません")
            elif usernum != 0:
                await message.channel.send("あなたはホストではありません")
            else:
                await uno(roomlist[roomnum],roommemberlist[roomnum],roommemberid[roomnum])

@client.event
async def uno(roomname,membersname,membersid):
    yama = ["r0","r1","r1","r2","r2","r3","r3","r4","r4","r5","r5","r6","r6","r7","r7","r8","r8","r9","r9"]
    yama += ["b0","b1","b1","b2","b2","b3","b3","b4","b4","b5","b5","b6","b6","b7","b7","b8","b8","b9","b9"]
    yama += ["y0","y1","y1","y2","y2","y3","y3","y4","y4","y5","y5","y6","y6","y7","y7","y8","y8","y9","y9"]
    yama += ["g0","g1","g1","g2","g2","g3","g3","g4","g4","g5","g5","g6","g6","g7","g7","g8","g8","g9","g9"]
    yama += ["Wx","Wx","Wx","Wx"]
    yama += ["rD","rD","bD","bD","yD","yD","gD","gD"]
    yama += ["rR","rR","bR","bR","yR","yR","gR","gR"]
    yama += ["rS","rS","bS","bS","yS","yS","gS","gS"]
    random.shuffle(yama)

    playercard = []
    population = len(membersid)

    for x in range(len(membersid)):
        playercard.append([])

    for i in range(7):
        for x in range(population):
            playercard[x].append(yama.pop())

    for x in range(population):
        player = client.get_user(membersid[x])
        allplayers = ""
        for y in range(population):
            if y == x:
                pass
            else:
                allplayers = "と" + membersname[y] + " さん "
        
        await player.send("ゲームの準備ができました！\n対戦相手は " + allplayers[1:] + "です")
    
    time.sleep(1.5)

    ba = yama.pop()
    while ba == "Wx":
        yama.append(ba)
        random.shuffle(yama)
        ba = yama.pop()

    daseru = []

    drawnext = 0
    next = 1

    turnnum = random.randrange(population)

    for x in range(population):
        player = client.get_user(membersid[x])

        if x == turnnum:
            await player.send("あなたからスタートです")
        else:
            await player.send( membersname[turnnum] + "さんからスタートです")

    game = True
    while game: #ゲームスタート


        whoplay = turnnum%population
        nowplayerid = membersid[whoplay]
        player = client.get_user(nowplayerid)

        for x in range(population):
            if nowplayerid != membersid[x]:
                opponent = client.get_user(membersid[x])
                sendtext = membersname[whoplay] + " さんのターンです"
                embed = discord.Embed(title=sendtext,description="",color=discord.Colour.from_rgb(255,0,0))
                await opponent.send(embed=embed)
        
        for i in range(drawnext):
            playercard[whoplay].append(yama.pop())
    
        drawnext = 0

        daseru = []

        tefudanum = len(playercard[whoplay])

        sendtext = "    場にあるのは\n" + ba + "です．どれを捨てますか(番号で選択)\n"

        for x in range(tefudanum):
            tefudainfo = playercard[whoplay][x]
            if ba[0] == tefudainfo[0] or ba[1] == tefudainfo[1] or "x" == tefudainfo[1]:
                sendtext += "[" + str(x) + "]:" + playercard[whoplay][x] + "  "
                daseru.append(x)
            else:
                sendtext += "[E]:" + playercard[whoplay][x] + "  "

        if len(daseru) == 0:
            playercard[whoplay].append(yama.pop())
            sendtext += "\n    出せる手札がないのでパスします．\n    引いた手札は"

            tefudainfo = playercard[whoplay][-1]
            sendtext += playercard[whoplay][tefudanum] + "です．"

            embed = discord.Embed(title="あなたのターンです",description=sendtext,color=discord.Colour.from_rgb(255,0,0))
            await player.send(embed=embed)

            for x in range(population):
                if nowplayerid != membersid[x]:
                    opponent = client.get_user(membersid[x])
                    sendop = membersname[whoplay] + " さん がパスしました"
                    embed = discord.Embed(title=sendop,description="",color=discord.Colour.from_rgb(255,0,0))
                    await opponent.send(embed=embed)

        else:

            embed = discord.Embed(title="あなたのターンです",description=sendtext,color=discord.Colour.from_rgb(255,0,0))
            await player.send(embed=embed)
            sendtext = ""
            sendop = ""

            def cardcheck(message):
                strdaseru = ["q","Q"]
                for x in daseru:
                    strdaseru.append(str(x))

                return message.author.id == nowplayerid and message.content in strdaseru and message.channel.id != 697321149872472107

            msg = await client.wait_for('message', check=cardcheck)
            suteru = msg.content
            suteru = int(suteru)

            suteruinfo = playercard[whoplay][int(suteru)]

            if suteruinfo[0] == "W":

                choicecolour = "どの色にしますか(数字で選択)\n[0]:red [1]:blue [2]:yellow [3]:green"
                embed = discord.Embed(title=sendop,description=choicecolour,color=discord.Colour.from_rgb(255,0,0))
                await player.send(embed=embed)
                
                def irocheck(message):
                    return message.author.id == nowplayerid and message.content in ["0","1","2","3"] and message.channel.id != 697321149872472107

                msg = await client.wait_for('message', check=irocheck)
                iro = msg.content
                iro = int(iro)

                wildcolors = ["rx","bx","yx","gx"]
                playercard[whoplay][suteru] = wildcolors[iro]

            elif suteruinfo[1] == "D":
                drawnext = 2
                sendtext = "ドロー +" + str(drawnext) + "！"
                sendop = "ドロー +" + str(drawnext) + "！"
            elif suteruinfo[1] == "R":
                next = -next
                sendtext = "リバース！"
                sendop = "リバース！"
            elif suteruinfo[1] == "S":
                turnnum += next
                sendtext = "スキップ！"
                sendop = "スキップ！"

            yama.insert(0,ba)
            ba = playercard[whoplay][suteru]
            del playercard[whoplay][suteru]

            sendop += "\n" + membersname[whoplay] + " さん が" + ba + "を捨てました"

            #連続投下

            daseru = []

            tefudanum = len(playercard[whoplay])

            for x in range(tefudanum):
                tefudainfo = playercard[whoplay][x]
                if ba[1:] == tefudainfo[1:]:
                    daseru.append(x)



            while len(daseru) != 0:

                sendtext += "\n  あなたが捨てたのは" + ba + "です．続けて捨てますか(番号で選択)\n"
                for x in range(tefudanum):
                    tefudainfo = playercard[whoplay][x]
                    if ba[1] == tefudainfo[1]:
                        sendtext += "[" + str(x) + "]:" + playercard[whoplay][x] + "  "
                        #daseru.append(x)
                    else:
                        sendtext += "[E]:" + playercard[whoplay][x] + "  "

                sendtext += "[Q]:捨てない"

                embed = discord.Embed(title="",description=sendtext,color=discord.Colour.from_rgb(255,0,0))
                await player.send(embed=embed)
                sendtext = ""

                msg = await client.wait_for('message', check=cardcheck)
                suteru = msg.content

                if suteru[0] != "Q" and suteru[0] != "q":

                    suteru = int(suteru)
                    suteruinfo = playercard[whoplay][suteru]

                    if suteruinfo[0] == "W":

                        sendtext = "どの色にしますか(数字で選択)\n[0]:red [1]:blue [2]:yellow [3]:green"

                        embed = discord.Embed(title="",description=sendtext,color=discord.Colour.from_rgb(255,0,0))
                        await player.send(embed=embed)

                        msg = await client.wait_for('message', check=irocheck)
                        iro = msg.content
                        iro = int(iro)

                        wildcolors = ["rx","bx","yx","gx"]
                        playercard[whoplay][suteru] = wildcolors[iro]

                    elif suteruinfo[1] == "D":
                        drawnext = 2
                        sendtext = "ドロー +" + str(drawnext) + "！"
                        senop += "\nドロー +" + str(drawnext) + "！"
                    elif suteruinfo[1] == "R":
                        next = -next
                        sendtext = "リバース！"
                        sendop += "\nリバース！"
                    elif suteruinfo[1] == "S":
                        turnnum += next
                        sendtext = "スキップ！"
                        sendop += "\nスキップ！"


                    #まだ出せるかチェック
                    yama.insert(0,ba)
                    ba = playercard[whoplay][suteru]
                    del playercard[whoplay][suteru]

                    sendop += "\n続けて" + ba + "を捨てました"

                    daseru = []

                    tefudanum = len(playercard[whoplay])

                    for x in range(tefudanum):
                        tefudainfo = playercard[whoplay][x]
                        if ba[1] == tefudainfo[1]:
                            daseru.append(x)


                else:
                    daseru = []
                    sendtext = ""

            sendtext += "\n  あなたが捨てたのは" + ba + "です．"
            embed = discord.Embed(title="",description=sendtext,color=discord.Colour.from_rgb(255,0,0))
            await player.send(embed=embed)

            for x in range(population):
                if nowplayerid != membersid[x]:
                    opponent = client.get_user(membersid[x])
                    embed = discord.Embed(title=sendop,description="",color=discord.Colour.from_rgb(255,0,0))
                    await opponent.send(embed=embed)

        for x in range(population):
            if playercard[x] == []:
                game = False
                finish = x

        turnnum += next

    #終了メッセージ
    for x in range(population):
        player = client.get_user(membersid[x])

        if x == finish:
            embed = discord.Embed(title="YOU WIN!!",description="あなたの勝ちです",color=discord.Colour.from_rgb(255,0,0))
            await player.send(embed=embed)
        else:
            embed = discord.Embed(title="YOU LOSE!!",description=membersname[finish] + "さん の勝ちです",color=discord.Colour.from_rgb(255,0,0))
            await player.send(embed=embed)




# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)