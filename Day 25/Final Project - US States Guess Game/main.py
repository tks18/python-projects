import turtle
import pandas

screen = turtle.Screen()
state_data = pandas.read_csv("50_states.csv")
screen.title("US States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

score = 0
while score != 50:
    answer_state = screen.textinput(f"{score}/50 Correct", "Enter a State Name").title()
    if answer_state.lower() == "exit":
        break
    guess = state_data[state_data.state == answer_state.title()]
    if guess.size != 0:
        guessed_states.append(answer_state)
        score += 1
        textWriter = turtle.Turtle()
        textWriter.hideturtle()
        textWriter.pu()
        textWriter.goto(float(guess.x), float(guess.y))
        textWriter.write(guess.state.item(), move=False, align='center')

list_data = state_data.state.to_list()
missed_data = [state for state in list_data if state not in guessed_states]

new_data = pandas.DataFrame(missed_data)
new_data.to_csv("State to Learn.csv")
print(missed_data)
