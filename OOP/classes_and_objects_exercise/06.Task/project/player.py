from typing import Dict


class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str, int] = {}  # {"fireball": 10} key = skill, value = mana_cost
        self.guild = "Unaffiliated"

    def add_skill(self, skill, mana_cost):
        if self.skills.get(skill, 0):
            return "Skill already added"

        self.skills[skill] = mana_cost
        return f"Skill {skill} added to the collection of the player {self.name}"

    def player_info(self):
        skills_str = "\n".join(f"==={skill} - {mana_cost}" for skill, mana_cost in self.skills.items())
        return (f"Name: {self.name}\n"
                f"Guild: {self.guild}\n"
                f"HP: {self.hp}\n"
                f"MP: {self.mp}\n"
                f"{skills_str}")