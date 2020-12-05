import random
import time

yama = []
player1 = []
player2 = []
player3 = []
name1 = ""
name2 = ""
drawnext = 0


def reset():

    global yama,player1,player2,player3,name1,name2,drawnext,turnnum

    yama = ["r0","r1","r1","r2","r2","r3","r3","r4","r4","r5","r5","r6","r6","r7","r7","r8","r8","r9","r9"]
    yama += ["b0","b1","b1","b2","b2","b3","b3","b4","b4","b5","b5","b6","b6","b7","b7","b8","b8","b9","b9"]
    yama += ["y0","y1","y1","y2","y2","y3","y3","y4","y4","y5","y5","y6","y6","y7","y7","y8","y8","y9","y9"]
    yama += ["g0","g1","g1","g2","g2","g3","g3","g4","g4","g5","g5","g6","g6","g7","g7","g8","g8","g9","g9"]
    yama += ["Wx","Wx","Wx","Wx"]
    yama += ["rD","rD","bD","bD","yD","yD","gD","gD"]
    yama += ["rR","rR","bR","bR","yR","yR","gR","gR"]
    yama += ["rS","rS","bS","bS","yS","yS","gS","gS"]
    random.shuffle(yama)

    player1 = []
    player2 = [] #com1
    player3 = [] #com2

    anime = ["栗山未来","イリヤ","中世古香織","中川夏紀","七咲逢","上崎理沙","長門有希","亜玖璃","百地たまて","志摩リン","各務原なでしこ","大垣千明","犬山あおい","安達","しまむら"]

    print("対戦相手を検索しています",end="",flush=True)
    for i in range(7):
        time.sleep(random.randint(1,2))
        print(".",end="",flush=True)

    print("\n",end="")
    
    nameseed = []
    nameseed += anime
    
    random.shuffle(nameseed)
    name1 = nameseed.pop()
    name2 = nameseed.pop()

    print("ゲームの準備ができました！\n対戦相手は " + name1 + "さん と " + name2 + "さん です\n\n",end="")
    time.sleep(1)

    for i in range(7):
        player1.append(yama.pop())
        player2.append(yama.pop())
        player3.append(yama.pop())


def start():

    global yama,player1,player2,player3,name1,name2,ba,drawnext,turnnum,next

    reset()

    ba = yama.pop()
    while ba == "Wx":
        yama.append(ba)
        random.shuffle(yama)
        ba = yama.pop()
    

    daseru = []

    drawnext = 0
    next = 1

    turnnum = random.randint(0,2)

    if turnnum == 0:
        print("  あなたからスタートです",end="")
    elif turnnum == 1:
        print("  " + name1 + "さん からスタートです",end="")
    elif turnnum == 2:
        print("  " + name2 + "さん からスタートです",end="")
    

    while player1 != [] and player2 != [] and player3 != []:

        #ゲーム進行
        if turnnum%3 == 0:
            player()
        elif turnnum%3 == 1:
            com1()
        elif turnnum%3 == 2:
            com2()
        
        turnnum += next

        

    

    #終了メッセージ
    if player1 == []:
        print("\n  \033[1m<<あなたの勝ちです>>\033[0m",end="")
    elif player2 == []:
        print("\n  \033[1m<<" + name1 + "さん の勝ちです>>\033[0m",end="")
    else:
        print("\n  \033[1m<<" + name2 + "さん の勝ちです>>\033[0m",end="")
    



def player():

    global yama,player1,player2,player3,name1,name2,ba,drawnext,turnnum,next

    print("\n\033[4mあなたのターンです\033[0m\n",end="")
    
    for i in range(drawnext):
        player1.append(yama.pop())
    
    drawnext = 0
        
    daseru = []

    tefudanum = len(player1)

    print("    場にあるのは",end="")

    if ba[:1] == "r":
        print("\033[31m",end="")
    elif ba[:1] == "b":
        print("\033[36m",end="")
    elif ba[:1] == "y":
        print("\033[33m",end="")
    else:
        print("\033[32m",end="")
    

    print(ba + "\033[0mです．どれを捨てますか(番号で選択)\n",end="")

    for x in range(tefudanum):
        tefudainfo = player1[x]
        if tefudainfo[:1] == "r":
            print("\033[31m",end="")
        elif tefudainfo[:1] == "b":
            print("\033[36m",end="")
        elif tefudainfo[:1] == "y":
            print("\033[33m",end="")
        elif tefudainfo[:1] == "g":
            print("\033[32m",end="")
        else:
            print("\033[30m\033[47m",end="")
        

        if ba[:1] == tefudainfo[:1] or ba[1:] == tefudainfo[1:] or "x" == tefudainfo[1:]:
            print("[" + str(x) + "]:" + player1[x] + " \033[0m",end="")
            daseru.append(x)
        else:
            print("[E]:" + player1[x] + " \033[0m",end="")
        
    
    print("\n",end="")

    if len(daseru) == 0:
        player1.append(yama.pop())
        print("    出せる手札がないのでパスします．\n    引いた手札は",end="")
        
        tefudainfo = player1[-1]
        if tefudainfo[:1] == "r":
            print("\033[31m",end="")
        elif tefudainfo[:1] == "b":
            print("\033[36m",end="")
        elif tefudainfo[:1] == "y":
            print("\033[33m",end="")
        elif tefudainfo[:1] == "g":
            print("\033[32m",end="")
        else:
            print("\033[30m\033[47m",end="")
        

        print(player1[tefudanum] + "\033[0mです．\n",end="")

    else:
        suteru = int(input())

        while suteru in daseru == False:
            print("  無効な入力です\n",end="")
            suteru = input()
        
                
        suteruinfo = player1[suteru]

        if suteruinfo[:1] == "W":

            print("    どの色にしますか(数字で選択)\n\033[31m[:1]:red \033[36m[1:]:blue \033[33m[2]:yellow \033[32m[3]:green\033[0m\n",end="")
            iro = int(input())

            num = [0,1,2,3]

            while iro in num == False:
                print("  無効な入力です\n",end="")
                iro = int(input())
                
            wildcolors = ["rx","bx","yx","gx"]
            player1[suteru] = wildcolors[iro]
            
        elif suteruinfo[1:] == "D":
            drawnext = 2
            print("\033[41mドロー +" + str(drawnext) + "！\033[0m\n",end="")
        elif suteruinfo[1:] == "R":
            next = -next
            print("\033[41mリバース！\033[0m\n",end="")
        elif suteruinfo[1:] == "S":
            turnnum += next
            print("\033[41mスキップ！\033[0m\n",end="")
        

        ba = player1[suteru]
        del player1[suteru]

        #連続投下

        daseru = []

        tefudanum = len(player1)

        for x in range(tefudanum):
            tefudainfo = player1[x]
            if ba[1:] == tefudainfo[1:]:
                daseru.append(x)
            
        

        while len(daseru) != 0:

            print("  あなたが捨てたのは",end="")

            if ba[:1] == "r":
                print("\033[31m",end="")
            elif ba[:1] == "b":
                print("\033[36m",end="")
            elif ba[:1] == "y":
                print("\033[33m",end="")
            else:
                print("\033[32m",end="")
            

            print(ba + "\033[0mです．続けて捨てますか(番号で選択)\n",end="")

            for x in range(tefudanum):
                tefudainfo = player1[x]
                if tefudainfo[:1] == "r":
                    print("\033[31m",end="")
                elif tefudainfo[:1] == "b":
                    print("\033[36m",end="")
                elif tefudainfo[:1] == "y":
                    print("\033[33m",end="")
                elif tefudainfo[:1] == "g":
                    print("\033[32m",end="")
                else:
                    print("\033[30m\033[47m",end="")
                

                if ba[1:] == tefudainfo[1:]:
                    print("[" + str(x) + "]:" + player1[x] + " \033[0m",end="")
                    daseru.append(x)
                else:
                    print("[E]:" + player1[x] + " \033[0m",end="")
                
            
            print("[Q]:捨てない\n",end="")

            suteru = input()

            if suteru != "Q" and suteru != "q":


                while suteru in daseru == False:
                    print("  無効な入力です\n",end="")
                    suteru = input()               
                
                suteruinfo = player1[int(suteru)]

                if suteruinfo[:1] == "W":

                    print("    どの色にしますか(番号で選択)\n\033[31m[:1]:red \033[36m[1:]:blue \033[33m[2]:yellow \033[32m[3]:green\033[0m\n",end="")
                    iro = int(input())

                    num = [0,1,2,3]

                    while iro in num == False:
                        print("  無効な入力です\n",end="")
                        iro = int(input())
                
                    wildcolors = ["rx","bx","yx","gx"]
                    player1[suteru] = wildcolors[iro]
            
                elif suteruinfo[1:] == "D":
                    drawnext += 2
                    print("\033[41mドロー +" + str(drawnext) + "！\033[0m\n",end="")
                elif suteruinfo[1:] == "R":
                    next = -next
                    print("\033[41mリバース！\033[0m\n",end="")
                elif suteruinfo[1:] == "S":
                    turnnum += next
                    print("\033[41mスキップ！\033[0m\n",end="")
                

                #まだ出せるかチェック
                ba = player1[int(suteru)]
                del player1[int(suteru)]

                daseru = []

                tefudanum = len(player1)

                for x in range(tefudanum):
                    tefudainfo = player1[x]
                    if ba[1:] == tefudainfo[1:]:
                        daseru.append(x)
        

            else:
                daseru = []



def com1():

    global yama,player1,player2,player3,name1,name2,ba,drawnext,turnnum,next

    print("\n\033[4m" + name1 + "さん のターンです\033[0m\n",end="")

    time.sleep(random.randint(1,7))

    daseru = []

    for i in range(drawnext):
        player2.append(yama.pop())
    
    drawnext = 0

    
    tefudanum = len(player2)

    print("    場にあるのは",end="")

    if ba[:1] == "r":
        print("\033[31m",end="")
    elif ba[:1] == "b":
        print("\033[36m",end="")
    elif ba[:1] == "y":
        print("\033[33m",end="")
    else:
        print("\033[32m",end="")
    

    print(ba + "\033[0mです．\n",end="")

    for x in range(tefudanum):
        tefudainfo = player2[x]
        if ba[:1] == tefudainfo[:1] or ba[1:] == tefudainfo[1:] or "x" == tefudainfo[1:]:
            daseru.append(x)
        
 

    if len(daseru) == 0:
        player2.append(yama.pop())
        print("    " + name1 + "さん は出せる手札がないのでパスします．\n",end="")
    else:
        laseru = len(daseru)
        suteru = daseru[random.randint(0,laseru-1)]
        suteruinfo = player2[suteru]
        if suteruinfo[:1] == "W":
            whichclolour = ["rx","bx","yx","gx"]
            wcl = len(whichclolour)
            player2[suteru] = whichclolour[random.randint(0,wcl-1)]
        elif suteruinfo[1:] == "D":
            drawnext = 2
            print("\033[41mドロー +" + str(drawnext) + "！\033[0m\n",end="")
        elif suteruinfo[1:] == "R":
            next = -next
            print("\033[41mリバース！\033[0m\n",end="")
        elif suteruinfo[1:] == "S":
            turnnum += next
            print("\033[41mスキップ！\033[0m\n",end="")
        

        msg = ("    " + name1 + "さん は")

        suteruinfo = player2[suteru]
        if suteruinfo[:1] == "r":
            msg += ("\033[31m")
        elif suteruinfo[:1] == "b":
            msg += ("\033[36m")
        elif suteruinfo[:1] == "y":
            msg += ("\033[33m")
        else:
            msg += ("\033[32m")
        

        print(msg + player2[suteru] + "\033[0mをすてました．\n",end="")

        ba = player2[suteru]
        del player2[suteru]

        #連続投下

        daseru = []

        
        tefudanum = len(player2)

        for x in range(tefudanum):
            tefudainfo = player2[x]
            if ba[1:] == tefudainfo[1:]:
                daseru.append(x)
            
        

        while len(daseru) != 0:

            laseru = len(daseru)
            suteru = daseru[random.randint(0,laseru-1)]

            suteruinfo = player2[suteru]

            if suteruinfo[:1] == "W":
                whichclolour = ["rx","bx","yx","gx"]
                wcl = len(whichclolour)
                player2[suteru] = whichclolour[random.randint(0,wcl-1)]
            elif suteruinfo[1:] == "D":
                drawnext += 2
                print("\033[41mドロー +" + str(drawnext) + "！\033[0m\n",end="")
            elif suteruinfo[1:] == "R":
                next = -next
                print("\033[41mリバース！\033[0m\n",end="")
            elif suteruinfo[1:] == "S":
                turnnum += next
                print("\033[41mスキップ！\033[0m\n",end="")
                
                
            #まだ出せるかチェック
            ba = player2[suteru]
            del player2[suteru]

            print("    続けて",end="")

            if ba[:1] == "r":
                print("\033[31m",end="")
            elif ba[:1] == "b":
                print("\033[36m",end="")
            elif ba[:1] == "y":
                print("\033[33m",end="")
            else:
                print("\033[32m",end="")
                

            print("" + ba + "\033[0mを捨てました\n",end="")

            daseru = []

            tefudanum = len(player2)

            for x in range(tefudanum):
                tefudainfo = player2[x]
                if ba[1:] == tefudainfo[1:]:
                    daseru.append(x)
                    

            
        
    
    print("    " + name1 + "さん の手札は\033[41m" + str(len(player2)) + "枚\033[0mです\n",end="")


def com2():

    global yama,player1,player2,player3,name1,name2,ba,drawnext,turnnum,next

    print("\n\033[4m" + name2 + "さん のターンです\033[0m\n",end="")

    time.sleep(random.randint(1,7))

    daseru = []

    for i in range(drawnext):
        player3.append(yama.pop())
    
    drawnext = 0

    
    tefudanum = len(player3)

    print("    場にあるのは",end="")

    if ba[:1] == "r":
        print("\033[31m",end="")
    elif ba[:1] == "b":
        print("\033[36m",end="")
    elif ba[:1] == "y":
        print("\033[33m",end="")
    else:
        print("\033[32m",end="")
    

    print(ba + "\033[0mです．\n",end="")

    for x in range(tefudanum):
        tefudainfo = player3[x]
        if ba[:1] == tefudainfo[:1] or ba[1:] == tefudainfo[1:] or "x" == tefudainfo[1:]:
            daseru.append(x)
        
 

    if len(daseru) == 0:
        player3.append(yama.pop())
        print("    " + name2 + "さん は出せる手札がないのでパスします．\n",end="")
    else:
        laseru = len(daseru)
        suteru = daseru[random.randint(0,laseru-1)]
        suteruinfo = player3[suteru]
        if suteruinfo[:1] == "W":
            whichclolour = ["rx","bx","yx","gx"]
            wcl = len(whichclolour)
            player3[suteru] = whichclolour[random.randint(0,wcl-1)]
        elif suteruinfo[1:] == "D":
            drawnext = 2
            print("\033[41mドロー +" + str(drawnext) + "！\033[0m\n",end="")
        elif suteruinfo[1:] == "R":
            next = -next
            print("\033[41mリバース！\033[0m\n",end="")
        elif suteruinfo[1:] == "S":
            turnnum += next
            print("\033[41mスキップ！\033[0m\n",end="")
        

        msg = ("    " + name2 + "さん は")

        suteruinfo = player3[suteru]
        if suteruinfo[:1] == "r":
            msg += ("\033[31m")
        elif suteruinfo[:1] == "b":
            msg += ("\033[36m")
        elif suteruinfo[:1] == "y":
            msg += ("\033[33m")
        else:
            msg += ("\033[32m")
        

        print(msg + player3[suteru] + "\033[0mをすてました．\n",end="")

        ba = player3[suteru]
        del player3[suteru]

        #連続投下

        daseru = []

        
        tefudanum = len(player3)

        for x in range(tefudanum):
            tefudainfo = player3[x]
            if ba[1:] == tefudainfo[1:]:
                daseru.append(x)
            
        

        while len(daseru) != 0:

            laseru = len(daseru)
            suteru = daseru[random.randint(0,laseru-1)]

            suteruinfo = player3[suteru]

            if suteruinfo[:1] == "W":
                whichclolour = ["rx","bx","yx","gx"]
                wcl = len(whichclolour)
                player3[suteru] = whichclolour[random.randint(0,wcl-1)]
            elif suteruinfo[1:] == "D":
                drawnext += 2
                print("\033[41mドロー +" + str(drawnext) + "！\033[0m\n",end="")
            elif suteruinfo[1:] == "R":
                next = -next
                print("\033[41mリバース！\033[0m\n",end="")
            elif suteruinfo[1:] == "S":
                turnnum += next
                print("\033[41mスキップ！\033[0m\n",end="")
                
                
            #まだ出せるかチェック
            ba = player3[suteru]
            del player3[suteru]

            print("    続けて",end="")

            if ba[:1] == "r":
                print("\033[31m",end="")
            elif ba[:1] == "b":
                print("\033[36m",end="")
            elif ba[:1] == "y":
                print("\033[33m",end="")
            else:
                print("\033[32m",end="")
                

            print("" + ba + "\033[0mを捨てました\n",end="")

            daseru = []

            tefudanum = len(player3)

            for x in range(tefudanum):
                tefudainfo = player3[x]
                if ba[1:] == tefudainfo[1:]:
                    daseru.append(x)
                    

            
        
    
    print("    " + name2 + "さん の手札は\033[41m" + str(len(player3)) + "枚\033[0mです\n",end="")


start()