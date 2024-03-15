class Weapon:
    def __init__(self, bullets: int):               #private method
        self.bullets = bullets                      #instance атрибут е това за всеки bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        # else:                                    #всяка функция by default връща None
        #     return "no bullets left"
        return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
#print(weapon.__dict__)





