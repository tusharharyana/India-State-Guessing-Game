import turtle

screen = turtle.Screen()
screen.setup(width=700,height=800)

screen.title("India State Game")
image = "image/India_states_map.gif"
screen.addshape(image)

turtle.shape(image)

screen.exitonclick()