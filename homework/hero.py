

class Hero:

    hp=0
    power=0
    name=""
    hero_line=""
    def fight(self,enemy_hp,enemy_power):
        """
        两方进行一回合制对打
        :param enemy_hp:敌人的血量
        :param enemy_power:敌人的攻击力
        :return:
        """
        final_hp=self.hp
        final_enmey_hp=enemy_hp
        final_hp=final_hp-enemy_power
        final_enmey_hp=final_enmey_hp-self.power

        self.speak_lines()

        if final_hp>final_enmey_hp:
            print(f"{self.name}赢了")
        elif final_hp<final_enmey_hp:
            print(f"敌人赢了")
        else:
            print(f"双方打成平手了")

    def speak_lines(self):
        print(f"{self.name}:{self.hero_line}")

