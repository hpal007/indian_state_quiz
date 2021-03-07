import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India State Game")
image = "./images/india_map.gif"
screen.addshape(image)

screen.setup(width=600, height=700)
pointer = turtle.Turtle()
pointer.shape(image)

state_data = pd.read_csv("state_and_co.csv")
all_states = state_data.state.to_list()


def print_all_state():
    p = turtle.Turtle()
    p.hideturtle()
    p.penup()

    for index, row in state_data.iterrows():
        if row["state"] in guessed_state:
            p.goto(row["x"], row["y"])
            p.color("black")
            p.write(row["state"])
        else:
            p.goto(row["x"], row["y"])
            p.color("red")
            p.write(row["state"])
        print(row["state"])


guessed_state = []

while len(guessed_state) < 36:
    answer_state = screen.textinput(title="Guess The State", prompt="Whats the another state's name").title()
    print(answer_state)
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        print_all_state()
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle("circle")
        t.shapesize(2 / 20)
        t.shape()
        t.color('black')
        # t.hideturtle()
        t.penup()
        row_data = state_data[state_data.state == answer_state]
        t.goto(int(row_data.x), int(row_data.y))
        t.write(answer_state)
        print(row_data)

screen.exitonclick()
