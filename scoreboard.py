import turtle as t

class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("courier", 40, "normal"))

        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("courier", 40, "normal"))

    ## **** updates the left score
    def l_point(self):

        self.l_score += 1
        self.update_scoreboard()


    ## **** updates the right score
    def r_point(self):

        self.r_score += 1
        self.update_scoreboard()


    ### **** setting wining match for left player
    # def l_win(self):
    #     if self.l_score >= 5:
    #         self.write(f"PLAYER ONE WON BY {self.l_score}", align="center", font=("courier", 40, "normal"))
    #         return False
    #
    # ### **** setting wining match for right player
    # def r_win(self):
    #     if self.l_score >= 5:
    #         self.write(f"PLAYER TWO WON BY {self.r_score}", align="center", font=("courier", 40, "normal"))
    #         return False