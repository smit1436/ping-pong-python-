from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

        ##**** increase the movement speed
        self.move_speed = 0.1

    ##*** ball will move to other left after every point
    def move_r(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    ##*** ball will move to other right after every point
    def move_l(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(-new_x, new_y)

    ##*** bounce or change the y-direction so when ball collides with upper and bottom border it bounces off
    def bounce_y(self):

        self.y_move *= -1

    ## *** changes the x-direction so when ball collides with paddle it moves to the other player
    def bounce_x(self):

        self.x_move *= -1
        self.move_speed *= 0.7

    ##*** reset position of the ball
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()