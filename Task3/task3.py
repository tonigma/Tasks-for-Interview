class Heros:
    def __init__(self, name, vitality, armor, speed, power):
        self.Name = name
        self.Health = vitality * 10
        self.Damage_reduction = armor * 0.06
        self.Attack_time = 0.25 + (2 / speed)
        self.Damage = power * 2

    def get_name(self):
        return self.Name

    def get_damage(self):
        return self.Damage

    def get_damage_reduct(self):
        return self.get_damage_reduct()

    def get_attack_time(self):
        return self.Attack_time

    def set_health(self, dealt_damage):
        self.Health = self.Health - dealt_damage

    def get_healt(self):
        return self.Health

    def print_hero(self):
        print(self.Name,self.Health,self.Damage_reduction,self.Attack_time,self.Damage)
