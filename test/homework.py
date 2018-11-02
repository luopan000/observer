# 通知者类  前台小姐
class Receptionist:
    def __init__(self):
        # 通知者需要通知人的列表和自己的状态
        self.observers = []
        self.status = ''
    def survey(self,observer):
        # 将观察者放入观察列表
        self.observers.append(observer)
    def notify(self):
        # 时刻将信息传入观察者
        for observer in self.observers:
            # 通知者使得观察者执行更新行动的方法
            observer.update()

class StockObserve:
    def __init__(self,name,reception):
        self.name = name
        self.reception = reception
    def update(self):
        if self.reception.status == '老板来了!':
            print("{0},停止玩游戏!".format(self.name))
        if self.reception.status == '':
            print("不慌,老板在和小蜜约会,继续玩!")


if __name__ == '__main__':
    # 创建通知者对象
    mrs = Receptionist()
    # 创建观察者对象
    a = StockObserve('a',mrs)
    b = StockObserve('b',mrs)
    # 将观察者加入通知者的通知列表
    mrs.survey(a)
    mrs.survey(b)

    # 开始监测 时刻通知

    mrs.status = '老板来了!'
    mrs.notify()





