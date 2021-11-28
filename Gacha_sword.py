
def gacha_sword ():
    import random
    import webbrowser

    #section name and random sword
    name = input('Enter your Name:')
    sword = ['Wood sword','Iron sword','Gold sword','Platinum sword','Diamond sword','Legendary sword']
    roll_sword = random.choice(sword)
    damage_sword = roll_sword
    damage_rate = {'Wood sword': 10, 'Iron sword': 20, 'Gold sword': 30, 'Platinum sword': 40, 'Diamond sword': 50,
                   'Legendary sword': 99}

    #Amulet sector
    amulet_critical = ['Normal amulet', 'Light amulet', 'High-class amulet', 'Saint-class amulet', 'Legendary amulet']
    amulet_critical_rate = {'Normal amulet': 15, 'Light amulet': 25, 'High-class amulet': 35, 'Saint-class amulet': 45,
                            'Legendary amulet': 65}
    roll_amulet = random.choice(amulet_critical)
    crit_rate = roll_amulet

    #Monster sector
    monster_list = ['Smile','Dragon','Devil']
    monster_dict = {'Smile':30,'Dragon':100,'Devil':200}



    if name.isdigit():
        print('Error')
    else:
        print('Hello : ' + name)
        put_sword = input('Let"s Gacha sword(y/n)' + '\n' + "Choice one : ")
        loop_sword = 1
        while loop_sword < 2:
            if put_sword == 'y':
                loop_sword += 1
                print("Congratulation you got " + roll_sword + '\n' + roll_sword + ": ATK RATE = " + str(damage_rate[damage_sword]))
                put_amulet = input("\n" + 'Hello' + name + "come here and get amulet" + '\n' + 'Let"s Gacha amulet(y/n)' + '\n' + "Choice one : " )
                if put_amulet == 'y':
                    print("Congratulation you got " + roll_amulet + '\n' + roll_amulet + ": Critical RATE = " + str(amulet_critical_rate[crit_rate]))
                elif put_sword == 'n':
                    print("Boom!!!# World has Fallen" + "\n" + "This gonna help you...")
                    webbrowser.open('https://youtu.be/dQw4w9WgXcQ')
            elif put_sword == "n":
                print("Boom!!!# World has Fallen" + "\n" + "This gonna help you...")
                webbrowser.open('https://youtu.be/dQw4w9WgXcQ')
                loop_sword += 1
            else:
                print("Roll again!!!" + "\n")
                put_sword = input("Let's Roll..(y/n)" + "\n" + "Choice one : ")
    return








print(gacha_sword())







