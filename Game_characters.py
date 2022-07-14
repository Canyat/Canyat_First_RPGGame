import pickle as p
# 创建主角
class Hero:
    t = open('basedata_list.savedata', 'rb')
    t1 = p.load(t)
    t.close()
    ATK = t1[0]
    HP = t1[1]
    WX = t1[2]
    Skill1 = '普通的一拳'
    def skill_one(hp,atk):
        hp -= atk
        return hp
    Skill2 = '认真的一拳'
    def skill_two(hp,atk):
        hp -= atk
        return hp
# 创建怪物
class slime:
    Name = '史莱姆'
    ATK = 5
    HP = 20
    Skill1 = '超级头槌~'
    def skill_one(hp,atk):
        hp -= atk
        return hp
    Skill2 = '果冻攻击'
    def skill_two(hp,atk):
        hp -= atk*1.5
        return hp

class zombie:
    Name = '僵尸'
    ATK = 10
    HP = 50
    Skill1 = '抓挠'
    def skill_one(hp,atk):
        hp -= atk
        return hp
    Skill2 = '小拳拳捶你胸口'
    def skill_two(hp,atk):
        hp -= atk*1.5
        return hp

class skeleton:
    Name = '骷髅'
    ATK = 15
    HP = 65
    Skill1 = '近战普通平A'
    def skill_one(hp,atk):
        hp -= atk
        return hp
    Skill2 = '远程骨头投掷'
    def skill_two(hp,atk):
        hp -= atk*1.5
        return hp

class boss:
    Name = '我自己'
    ATK = 50
    HP = 3000
    Skill1 = '普通的一拳'
    def skill_one(hp,atk):
        hp -= atk
        return hp
    Skill2 = '认真的一拳'
    def skill_two(hp,atk):
        hp -= atk
        return hp


#print(Hero.ATK,Hero.HP,Hero.WX)