import discord

# 自分のBotのアクセストークン
with open("bot.token") as tokenfile:
    TOKEN = tokenfile.read()

# 接続に必要なオブジェクトを生成
client = discord.Client()

roomlist = ["roomA","roomB"]
roommemberlist = [["a","b","c"],["abc","def"]]
roommemberid = [[123,456,789],[234,678]]

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
                if message.authorid in x:
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
                    await host.send(message.author.name + "があなたのルームに参加しました")
                    await message.channel.send(roomlist[roomnum] + "に参加しました！\n    [host : " + eachroommembernames + "]")



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


        




# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)