from __future__ import annotations
from dataclasses import dataclass, field
from random import randint

@dataclass
class Tank:
    model:str
    armor:int
    health:float
    min_damage:int
    max_damage:int
    damage:int = field(init=False)
    mes:str = field(init=False)
    def __post_init__(self)->None:
        if self.armor>10:self.armor=10
        if self.health>100:self.health=100
        if self.min_damage>10:self.min_damage=10
        if self.max_damage>20:self.max_damage=10
        self.damage=randint(self.min_damage,self.max_damage)
    def print_info(self)->None:
        self.mes = f"«{self.model}» имеет лобовую броню «{self.armor}»"\
                    f"мм. при «{self.health}» ед. здоровья и урон в "\
                    f"«{self.damage}» единиц"
    def shot(self,some_tank:Tank)->None:
        some_tank.health_down(self.damage)
        if some_tank.health<=0:
            self.mes = f"Экипаж танка «{some_tank.model}» уничтожен"
        else:
            self.mes = f"«{self.model}»: Точно в цель, у противника "\
                        f"«{some_tank.model}» осталось «{some_tank.health}»"\
                        f"единиц здоровья"

    def helth_down(self,damage_taken:int)->None:
        self.health-=damage_taken/self.armor
        if self.health>0:
            self.mes = f"«{self.model}»: Командир, по экипажу «{self.model}» "\
                        f"попали, у нас осталось «{self.health}» очков здоровья"
        else:
            self.mes = f"«{self.model}»: Командир, по экипажу «{self.model}» "\
            f"попали, у нас не осталось очков здоровья"