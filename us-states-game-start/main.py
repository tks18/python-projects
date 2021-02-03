import turtle

screen = turtle.Screen()
screen.title("US States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput("Guess the State", "Enter a Name")
print(answer_state)
