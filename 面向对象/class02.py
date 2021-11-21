# 花猫应用
class Cat:
    type = '猫'

    # 属性初始化
    def __init__(self, nickname, age, color):
        self.nickname = nickname
        self.age = age
        self.color = color

    # 方法(动作)
    def eat(self, food):
        print('{}喜欢吃{}'.format(self.nickname, food))

    def catch_mouse(self, color, weight):
        print('{},抓了一只{}kg的,{}的大老鼠'.format(self.nickname, weight, color))

    def sleep(self, hour):
        if hour < 5:
            print('继续睡觉！')
        else:
            print('活动活动！')

    def show(self):
        print('猫咪叫做{},{}岁了,颜色是{}')


# 创建对象
cat1 = Cat('花花', 2, '黑色')
# 通过对象调用方法
cat1.catch_mouse('黑色', 2)
cat1.sleep(8)
cat1.eat('鱼')
cat1.show()
