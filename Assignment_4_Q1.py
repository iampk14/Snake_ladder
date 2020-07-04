import turtle
import random

Race_game = turtle.Screen()
Race_game.title("Race Game")
dice = [1, 2, 3, 4, 5, 6]

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-400, 100)

player_one.goto(400, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-400, 100)

player_two = player_one.clone()
player_two.color("red")
player_two.penup()
player_two.goto(-400, -100)

player_two.goto(400, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-400, -100)

for i in range(20):
    if player_one.pos() >= (380, 100):
        print("Player one Wins the game")
        break
    elif player_two.pos() >= (380, -100):
        print("Player two Wins the game")
        break
    else:
        player_one_turn = input("\nRoll the dice")
        dice_result = random.choice(dice)
        print("The result of the die roll is: ")
        print(dice_result)
        print("The number of steps will be: ")
        print(20 * dice_result)
        player_one.fd(20 * dice_result)
        player_two_turn = input("\nRoll the dice")
        dice_result2 = random.choice(dice)
        print("The result of the die roll is: ")
        print(dice_result2)
        print("The number of steps will be: ")
        print(20 * dice_result2)
        player_two.fd(20 * dice_result2)
Race_game.exitonclick()
