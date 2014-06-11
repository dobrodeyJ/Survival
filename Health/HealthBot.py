from Health import Health


class HealthBot(Health):
    def __init__(self, health):
        Health.__init__(self, health, "zombie_health")
        self.animate()

    def animate(self):
        if self.getHealth() == 0:
            self.image = self.images.getImage(self.nameImage + "_null")
        elif self.getHealth() == 1:
            self.image = self.images.getImage(self.nameImage + "_1")
        elif self.getHealth() == 2:
            self.image = self.images.getImage(self.nameImage + "_2")
        elif self.getHealth() == 3:
            self.image = self.images.getImage(self.nameImage + "_full")