class PlayerCharacter: #create class Player character
    name = 'Name not entered' #Name of the character
    HP = 10 #Health points of the character

class Warrior(PlayerCharacter): #create child class Warrior
    weaponSpecialty: 'Sword' #Feature of warrior class, weapon specialty
    armorClass: 2 #Feature of warrior class, how tough are they?

class Mage(PlayerCharacter): #create child class Mage
    signitureSpell: 'Fireball' #Feature of Mage class, signature spell attack
    magicDefense: 2 #Feature of Mage class, defense against magic attacks
