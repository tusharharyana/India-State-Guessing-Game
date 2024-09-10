import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=700,height=800)

screen.title("India State Game")
image = "image/India_states_map.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("28_states.csv")
all_states = data.state.to_list()
guessed_state = []


while len(guessed_state) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/28 States Correct",prompt="What's another state's name?").title()
    # answer_state = ' '.join(word.capitalize() for word in answer_state.split()) #title() function work same here
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())



"""
#To get co-ordinates on India map.
def get_mouse_click_coor(x, y):
    print(x, y)
    
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
"""


screen.exitonclick()