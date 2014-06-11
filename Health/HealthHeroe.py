from Health import Health


class HealthHeroe(Health):
    def __init__(self):
        health = 20
        Health.__init__(self, health, "health")
        self.countDamage = 0
        posX = 0
        posY = 0
        self.setPosition(posX, posY)
        self.animate()

    def animate(self):
        if self.getHealth() == 0:
            self.image = self.images.getImage(self.nameImage + "_null")
        elif self.getHealth() == 20:
            self.image = self.images.getImage(self.nameImage + "_full")
        else:
            self.image = self.images.getImage(self.nameImage + str(self.getHealth()))

    def minusHealth(self):
        if self.isLive():
            if self.countDamage % 5 == 0:
                if self.getHealth() == 1:
                    self.lives = False
                self.countHealth -= 1
            self.countDamage += 1
        self.animate()

