import random


class Hero:


    def __init__(self,name,hp,power):
        #初始化英雄的基本属性
        self.my_name = name
        self.my_hp = hp
        self.my_power = power

    #打斗方法
    def fight(self,enemy_name,enemy_hp,enemy_power):
        #比赛结果
        result = ""

        #循环打斗
        while True:
            #一轮打斗
            self.my_hp = self.my_hp - enemy_power
            enemy_hp = enemy_hp - self.my_power
            print(f"己方{self.my_name}的血量为:{self.my_hp},敌方{enemy_name}的血量为:{enemy_hp}")
            #判断输赢
            if self.my_hp > enemy_hp:
                result = "我方获胜"
            elif enemy_hp > self.my_hp:
                result = "敌方获胜"
            else:
                result = "平局"

            if enemy_hp <= 0 or self.my_hp <= 0:
                break
        return result

class HouYi(Hero):
    def __init__(self,name,hp,power):
        self.defense = 100
        super().__init__(name,hp,power)


    def fight(self, enemy_name, enemy_hp, enemy_power):
    # 比赛结果
        result = ""

    # 循环打斗
        while True:
        # 一轮打斗
            self.my_hp = self.my_hp + self.defense - enemy_power
            enemy_hp = enemy_hp - self.my_power
            print(f"己方{self.my_name}的血量为:{self.my_hp},敌方{enemy_name}的血量为:{enemy_hp}")
        # 判断输赢
            if self.my_hp > enemy_hp:
                result = "我方获胜"
            elif enemy_hp > self.my_hp:
                result = "敌方获胜"
            else:
                result = "平局"

            if enemy_hp <= 0 or self.my_hp <= 0:
                break
        return result

if __name__ == '__main__':
    #定义英雄属性值
    EZ_hp = 1000
    EZ_power = 190
    # Jinx_hp = 1000
    # Jinx_power = 190
    hp = [x for x in range(990,1010)]
    Jinx_hp = random.choice(hp)
    print(Jinx_hp)
    Jinx_power = random.randint(190,210)
    print(Jinx_power)
    #实例化英雄
    # ez = Hero("EZ",EZ_hp,EZ_power)
    # #调用打斗方法
    # r = ez.fight("Jinx",Jinx_hp,Jinx_power)
    # #打印比赛结果
    # print(r)

    houyi = HouYi("后裔",990,220)
    r = houyi.fight("Jinx",Jinx_hp,Jinx_power)
    print(r)

