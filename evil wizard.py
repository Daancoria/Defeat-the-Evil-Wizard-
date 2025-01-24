import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {amount} points! Current health: {self.health}/{self.max_health}")        

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  
        
    #We added a power attack method 
    def power_attack(self, opponent):
        damage = random.randint(self.attack_power * 2 - 10, self.attack_power * 2 + 10)
        opponent.health -= damage
        print(f"{self.name} uses a power attack on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def heal(self,amount):
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {amount} points! Current health: {self.health}/{self.max_health}")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power
        self.invulnerable = False
        
    # Cast spell method here
    def cast_spell(self,opponent):
        damage = random.randint(self.attack_power * 3 - 15, self.attack_power * 3 + 15)
        opponent.health -= damage
        print(f"{self.name} cast a spell on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
     #Ability        
    def teleport(self):
        self.invulnerable = True
        print(f"{self.name} teleported for 1 turn!")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=40)  
        self.invulnerable = False
        
    def quick_shot(self,opponent):
        damage = random.randint(self.attack_power * 2 - 10, self.attack_power * 2 + 10)
        opponent.health -= damage
        print(f"{self.name} performs a quick shot on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def evade(self):
        self.invulnerable = True
        print(f"{self.name} evaded the attack!")

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health= 160, attack_power=20)     
        self.invulnerable = False
        
    def holy_strike(self,opponent):
        damage = random.randint(self.attack_power * 2 - 10, self.attack_power * 2 +10)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} with holy strike for {damage} damage!")
        if opponent.health <= 0:
            print(f"{self.name} has been defeated!")
    
    def divine_shield(self):
        self.invulnerable = True
        print(f"{self.name} uses divine shield to block the following attack!")       

# Rogue class (inherits from Character)
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health= 110, attack_power=30)
        self.invulnerable = False

    def backstab(self,opponent):
        damage = random.randint(self.attack_power * 2 - 10, self.attack_power * 2 +10)
        opponent.health -= damage
        print(f"{self.name} backstabs {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def shadow_dodge(self):
        self.invulnerable = True
        print(f"{self.name} uses shadow dodge to avoid the next attack!")       

#Necromancer class (inherits from Character)
class Necromancer(Character):
    def __init__(self, name):
        super().__init__(name, health= 140, attack_power= 15)
        self.invulnerable = False
        
    def summon_minions(self):
        self.invulnerable = True
        print(f"{self.name} summons minions to use as shields!")
    
    def leech_seed(self,opponent):
        damage = random.randint(self.attack_power * 3 - 15, self.attack_power * 3 + 15)
        opponent.health -= damage
        self.health += damage // 2
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} drains life points from {opponent.name} for {damage} damage and heals for {damage // 2} points!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")                        

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  
        
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def attack(self, opponent):
        if isinstance(opponent, Mage) and opponent.invulnerable:
            print(f"{self.name} couldn't attack due to teleport!")
            opponent.invulnerable = False
            
        elif    isinstance(opponent, Archer) and opponent.invulnerable:
                print(f"{self.name} couldn't attack due to evade!")
                opponent.invulnerable = False
            
        elif    isinstance(opponent, Paladin) and opponent.invulnerable:
                print(f"{self.name} couldn't attack due to divine shield!")
                opponent.invulnerable = False
                
        elif    isinstance(opponent, Rogue) and opponent.invulnerable:
                print(f"{self.name} couldn't attack due to shadow dodge!")
                opponent.invulnerable = False
                
        elif    isinstance(opponent, Necromancer) and opponent.invulnerable:
                print(f"{self.name} attacks the minions instead of {opponent.name}!")
                opponent.invulnerable = False        
        else:
            damage = random.randint(self.attack_power * 2 - 5, self.attack_power * 2 -5)
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} with a fire blast for {damage} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  
    print("4. Paladin")  
    print("5. Rogue")
    print("6. Necromancer")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    elif class_choice == '5':
        return Rogue(name)
    elif class_choice == '6':
        return Necromancer(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player,Warrior):
                player.power_attack(wizard)
                player.heal(5)
            elif isinstance(player, Mage):
                player.cast_spell(wizard)
                player.teleport()
            elif isinstance(player, Archer):
                player.quick_shot(wizard)
                player.evade()
            elif isinstance(player, Paladin):
                player.divine_shield()
                player.holy_strike(wizard)
            elif isinstance(player, Rogue):
                player.backstab(wizard)
                player.shadow_dodge()
            elif isinstance(player, Necromancer):
                player.summon_minions() 
                player.leech_seed(wizard)    
        elif choice == '3':
            player.heal(15)            
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()
    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")
    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()