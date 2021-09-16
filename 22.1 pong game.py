import turtle as t
import paddle
import ball
import scoreboard
import time


screen = t.Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
### ************ create paddle ************* ###

r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))

# *********** create ball *************** ###

ball = ball.Ball()

## ********** create scoreboard class **** ###

scoreboard = scoreboard.Scoreboard()

### ************************************** ####


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_r()

    ## ****** detect collision with wall ****##
    if ball.ycor() > 282 or ball.ycor() < -282:
        ## **** bounce *** ##
        ball.bounce_y()

    #*** detect collision with paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #*** collision at right side of the screen (for game over)

    if ball.xcor() > 380:
        ball.reset_position()
        # if scoreboard.l_score > 5:
        #     tim = t.Turtle()
        #     tim.color("white")
        #     tim.hideturtle()
        #     tim.write(f"PLAYER ONE WON BY {scoreboard.l_score}", align="center", font=("courier", 40, "normal"))
        #     game_is_on = False
        scoreboard.l_point()


    ##**** collision at the left side of the screen

    if ball.xcor() < -380:
        ball.reset_position()
        # if scoreboard.l_score > 5:
        #     tim2 = t.Turtle()
        #     tim2.color("white")
        #     tim2.hideturtle()
        #     tim2.write(f"PLAYER TWO WON BY {scoreboard.r_score}", align="center", font=("courier", 40, "normal"))
        #     game_is_on = False

        scoreboard.r_point()






screen.exitonclick()