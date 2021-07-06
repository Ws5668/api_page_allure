class Animal:


    def __init__(self ,name ,color ,age ,gender):
        self.animal_name = name
        self.animal_color = color
        self.animal_age = age
        self.animal_gender = gender

    def jiao(self):
        print(f"这只{self.animal_name},是{self.animal_color}颜色的,今年{self.animal_age}岁,性别是:{self.animal_gender} 它会叫~")

    def run(self):
        print(f"这只{self.animal_name},是{self.animal_color}颜色的,今年{self.animal_age}岁,性别是:{self.animal_gender} 它会跑~")


class Cat(Animal):
    def __init__(self,name,color,age,gender,hair):


        super().__init__(name,color,age,gender)
        self.hair = hair


    def zhuo_mouse(self):
        print(f"这只{self.animal_name}是{self.animal_color}色{self.hair}的，今年{self.animal_age}岁，性别是:{self.animal_gender},并且会抓老鼠。")

    def jiao(self):
        print(f"这只{self.animal_name}是{self.animal_color}色{self.hair}的，今年{self.animal_age}岁，性别是:{self.animal_gender},发出喵喵的叫声。")

class Dog(Animal):
    def __init__(self,name,color,age,gender,hair):

        super().__init__(name,color,age,gender)
        self.hair = hair


    def kan_jia(self):
        print(f"这只{self.animal_name}是{self.animal_color}色{self.hair}的，今年{self.animal_age}岁，性别是:{self.animal_gender},并且会看家。")

    def jiao(self):
        print(f"这只{self.animal_name}是{self.animal_color}色{self.hair}的，今年{self.animal_age}岁，性别是:{self.animal_gender},并且会汪汪叫。")

if __name__ == "__main__":

    mao = Cat("猫" , "黑" , 3 , "雄性" , "短毛")
    mao.run()
    mao.zhuo_mouse()
    mao.jiao()


    gou = Dog("狗" , "黄" , 2 , "雌性" , "长毛")
    gou.run()
    gou.kan_jia()
    gou.jiao()








