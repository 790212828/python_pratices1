from ez import EZ
from hero import Hero


class Jinx(Hero):
    hp=1000
    power=210
    name = "Jinx"
    hero_line = "Jinx 进攻"
    # def fight(self,enemy_hp,enemy_power):
    #     final_hp=self.hp
    #     final_enmey_hp=enemy_hp
    #
    #     final_hp=final_hp-enemy_power
    #     final_enmey_hp=final_enmey_hp-self.power
    #     if final_hp>final_enmey_hp:
    #         print(f"Jinx赢了")
    #     elif final_hp<final_enmey_hp:
    #         print(f"敌人赢了")
    #     else:
    #         print("Jinx和敌人打平手了")


if __name__ == '__main__':
    ez = EZ()
    jinx = Jinx()
    jinx.fight(ez.hp, ez.power)
    ez.fight(jinx.hp,jinx.power)