import random as r
import Game_characters as G
import pickle
#存档系统
def cun_dang(atk,hp,wx):
    basedata = []
    basedata.append(atk)
    basedata.append(hp)
    basedata.append(wx)
    pick = open('Tempdata_list.savedata','wb')
    pickle.dump(basedata,pick)
    pick.close()

def temp_cundang_To_Base():
    tem = open('Tempdata_list.savedata','rb')
    temp_list = pickle.load(tem)
    tem.close()
    pic = open('basedata_list.savedata','wb')
    pickle.dump(temp_list,pic)
    pic.close()

#说垃圾话的系统
def Say(x,y,z):
    v = r.randint(1,3)
    if v == 1:
        print(x)
    elif v == 2:
        print(y)
    else:
        print(z)

#修整甲胄，回复状态
def Heal(hp):
    hp += r.randint(4,7)
    return hp

#练功！提升！
def Attack_up(atk,wx):
    atk += r.randint(1,4) + wx
    return atk

# 魔物生成系统
def Summon_mob():
    mingyun = r.randint(1,3)
    if mingyun == 1:
        mob = G.slime
    elif mingyun == 2:
        mob = G.zombie
    else:
        mob = G.skeleton
    return mob



# 战斗系统
''''''
def Battle(Hp,atk):
    Mob = Summon_mob()
    Mob.HP += r.randint(-5,30)
    Mob.ATK += r.randint(-2,4)
    # print(Mob.HP,Mob.ATK)
    # 主角表示想要攻击
    def hero_attack(HeroAtk):
        print('''
        请选择攻击方式：
            1.普通的一拳
            2.认真的一拳''')
        com = input('来选择吧: ')
        if com == '1':
            print( '你发动了技能：', G.Hero.Skill1)
            return G.Hero.skill_one(Mob.HP,HeroAtk)
        elif com == '2':
            print('你发动了技能：', G.Hero.Skill1)
            return G.Hero.skill_two(Mob.HP,HeroAtk)
        else:
            '输入指令不对，请重新输入哦'
            hero_attack(HeroAtk)
    # 魔物表示也想攻击
    def mob_attack(Herohp):
        mingyun = r.randint(1, 2)
        if mingyun == 1:
            print(Mob.Name, '发动了技能：', Mob.Skill1)
            hp = Mob.skill_one(Hp,Mob.ATK)
        else:
            print(Mob.Name,'发动了技能：',Mob.Skill2)
            hp = Mob.skill_two(Hp,Mob.ATK)
        return hp
    # 循环攻击殊死决斗
    while (Hp > 0) and (Mob.HP > 0):
        print('敌方信息:\n',Mob.Name,'\nHP: ',Mob.HP,'\nATK: ',Mob.ATK)
        print('\n我方信息:','\nHP: ',Hp,'\nATK: ',atk)
        Mob.HP = hero_attack(atk)
        if Mob.HP > 0:
            Hp = mob_attack(Hp)
        else:
            break
        # print(Hp,(Hp and Mob.HP) > 0)
    if Hp > 0:
        print('恭喜你赢得了这场博弈')
    else:
        print('胜败乃兵家常事，还请少侠下周目继续吧')
    return Hp


# Battle(G.Hero.HP,G.Hero.ATK)
