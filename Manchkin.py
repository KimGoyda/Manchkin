import random


def hero():#параметры героя
    hero={'Name':'Kimian','Sila':1,'LvL':1}
    print(hero)
    return hero

# подбор противника
def dungeon():
    var='Monster'
    monstrsila=random.randint(1,10)
    print(var+" have strenght "+str(monstrsila))
    return monstrsila

# улучшение после победы
def up():
     bonussila=random.randint(1,5)
     print(f"Hero get imrove {bonussila} SILA!")
     return bonussila

# ход игры
def round():
    newhero=hero() #загружаем героя
    while newhero['LvL']<10:    #играем до 10 уровня
        print('Lets find new dungeon!\n')
        enemy=dungeon() #подготавливаем противника
        if  enemy<=newhero['Sila']: #происходит бой - если герой побеждает то получает награды
            newhero['LvL']+=1
            sl=up()
            newhero['Sila']=newhero['Sila']+sl
            print('YOU WIN!\nTake a trophy.\n')
            if newhero['LvL']==10: # если герой набирает 10 уровень останаливаем игру
                print(f'You kill all monsters...\n Your results is {newhero}')
                break
        else:#если проигрываем то несем потери
            newhero['LvL']-=1
            print('Enemy was better then you! YOU LOSE!\n')
            if newhero['LvL']==0: #потеряли все уровни - проиграли - останаливаем игру
                print(f'YOU DIED\nYour results is {newhero}')
                break


round()