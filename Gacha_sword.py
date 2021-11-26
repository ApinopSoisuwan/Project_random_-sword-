import random
def gacha_sword ():
    sword = ['Wood sword','Iron sword','Gold sword','Platinum sword','Diamond sword','Legendary sword']
    roll_sword = random.choice(sword)
    put_sword = roll_sword
    amulet_critical = ['Normal amulet', 'Light amulet', 'High-class amulet', 'Saint-class amulet', 'Legendary amulet']
    damage_rate = {'Wood sword':10,'Iron sword':20,'Gold sword':30,'Platinum sword':40,'Diamond sword':50,'Legendary sword':99}
    return "Congratulation you got " + roll_sword+'\n'+roll_sword +  ": ATK "+ str(damage_rate[put_sword])

name = input('Enter your Name:')
if name.isdigit():
    print('Error')
else:
    print('Hello : ' + name )
    put_sword = input('Let"s Gacha sword(Y/N)' +'\n'+  "Choice one : ")
    loop_sword = 1
    while loop_sword < 2:
        if put_sword == "Y":
            print(gacha_sword())
            loop_sword += 1
        elif put_sword == "N":
            print("Boom!!!# World has Fallen" +"\n" + "press this,This gonna help you : "" https://youtu.be/dQw4w9WgXcQ")
            loop_sword += 1
        else:
            print("Roll again!!!" + "\n")
            put_sword = input("Let's Roll..(Y/N)" + "\n" + "Choice one : ")





