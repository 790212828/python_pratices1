from ez import EZ
from jinx import Jinx
from police import Police
from timo import Timo


class HeroFactory:
    """
    简单工厂模式专门定义一个类来负责创建其他类型的英雄的实例

    1、职责清晰
    2、提供了一个入口。比如添加了新的英雄，其他研发调用代码的过程中，可以以factory为主
    3、不需要一个文件去读写的内容
    """

    def create_hero(self,name):
        if name=="Jinx":
            return Jinx()
        elif name=="EZ":
            return EZ()
        elif name=="Timo":
            return Timo()
        elif name=="Police":
            return Police()
        else:
            raise Exception(f"没有此英雄，不在英雄工厂中")

if __name__ == '__main__':
    hero_factory=HeroFactory()
    jinx=hero_factory.create_hero("Jinx")
    ez=hero_factory.create_hero("EZ")
    jinx.fight(ez.hp,ez.power)

    timo=hero_factory.create_hero("Timo")
    police = hero_factory.create_hero("Police")
    timo.fight(police.hp,police.power)
    police.fight(timo.hp,timo.power)



