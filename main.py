import turtle
import pandas as pd

# Setup screen
screen = turtle.Screen()
screen.setup(width=700,height=800)
screen.title("India State Game")
image = "image/India_states_map.gif"
screen.addshape(image)
turtle.shape(image)

#Load state data
data = pd.read_csv("28_states.csv")
all_states = data.state.to_list()
guessed_state = []

# Function to draw a yellow box behind the state name
def draw_yellow_box(t, x, y, width=100, height=20):
    t.penup()
    t.goto(x - width / 2, y + height / 2)  # Move to top-left corner of the rectangle
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.penup()

while len(guessed_state) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/28 States Correct",prompt="What's another state's name?").title()
    # answer_state = ' '.join(word.capitalize() for word in answer_state.split()) #title() function work same here
    if answer_state == "Exit":
        for index, row in data.iterrows():
            if row['state'] not in guessed_state:
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                x, y = row['x'],row['y']
        
                # Draw yellow box behind the state name
                draw_yellow_box(t, x, y)

                # Write the state name on top of the box
                t.goto(x, y -7)  # Adjusting y-position slightly to center the text
                t.write(row['state'], align="center", font=("Arial", 8, "normal"))
            
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        
        # Get the coordinates for the state
        state_data = data[data.state == answer_state]
        x, y = state_data.x.item(), state_data.y.item()
        
        # Draw yellow box behind the state name
        draw_yellow_box(t, x, y)

        # Write the state name on top of the box
        t.goto(x, y - 10)  # Adjusting y-position slightly to center the text
        t.write(state_data.state.item(), align="center", font=("Arial", 8, "normal"))
        
    else:
        screen.textinput(title="Invalid Input", prompt="State not recognized or already guessed. Try again. [Click Ok]")


"""
#To get co-ordinates on India map.
def get_mouse_click_coor(x, y):
    print(x, y)
    
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
"""


screen.exitonclick()