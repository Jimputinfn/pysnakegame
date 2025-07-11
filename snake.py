# Credit To Jimputin https://github.com/Jimputinfn @ https://elysiannodes.uk
# I added comments to some parts of the code to make it easier to understand
from tkinter import *
import random
import tkinter as tk

# Game Settings
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 1
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body_parts = BODY_PARTS
        self.coordinates = []
        self.squares = []
        # Starting position of the snake

        for _ in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]
        self.canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
def next_turn(snake, food):
    global score
    
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food(canvas)
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    if new_direction == 'left':    
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
    new_game_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

def start_new_game():
    global snake, food, score, direction
    canvas.delete(ALL)
    new_game_button.place_forget()
    score = 0
    direction = "down"
    label.config(text="Score: {}".format(score))
    snake = Snake(canvas)
    food = Food(canvas)
    next_turn(snake, food)

window = Tk()
window.title("Snake Game By Jimputin")
window.resizable(False, False)

score = 0
direction = "down"
label = Label(window, text="Score: {}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

new_game_button = tk.Button(window, text="New Game", command=start_new_game, font=('consolas', 20))

# Center the window on the screen
window.update_idletasks()
window_width = window.winfo_width() 
window_height = window.winfo_height() 
screen_width = window.winfo_screenwidth() 
screen_height = window.winfo_screenheight() 

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#keybinds
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))

snake = Snake(canvas)
food = Food(canvas)

next_turn(snake, food)

window.mainloop()
