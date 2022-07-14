import random as r
import Game_characters as chara
import System_For_3 as sys3
import pickle as p
import time as t

def Main_Game_Play():

# 读取存档开始
    Canyat = chara.Hero()


# 定义三个循环选择系统
    def Choise_circulation():
# 先搞个变量
        First_Choise = r.randint(1,30)
        Second_Choise = r.randint(1,30)
        Third_Choise = r.randint(1,30)
# 按一定概率去显示选项的函数定义
        def Choise_(niubi):
            if niubi <= 20:
                a = 1
                return ['去战斗！塔塔开！！！',a]
            elif niubi <= 25:
                b = 2
                return ['修整甲胄，回复状态',b]
            else:
                c = 3
                return ['练功！提升！',c]

# 定义选择之后触发事件的函数
# 战斗系统
        def The_first_choise(cho):
            sys3.cun_dang(Canyat.ATK,Canyat.HP,Canyat.WX)
            sys3.temp_cundang_To_Base()
            sys3.Say('\n不好，有敌袭！','\n前方似乎有个黑影','\n那是什么？')
            # sys3.Battle(Canyat.HP,Canyat.ATK)
            return sys3.Battle(Canyat.HP,Canyat.ATK)

# 修整甲胄系统
        def The_second_choise(cho):
            sys3.Say('\n豁，精神起来了', '\n休养生息，还不赖', '\n哦？终于可以休息了吗？')
            Canyat.HP = sys3.Heal(Canyat.HP)
            sys3.cun_dang(Canyat.ATK, Canyat.HP, Canyat.WX)
            sys3.temp_cundang_To_Base()

# 练功系统
        def The_third_choise(cho):
            sys3.Say('\n哈，又有了很大的突破', '\n我的功力在上升', '\n哈哈哈哈哈哈本大爷是无敌的')
            Canyat.ATK = sys3.Attack_up(Canyat.ATK,Canyat.WX)
            sys3.cun_dang(Canyat.ATK, Canyat.HP, Canyat.WX)
            sys3.temp_cundang_To_Base()

# 重定向选择
        def Choise_True(niu):
            if niu == 1:
                # The_first_choise(niu)
                return The_first_choise(niu)
            elif niu == 2:
                The_second_choise(niu)
                return 1
            else:
                The_third_choise(niu)
                return 1


# 进行选择，道路分叉
# 打印目前状态显示给玩家
        print('\n现在的状态是： ','\nHP:\t \t',Canyat.HP,'point','\nATK:\t',Canyat.ATK,'point')
# 打印三个道路选项给玩家
        print('1:  ',Choise_(First_Choise)[0])
        print('2:  ',Choise_(Second_Choise)[0])
        print('3:  ',Choise_(Third_Choise)[0])

# 定义且下一步的函数
        def Next_step_chiose():
            # 玩家输入下一步骤的指示
            Nextstep = input('你需要走那条路（1/2/3）：')
            if Nextstep == '1':
                # Choise_True(Choise_(First_Choise)[1])
                return Choise_True(Choise_(First_Choise)[1])
            elif Nextstep == '2':
                # Choise_True(Choise(Second_Choise)[1])
                return Choise_True(Choise_(Second_Choise)[1])
            elif Nextstep == '3':
                # Choise_True(Choise_(Third_Choise)[1])
                return Choise_True(Choise_(Third_Choise)[1])
            else:
                print('你输入的不是 1 or 2 or 3 哦qwq，再来吧！')
                Next_step_chiose()
# 执行下一步函数
#         Next_step_chiose(Next_step)
        return Next_step_chiose()
    for i in range(0,20):
        jiance = Choise_circulation()
        print(jiance)
        if jiance <= 0:
            # tem = open('Tempdata_list.savedata','rb')
            # temp_list = p.load(tem)
            # tem.close()
            # pic = open('basedata_list.savedata','wb')
            # p.dump(temp_list,pic)
            # pic.close()
            sys3.temp_cundang_To_Base()
            t.sleep(3)
            print('少侠，存档已经为您自动保存，您将开启下一轮之轮回。')
            t.sleep(3)
            quit()
            break


#boss战
    print('经过多次轮回，您终于来到了boss面前')
    t.sleep(1)
    print('可是您发现，boss居然是我自己！')
    t.sleep(1)
    sys3.temp_cundang_To_Base()
    def Bosszhan(Hp, atk):
        Mob = chara.boss
        print(Mob.HP, Mob.ATK)

        # 主角表示想要攻击
        def hero_attack(HeroAtk):
            print('''
                请选择攻击方式：
                    1.普通的一拳
                    2.认真的一拳''')
            com = input('来选择吧: ')
            if com == '1':
                print('你发动了技能：', chara.Hero.Skill1)
                return chara.Hero.skill_one(Mob.HP, HeroAtk)
            elif com == '2':
                print('你发动了技能：', chara.Hero.Skill1)
                return chara.Hero.skill_two(Mob.HP, HeroAtk)
            else:
                '输入指令不对，请重新输入哦'
                hero_attack(HeroAtk)

        # boss表示也想攻击
        def mob_attack(Herohp):
            mingyun = r.randint(1, 2)
            if mingyun == 1:
                print(Mob.Name, '发动了技能：', Mob.Skill1)
                hp = Mob.skill_one(Hp, Mob.ATK)
            else:
                print(Mob.Name, '发动了技能：', Mob.Skill2)
                hp = Mob.skill_two(Hp, Mob.ATK)
            return hp

        # 循环攻击殊死决斗
        while (Hp > 0) and (Mob.HP > 0):
            print('敌方信息:\n', Mob.Name, '\nHP: ', Mob.HP, '\nATK: ', Mob.ATK)
            print('\n我方信息:', '\nHP: ', Hp, '\nATK: ', atk)
            Mob.HP = hero_attack(atk)
            if Mob.HP > 0:
                Hp = mob_attack(Hp)
            else:
                break
            # print(Hp,(Hp and Mob.HP) > 0)
        if Hp > 0:
            print('恭喜你赢得了这场博弈')
            t.sleep(1)
            print('战胜之后，您忽然发现，您的心上人只是一张纸片')
            t.sleep(1)
            print('而您击败了轮回了多次的您自己，却又困于轮回之中，成为了下一个将要被上一个轮回的您击败的boss')
            print('全剧终')
            t.sleep(3)
            print('感谢您的游玩，即将退出游戏')
            t.sleep(1)
            quit()
        else:
            print('胜败乃兵家常事，还请少侠下周目继续吧')
            quit()
    Bosszhan(Canyat.HP,Canyat.ATK)
# Main_Game_Play()