from Air import Air


class FireBall(Air):
    def __init__(self):
        nameImage = "fireBall"
        width = 32
        height = 20
        step = 10
        Air.__init__(self, nameImage, step, width, height)

