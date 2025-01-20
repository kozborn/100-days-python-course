import turtle
import pandas as pd
screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
img = screen.addshape(image)


turtle.shape(image)

screen.listen()
def get_mouse_coordinates(x, y):
    print(x,y)

states_map = pd.read_csv('50_states.csv')
print(states_map)

screen.onscreenclick(get_mouse_coordinates)

correct_guesses = 0
states_length = len(states_map.index)
guessed_states = []

def write_answer(answer):
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(answer.iloc[0].x, answer.iloc[0].y)
    t.write(answer.iloc[0].state)

while len(guessed_states) < states_length:
    answer_state = screen.textinput(f"States {len(guessed_states)}/{states_length}", "What is another state?").lower()
    if answer_state == "exit":
        break
    result = states_map[states_map['state'].str.lower() == answer_state.strip()]
    if result.empty:
        print("no match")
    elif result.iloc[0].state not in guessed_states:
        guessed_states.append(result.iloc[0].state)
        write_answer(result)


to_learn_df = states_map[~states_map['state'].isin(guessed_states)]
print(to_learn_df)
to_learn_df.to_csv('to_learn_df.csv')







