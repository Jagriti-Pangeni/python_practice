# Oops concept practice

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def show(self):
#         print(self.real,"i +",self.img,"j")

#     def __add__(self,num2):
#         adreal=self.real+num2.real
#         adimg=self.img+num2.img
#         return Complex(adreal,adimg)    
    
#     def __sub__(self,num2):
#         adreal=self.real-num2.real
#         adimg=self.img-num2.img
#         return Complex(adreal,adimg)    

# c1=Complex(2,3)
# c2=Complex(4,5) 
# c3=c1+c2
# c3.show()
# c4=c1-c2
# c4.show()


class Railway:
    def __init__(self,name,age,destination):
        self.name=name
        self.age=age
        self.dest=destination

    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Destination:",self.dest)
        print("Ticket price:200")

class Vip(Railway):
    def __init__(self,name,age,destination,food,security):
        super().__init__(name,age,destination)
        self.food=food
        self.security=security

    def show2(self):
        super().show()
        print("Food:",self.food)
        if(self.security=="Yes"):
            print("Security-Included")
            print("Ticket Price:1000")
        else:
            print("Security:Not Included")
            print("Ticet price:500")      

t1=Railway("Jagriti Pangeni",20,"Nawalpur")            
t1.show()
t2=Vip("Jagriti Pangeni",20,"Nawalpur","Thali","Yes")
t2.show2()