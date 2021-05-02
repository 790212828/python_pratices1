from hero import Hero


class EZ(Hero):
    hp=1100
    power=190
    name = "EZ"
    hero_line = "EZ 进攻"
    # def fight(self,enemy_hp,enemy_power):
    #     """
    #     两方进行一回合制对打
    #     :param enemy_hp:敌人的血量
    #     :param enemy_power:敌人的攻击力
    #     :return:
    #     """
    #     final_hp=self.hp
    #     enemy_final_hp=enemy_hp
    #     #通过实例变量（self.xx）获取到类变量(hp或者power)
    #     final_hp=final_hp-enemy_hp
    #     enemy_final_hp=enemy_final_hp-self.power
    #     if final_hp>enemy_final_hp:
    #         print(f"ez赢了")
    #     elif final_hp<enemy_final_hp:
    #         print(f"敌人赢了")
    #     else:
    #         print(f"我们打平手了")
