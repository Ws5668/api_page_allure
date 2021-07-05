class Bicycle:

    model = "26"

    def run(self,km):
        print(f"用脚骑行了 {km}公里")


class EBicycle(Bicycle):

    #如果属性需要传参定义，需要写在构造函数中
    def __init__(self,valume):
        #电动车目前的电量
        self.valume = valume

    #充电方法
    def fill_charge(self,vol):
        self.valume = self.valume + vol
        if self.valume <= 30:
            print(f"充了{vol}度电，目前电量为{self.valume}")
        else:
            raise Exception("充电太多，装不下！")
    def run(self,km):
        power_km = self.valume * 10
        if power_km >= km:
            print(f"用电力骑行了{km}公里")
        else:
            print(f"用电力骑行了{power_km}公里，没电啦!")
            #直接调用父类方法
            #Bicycle().run(km - power_km)
            #或者利用继承关系调用父类方法
            super().run(km - power_km)


if __name__ == "__main__":
    bike = Bicycle()
    bike.run(300)
    ebike = EBicycle(10)
    ebike.fill_charge(20)
    ebike.run(1000)