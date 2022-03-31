# Encapsulacion: Es el proceso de mantener lo datos y metodos  juntos como una unidad:
# Ventajas de la emcapsulacion:
    # Las clases hacen que el codigo sea facil de cambiar y mantener 
    # Las propiedades que se ocultará se pueden especificar facilemnte.
    # Las clases o funciones externas pueden acceder a las propiedades 

from msilib.schema import Class
from unicodedata import name


class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display_user(self):
        print("User Name is: ",self.name)
        print("User age is: ",self.age)

user1 = User("Jhon Doe", 35)

#llamado al metodo de la clase
user1.display_user()

#accediendo directamente de las variables
user1.name
user1.age

print()
print(">>>>>>>>>>>>>")
print()
#user1._User__age

class Robot:
    def __init__(self,):
        self.a = 123 # atributo de acceso publico 
        self._b = 456 #atributo de acceso protegido 
        self._Robot__c = 789  # atributo de acceso privado    
        
        # No se pued self. __c
        
yorobot = Robot()

print(yorobot.a)
print(yorobot._b)
print(yorobot._Robot__c)

#class Car:
#    maxspeed = 0
#    name = ""
    
#    def __init__(self):
#        self.maxspeed = 200
#        self.name = "SuperCar"
        
#    def drive(self):
#        print("drivind maxspeed",self.__maxspeed)
    
#    def setMaxSpeed(self,speed):
#        self.__maxspeed = speed
        
#bluecar = Car()
#bluecar.drive()
#bluecar