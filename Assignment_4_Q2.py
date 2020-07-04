import turtle
import random

dice = [1, 2, 3, 4, 5, 6]

# background
image = "naruto2.gif"
Snake_ladder = turtle.Screen()
Snake_ladder.title("Snake & ladder")
Snake_ladder.setup(700, 580)
Snake_ladder.bgpic("board.gif")
Snake_ladder.addshape(image)

player_one = turtle.Turtle()
player_one.shape(image)
player_one.penup()
player_one.goto(-290, -235)


def condition_check():
    if player_one.pos() == (-58, -235):  # for 3 ladder
        player_one.goto(-58, 113)
    elif player_one.pos() == (174, -235):  # for 5 ladder
        player_one.goto(174, -119)
    elif player_one.pos() == (-174, -119):  # for 11 ladder
        player_one.goto(-174, 229)
    elif player_one.pos() == (174, 113):  # for 20 ladder
        player_one.goto(174, 229)
    elif player_one.pos() == (174, -3):  # for 17 Snake
        player_one.goto(58, -235)
    elif player_one.pos() == (-58, 229):  # for 27 Snake
        player_one.goto(-290, -235)
    elif player_one.pos() == (58, 113):  # for 21 Snake
        player_one.goto(58, -119)
    elif player_one.pos() == (290, 113):  # for 19 Snake
        player_one.goto(290, -119)

    return None


def left():
    player_one.left(90)
    player_one.forward(116)
    player_one.right(90)


while player_one.pos() < (290, 229):

    press = input("press enter for roll th dice")
    di = random.choice(dice)
    print(di)
    for i in range(1, di + 1):
        if player_one.xcor() <= 180 and player_one.ycor() == (-235):  # first row
            player_one.forward(116)

        elif player_one.pos() == (290, -235):  # first row to second row
            left()

        elif player_one.xcor() >= (-180) and player_one.ycor() == (-119):  # second row
            player_one.forward(-116)

        elif player_one.pos() == (-290, -119):  # second row to third row
            left()

        elif player_one.xcor() <= 180 and player_one.ycor() == (-3.0):  # third row
            player_one.forward(116)

        elif player_one.pos() == (290, -3):  # third to fourth row
            left()

        elif player_one.xcor() >= (-180) and player_one.ycor() == 113:  # fourth row
            player_one.forward(-116)


        elif player_one.pos() == (-290, 113):  # 24 block to check direct final or row incrementation

            if di == 6:
                player_one.goto(300, 235)
            else:
                left()


        elif player_one.xcor() == -290 and player_one.ycor() == 229:  # 25 block condition

            if di == 5:

                player_one.goto(300, 235)

            elif di > 5:

                press = input("press enter for roll th dice")

            elif di < 5:

                player_one.forward(116)


        elif player_one.xcor() == -174 and player_one.ycor() == 229:  # 26 block condition

            if di == 4:

                player_one.goto(300, 235)

            elif di > 4:

                press = input("press enter for roll th dice")

            elif di < 4:

                player_one.forward(116)


        elif player_one.xcor() == -58 and player_one.ycor() == 229:  # 27 block condition

            if di == 3:

                player_one.goto(300, 235)

            elif di > 3:

                press = input("press enter for roll th dice")

            elif di < 3:

                player_one.forward(116)


        elif player_one.xcor() == 58 and player_one.ycor() == 229:  # 28 block condition

            if di == 2:

                player_one.goto(300, 235)

            elif di > 2:

                press = input("press enter for roll th dice")

            elif di < 2:

                player_one.forward(116)


        elif player_one.xcor() == 174 and player_one.ycor() == 229:    # 29 block condition

            if di == 1:

                player_one.goto(300, 235)

            elif di > 1:

                press = input("press enter for roll th dice")

            else:

                player_one.forward(116)

    condition_check()
print("You Win the game")
Snake_ladder.exitonclick()
