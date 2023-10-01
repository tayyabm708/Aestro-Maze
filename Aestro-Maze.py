# importing all the necessary modules...
import winsound
import turtle

freq1 = 700
dur1 = 200

print("Total Lives = 3")
print("Your score is 0")

# setting the window

window = turtle.Screen()
window.bgpic("ex.gif")
window.title("Escape the Maze")
window.setup(700, 700)

# Register shapes

turtle.register_shape("score1.gif")
turtle.register_shape("wall.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("sus1.gif")
turtle.register_shape("sus2.gif")
turtle.register_shape("end1.gif")
turtle.register_shape("win1.gif")


# creating a class named pen for walls..
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("wall.gif")
        self.speed(0)  # maximum speed
        self.penup()


# Title of the game..
t = turtle.Turtle()
t.hideturtle()
t.color("white")
t.penup()
t.goto(0, 305)
t.write("ASTERO MAZE", align="center", font=("Gameplay", 25, "bold"))


# player class
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("sus1.gif")
        self.penup()
        self.speed(0)
        self.gold = 0
        self.lives = 3

    def go_up(self):
        winsound.PlaySound("move.wav", winsound.SND_ASYNC)
        xcord = ditchwitch.xcor()
        ycord = ditchwitch.ycor() + 24

        if (xcord, ycord) not in walls:
            self.goto(xcord, ycord)

        if (xcord, ycord) in treasures1:
            self.goto(xcord, ycord)
            self.gold = self.gold + 100
            treasures1.remove((xcord, ycord))

            score1.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures2:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures2.remove((xcord, ycord))

            score2.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures3:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures3.remove((xcord, ycord))

            score3.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures4:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures4.remove((xcord, ycord))

            score4.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures5:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures5.remove((xcord, ycord))

            score5.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in warning:
            print("Enemy ahead. Be aware!")

        if (xcord, ycord) in bawas:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:
                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:
                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in warning:
            print("Enemy ahead. Be aware!")

        if (xcord, ycord) in bawas1:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:
                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:
                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in bawas2:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:
                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:
                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in bawas3:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:
                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:

                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in yayyy:
            winsound.PlaySound("win.wav", winsound.SND_ASYNC)
            self.goto(0, 0)
            self.shape("win1.gif")
            self.stamp()

            print("You won")

    def go_down(self):
        winsound.PlaySound("move.wav", winsound.SND_ASYNC)
        xcord = ditchwitch.xcor()
        ycord = ditchwitch.ycor() - 24

        if (xcord, ycord) not in walls:
            self.goto(xcord, ycord)

        if (xcord, ycord) in treasures1:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures1.remove((xcord, ycord))

            score1.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures2:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures2.remove((xcord, ycord))

            score2.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures3:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures3.remove((xcord, ycord))

            score3.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures4:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures4.remove((xcord, ycord))

            score4.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures5:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures5.remove((xcord, ycord))

            score5.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in warning:
            print("Enemy ahead. Be aware!")

        if (xcord, ycord) in bawas:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:

                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:
                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in bawas1:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:

                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:
                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in bawas2:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:

                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:
                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in bawas3:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:
                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:

                print("you lost")

                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in yayyy:
            winsound.PlaySound("win.wav", winsound.SND_ASYNC)
            self.goto(0, 0)
            self.shape("win1.gif")
            self.stamp()

            print("You won")

    def go_left(self):
        winsound.PlaySound("move.wav", winsound.SND_ASYNC)
        self.shape("sus2.gif")
        xcord = ditchwitch.xcor() - 24
        ycord = ditchwitch.ycor()

        if (xcord, ycord) not in walls:
            self.goto(xcord, ycord)

        if (xcord, ycord) in treasures1:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures1.remove((xcord, ycord))

            score1.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures2:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures2.remove((xcord, ycord))

            score2.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures3:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures3.remove((xcord, ycord))

            score3.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures4:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures4.remove((xcord, ycord))

            score4.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures5:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures5.remove((xcord, ycord))

            score5.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in warning:
            print("Enemy ahead. Be aware!")

        if (xcord, ycord) in bawas:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:

                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:
                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in bawas1:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:

                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:
                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in bawas2:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:

                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:
                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in bawas3:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:

                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:

                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in yayyy:
            winsound.PlaySound("win.wav", winsound.SND_ASYNC)
            self.goto(0, 0)
            self.shape("win1.gif")
            self.stamp()

            print("You won")

    def go_right(self):
        winsound.PlaySound("move.wav", winsound.SND_ASYNC)
        self.shape("sus1.gif")
        xcord = ditchwitch.xcor() + 24
        ycord = ditchwitch.ycor()

        if (xcord, ycord) not in walls:
            self.goto(xcord, ycord)

        if (xcord, ycord) in treasures1:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures1.remove((xcord, ycord))
            score1.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures2:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures2.remove((xcord, ycord))
            score2.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures3:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures3.remove((xcord, ycord))
            score3.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC )

        if (xcord, ycord) in treasures4:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures4.remove((xcord, ycord))
            score4.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in treasures5:
            self.goto(xcord, ycord)
            self.gold = 100 + self.gold
            treasures5.remove((xcord, ycord))
            score5.goto(2000, -2000)
            print("Your score is", self.gold)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if (xcord, ycord) in warning:
            print("Enemy ahead. Be aware!")

        if (xcord, ycord) in bawas:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:

                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:
                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in bawas1:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:

                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:
                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in bawas2:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:

                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:
                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in bawas3:
            winsound.Beep(freq1, dur1)
            if self.lives > 1:
                self.lives = self.lives - 1
                print("Remaining live = ", self.lives)
                self.goto(org[1])
            else:

                print("you lost")
                winsound.PlaySound("over.wav", winsound.SND_ASYNC)
                self.goto(0, 0)
                self.shape("end1.gif")
                self.stamp()

        if (xcord, ycord) in yayyy:
            winsound.PlaySound("win.wav", winsound.SND_ASYNC)
            self.goto(0, 0)
            self.shape("win1.gif")
            self.stamp()

            print("You won")


# Treasures class

class Treasure(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("score1.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100


# Enemy class

class Enemy(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("enemy.gif")
        self.color("red")
        self.penup()
        self.speed(0)


# finishing point class

class Finish(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("classic")
        self.right(90)
        self.color("orange")
        self.penup()
        self.speed(0)


# creating  a levels list

levels = [""]

# creating a walls list

walls = [""]

# creating a treasures list

treasures1 = [""]
treasures2 = [""]
treasures3 = [""]
treasures4 = [""]
treasures5 = [""]

# creating enemy list

bawas = [""]
bawas1 = [""]
bawas2 = [""]
bawas3 = [""]

# creating end point list

yayyy = [""]

# orginal coordinate of player

org = [""]

# for warning

warning = ["(168,144),(120,144),(144,168),(144,120)"]

# structure of the maze
level_1 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWW",
    "WP     W W W  W    W    W",
    "W   W    W W  W  W   W  W",
    "W W WWW  W    W WWWWWWW W",
    "W W   W WWW WWW W     W W",
    "W W W W         W l   W W",
    "WWW W WWWWWWW WWWWEW    W",
    "W   W    WA W   W  W WWWW",
    "WWWWW    W  W   W  W    W",
    "W   WWW WW WWWWW  WWWWW W",
    "W W      W   W   WW     W",
    "WWW  W   W     W  WWWW  W",
    "W   WWWWWWWWW WW   W W WW",
    "W W WB W    W  WW    W  W",
    "W   W  W  W   WW  WW WW W",
    "W WWW     W W  W  W  W  W",
    "W   WWWWW WWW N   WC W WW",
    "WW  W       WWWW  WWWW  W",
    "W  WW       W  WW  W  W W",
    "W   WWW WWWWWD W  WW    W",
    "W WT W   W     WW  WWW WW",
    "W   e       WWWW  W     W",
    "WWWWWW WWW  W    WWWWW  W",
    "W     M     W           W",
    "WWWWWWWWWWFWWWWWWWWWWWWWW",
]
levels.append(level_1)

# maze turtle (object of pen class)
pointer = Pen()

# player turtle (object of player class)
ditchwitch = Player()

# treasure turtles (objectsof treasure class)
score1 = Treasure()
score2 = Treasure()
score3 = Treasure()
score4 = Treasure()
score5 = Treasure()

# enemy turtles (objects of  enemy class)
bawa = Enemy()
bawa1 = Enemy()
bawa2 = Enemy()
bawa3 = Enemy()

# finish point turtle (object of finish class)
finish = Finish()


def setup(level_1):
    for y in range(len(level_1)):
        for x in range(len(level_1)):

            character = level_1[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # building the maze

            if character == "W":
                pointer.goto(screen_x, screen_y)
                walls.append((screen_x, screen_y))
                pointer.stamp()

            # adding the player

            if character == "P":
                ditchwitch.goto(screen_x, screen_y)
                org.append((screen_x, screen_y))

            # adding treasures

            if character == "A":
                score1.goto(screen_x, screen_y)
                treasures1.append((screen_x, screen_y))
            if character == "B":
                score2.goto(screen_x, screen_y)
                treasures2.append((screen_x, screen_y))
            if character == "C":
                score3.goto(screen_x, screen_y)
                treasures3.append((screen_x, screen_y))
            if character == "D":
                score4.goto(screen_x, screen_y)
                treasures4.append((screen_x, screen_y))
            if character == "T":
                score5.goto(screen_x, screen_y)
                treasures5.append((screen_x, screen_y))

            # adding the enemies

            if character == "E":
                bawa.goto(screen_x, screen_y)
                bawas.append((screen_x, screen_y))
            if character == "N":
                bawa1.goto(screen_x, screen_y)
                bawas1.append((screen_x, screen_y))
            if character == "e":
                bawa2.goto(screen_x, screen_y)
                bawas2.append((screen_x, screen_y))
            if character == "M":
                bawa3.goto(screen_x, screen_y)
                bawas3.append((screen_x, screen_y))

            if character == "l":
                warning.append((screen_x, screen_y))

            # adding the finishing point

            if character == "F":
                finish.goto((screen_x, screen_y))
                yayyy.append((screen_x, screen_y))


# Here we are calling the function to set up  the maze
setup(levels[1])

# linking the movement of the turtle with the keyboard
turtle.listen()
turtle.onkey(ditchwitch.go_left, "Left")
turtle.onkey(ditchwitch.go_right, "Right")
turtle.onkey(ditchwitch.go_up, "Up")
turtle.onkey(ditchwitch.go_down, "Down")
