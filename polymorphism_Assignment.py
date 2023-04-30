#Class Weapon, it has a name and a size
class Weapon:
    name = 'weapon'
    size = 'medium'

    def attack(self):
        msg = '\nThe {} {} is weilded at the opponent.'.format(self.size, self.name)
        print(msg)#print the msg

#Child class Bow, it has a string type and ammunition
class Bow(Weapon):
    name = 'Bow'
    string_type = 'nylon'
    ammo = 'arrow'

    def attack(self): #polymorphism, override the attack method
        msg = '\nThe {} is fires {}s at the opponent.'.format(self.name, self.ammo)
        print(msg)#print the msg

#Child class Sword, it has a length and a material
class Sword(Weapon):
    name = 'Sword'
    length = '4'
    material = 'Steel'

    def attack(self): #polymorphism, override the attack method
        msg = '\nThe {} {} is {} feet long. The pointy end goes towards the opponent.'.format(self.material, self.name, self.length)
        print(msg) #print the msg


if __name__ == '__main__':
    #instanciate each class 
    weapon = Weapon()
    bow = Bow()
    sword = Sword()
    #call methods
    weapon.attack()
    bow.attack()
    sword.attack()
