class Animal():
    def __init__(self, name, speices, age, sound, zoo_name= '---'):
        self.name = name
        self.speices = speices
        self.age = age
        self.sound = sound
        self.zoo_name = zoo_name
        
        
    def make_sound(self):
        print(f"{self.sound}")
        
    def info(self):
        print(f"{self.name}, {self.speices}, {self.age}, {self.sound}, {self.zoo_name}")
        
    def __str__(self):
        p = f'{self.name}, {self.speices}, {self.age}, {self.sound}, {self.zoo_name}'
        return p
        
Anim = Animal("شیر", "پستاندار", 5, "غرش", "مرکزی")
print(Anim.name, Anim.speices, Anim.age, Anim.sound)

Anim.make_sound()

Anim.info()

class Bird(Animal):
    def __init__(self, name, speices, age, sound, wing_span, zoo_name):
        Animal.__init__(self,name, speices, age, sound, zoo_name)
        self.wing_span = wing_span
        

    def make_sound(self):
        print(f"صدای پرنده: {self.sound}")

Bird = Bird("گنجشک", "تخمگذار", 2, "جیکجیک", "شهر", "کوچک")
Bird.info()

print(Anim)