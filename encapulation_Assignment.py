

class ChickenCoup: 
    def __init__(self):
        self.eggs = 0 #standard variable
        self._chickens = 5 #private variable
        self.__roosters = 1 #Protected variable

    def getRoosters(self):  #method to get the value of protected variable
        print(self.__roosters) 

    def setRoosters(self, private): #method to change the value of protected variable
        self.__roosters = private



if __name__ == '__main__':
    coup = ChickenCoup()  #create object
    print(coup.eggs) #print the standard variable
    print(coup._chickens)#print the private variable
    coup.getRoosters() #print the protected variable
    coup.setRoosters(2)#set the protected variable
    coup.getRoosters() #print the protected variable
