class Animal():
     name ='Tom'
     color='black'
     hair='furry'
     legs=4

     def eat(self):
        print('eating')
        
     def get_color(self):
        print(self.color)

     def get_hair(self):
        print(self.hair)


class Dog(Animal):
     name='rocky'

     def bark(self):
       print('barking')  

class Cat(Animal):
    eyes='shining'

    def looks(self):
        print('scary')


obj1=Dog()
print('Dog :')
obj1.name
obj1.eat()
obj1.get_color()
obj1.get_hair()
obj1.bark()

print('Cat :')

obj2=Cat()
obj2.name
obj2.get_color()
obj2.looks()
        
    
      
