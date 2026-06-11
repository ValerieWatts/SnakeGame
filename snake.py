from turtle import Turtle

class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.snake_blocks = []

        for i in range(3):
            piece = self.piece()

            self.snake_blocks.append(piece)
            piece.setpos(self.x, self.y)
            self.x -= 20

    def piece(self):
        snake_piece = Turtle(shape="square")
        snake_piece.color("white")
        snake_piece.penup()
        return snake_piece

    def grow(self):
        new_piece = self.piece()
        new_piece.setpos(self.snake_blocks[-1].pos())
        self.snake_blocks.append(new_piece)


    def move(self):

        head = self.snake_blocks[0]
        head.color("lightblue")

        def move_up():
            if head.heading() != 270:
                head.setheading(90)

        def move_left():
            if head.heading() != 0:
                head.setheading(180)

        def move_right():
            if head.heading() != 180:
                head.setheading(0)

        def move_down():
            if head.heading() != 90:
                head.setheading(270)

        self.screen.listen()
        self.screen.onkey(fun=move_up, key="w")
        self.screen.onkey(fun=move_left, key="a")
        self.screen.onkey(fun=move_right, key="d")
        self.screen.onkey(fun=move_down, key="s")

        for i in range(len(self.snake_blocks) - 1, 0, -1):
            self.snake_blocks[i].setpos(self.snake_blocks[i - 1].pos())

        head.forward(20)
