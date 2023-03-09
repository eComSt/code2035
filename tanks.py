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
    