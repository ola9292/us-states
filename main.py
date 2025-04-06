import turtle
import pandas
screen = turtle.Screen()
screen.title = "US states game"
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

no_of_guess = 0
data = pandas.read_csv('50_states.csv')
states_guessed = []

while no_of_guess < len(data['state']):
    answer_state = screen.textinput(title=f"{no_of_guess}/{len(data['state'])} Guess the state", prompt="What's another state's name? ")
    answer_state_cap = answer_state.title()
    if answer_state_cap == "Exit":
        arr_csv = list(set(data.state) - set(states_guessed))
        missed_states_data = pandas.DataFrame(arr_csv)
        missed_states_data.to_csv('states_to_learn.csv')
        break
    if answer_state != "":  
        for state in data.state:
            if answer_state_cap == state:
                guess_state = data[data.state == answer_state_cap]
                x_coord = guess_state['x'].iloc[0]
                y_coord = guess_state['y'].iloc[0]
                pen.goto(x_coord, y_coord)
                pen.write(answer_state_cap, align="center", font=("Arial", 8, "normal"))
                states_guessed.append(answer_state_cap)
        no_of_guess += 1
        
        
        
# screen.exitonclick()


