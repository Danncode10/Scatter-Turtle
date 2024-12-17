import turtle
from turtle import Turtle, Screen
import random as r

def enter_user_bet():
    global user_bet  # Use the global variable
    while True:
        user_bet = screen.textinput(
            title="Make your bet",
            prompt="Which turtle will win the race (purple, blue, green, yellow, orange, red): "
        )
        if user_bet in ['purple', 'blue', 'green', 'yellow', 'orange', 'red']:
            break  # Valid input
        print("Invalid Input!")

def starting_position():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    global turtle_list

    # distance_between turtle is 33
    d = 33
    for i in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(-230, -100 + (d * i))
        turtle_list.append(new_turtle)

def start_race():
    global turtle_list, place
    place_size = 0
    while True:
        for turtle in turtle_list:
            if(turtle.xcor() > 230):
                # # print(turtle.color()) => returns a tuple, ('purple', 'purple'), instead, use pencolor()
                # print(f"Winner: {turtle.pencolor()}")
                # # break => doesnt stop the while True loop
                # return
 
                #remove turtle that is already in place so that it will not loop back
                turtle_list.remove(turtle)

                place.append(turtle.pencolor())
                place_size+= 1

                if(place_size == 6):
                    return

            turtle.forward(r.randint(0,10))

def showWinner():
    winner = place[0]
    print(f"The Winner is {winner}")
    i = 0
    for color in place:
        i += 1
        print(f"{i}: {color}")

    return winner

def compareWinner(winner):
    if(user_bet == winner):
        print("You Won!")
    else:
        print("You Lose!")


def main():
    enter_user_bet()
    print(f"Your bet: {user_bet}") #prints in Console
    starting_position()
    start_race()
    winner = showWinner()
    compareWinner(winner)

#global var
screen = Screen()
user_bet = ""
turtle_list = []
place = []

#Call main
screen.setup(width = 500, height = 400)
main()
screen.mainloop()


'''Commit
'''
