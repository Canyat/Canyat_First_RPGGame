import random as r
import time as t
import pickle

#等待函数
def wait():
    t.sleep(1)
# 初始数据选择系统
def base_data_cho():
    atk = r.randint(1,10)
    hp = r.randint(1,10)
    wx = r.randint(1,10)
    print('您的攻击力初始值是：',atk,'\n','您的生命力初始值是：',hp,'\n','您的悟性值为：',wx,'\n ')
    re = input('您是否满意该数值？（Y/N）:')
    if re == 'Y':
        #储存进度
        basedata_list = []
        basedata_list.append(atk)
        basedata_list.append(hp)
        basedata_list.append(wx)
        pickle_file = open('basedata_list.savedata','wb')
        pickle.dump(basedata_list,pickle_file)
        pickle_file.close()

        import Main_Game as M
        #开始游戏
        print('您是一位时空旅者，拥有轮回的能力')
        wait()
        print('您的心上人被抓到了塔上，您需要去救她')
        wait()
        print('于是，您开启了征程')
        M.Main_Game_Play()

    elif re == 'N':
        print('正在为您重新投胎……\n')
        t.sleep(2)
        base_data_cho()
    else:
        print('你是不是输入错啦，那我们再来一次!')
        t.sleep(2)
        base_data_cho()
# 让玩家选择新游戏还是读取存档下一周目
startgame = input("输入 1 新的游戏，输入 2 读取存档：")
# 进入启动器主程序
if startgame == '1':
    print('游戏开始,请选择您的初始数值~\n ')
    wait()
    print('初始数值中的Y/N强迫性大写哦~\n(绝对不是帅比游戏作者偷懒不想打代码qwq)\n ')
    wait()
    base_data_cho()
# 读取基础存档信息
elif startgame == '2':
    import Main_Game as M
    pickle_file = open('basedata_list.savedata', 'rb')
    my_basedata = pickle.load(pickle_file)
    # print(my_basedata)
    print('啊，又是一次轮回')
    M.Main_Game_Play()
# 好耶，玩家开始皮了
else:
    print('又调戏我？qwq哼，不理你了！')
    count1 = 6
    while count1 > 0:
        count1 -= 1
        print('哼唧')