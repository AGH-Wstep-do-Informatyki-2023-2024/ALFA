class Snake:
    def __init__(self):
        self.x = width // 2
        self.y = height // 2
        self.body = [Vector2(self.x, self.y), Vector2(self.x - 40, self.y)]
        self.direction = Vector2(40,0)
    
    def draw(self):
        for part in self.body:
            sprite = pg.Rect(part.x, part.y, 40, 40)
            pg.draw.rect(screen, (100, 126, 100), sprite)
    
    def move(self):
        next_body = self.body[:-1]
        next_body.insert(0, next_body[0] + self.direction)
        self.body = next_body[:]
