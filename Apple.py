class Apple:
    def __init__(self):
        self.x = 40 * random.randint(0, (width / 40) - 1)
        self.y = 40 * random.randint(0, (height / 40) - 1 )
        self.pos = Vector2(self.x, self.y)
    def draw(self):
        sprite = pg.Rect(self.pos.x, self.pos.y, 40, 40)
        pg.draw.rect(screen, (126,0,0), sprite)
