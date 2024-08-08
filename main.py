import turtle
import pandas

screen = turtle.Screen()
screen.title("Portugal Districts Game")
image = "portugal_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("districts.csv")
all_districts = data.district.to_list()
guessed_districts = []

while len(guessed_districts) < 18:
    answer_district = screen.textinput(title=f"{len(guessed_districts)}/18 Districts Correct",
                                    prompt="What's another district name?").title()

    if answer_district == "Exit":
        missing_districts = [district for district in all_districts if district not in guessed_districts]
        new_data = pandas.DataFrame(missing_districts)
        new_data.to_csv("districts_to_learn.csv")
        break

    if answer_district in all_districts:
        guessed_districts.append(answer_district)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        district_data = data[data.district == answer_district]
        t.goto(int(district_data.x.iloc[0]), int(district_data.y.iloc[0]))  # Use .iloc[0] to get the integer value
        t.write(answer_district)

# def get_mouse_click_coord(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()

