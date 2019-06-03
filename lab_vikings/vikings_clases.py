# Project lab-data-vikings
import random


# Soldier (constructor, ataque y daño)
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receive_damage(self, damage):
        self.health -=damage

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
        

    def receive_damage(self, damage):
        super().receive_damage(damage)
        if self.health <= 0:
            return self.name + " has died in act of combat"
        else:
            return self.name + " has received " + str(damage) + " points of damage"

    def battle_cry(self):
        return "Odin Owns You All!"
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receive_damage(self, damage):
        super().receive_damage(damage)
        if self.health <= 0:
            return "A Saxon has died in combat"
        else:
            return "A Saxon has received " + str(damage) + " points of damage"

# War
class War:
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []


    def add_viking(self, viking):
        self.viking_army.append(viking)

    def add_saxon(self, saxon):
        self.saxon_army.append(saxon)

    def viking_attack(self):
        # attacked_saxon = self.saxon_army[random.randint(0, len(self.saxon_army)-1)]
        attacked_saxon = random.choice(self.saxon_army)
        attacker_viking = random.choice(self.viking_army)
        return attacked_saxon.receive_damage(attacker_viking.strength)
        if attacked_saxon.health == 0:
            self.saxon_army.remove(attacked_saxon)

    def saxon_attack(self):
        attacker_saxon = random.choice(self.saxon_army)
        attacked_viking = random.choice(self.viking_army)
        return attacked_viking.receive_damage(attacker_saxon.strength)
        if attacked_viking.health == 0:
            self.viking_army.remove(attacked_viking)


    def show_status(self):
        if len(self.saxon_army) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.viking_army) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
