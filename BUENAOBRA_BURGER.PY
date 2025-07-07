import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Stylized Bouncing Burger - Running")
root.geometry("600x400")
root.resizable(False, False)

# Canvas
canvas = tk.Canvas(root, width=600, height=400, bg="skyblue")
canvas.pack()

# Initial position and movement
x, y = 100, 100
dx, dy = 3, 2
paused = False

# Create stylized burger
top_bun = canvas.create_oval(x, y, x+160, y+60, fill="#F4A460", outline="")  # top bun
seeds = [
    canvas.create_oval(x+30+i*20, y+10, x+35+i*20, y+15, fill="white", outline="")
    for i in range(5)
]  # sesame seeds

lettuce = canvas.create_polygon(
    x+10, y+58, x+20, y+68, x+40, y+60, x+60, y+68, x+80, y+60,
    x+100, y+68, x+120, y+60, x+140, y+68, x+150, y+58,
    fill="#32CD32", outline=""
)

tomato = canvas.create_rectangle(x+20, y+70, x+140, y+80, fill="#FF6347", outline="")  # tomato
cheese = canvas.create_polygon(
    x+30, y+80, x+130, y+80, x+115, y+90, x+45, y+90,
    fill="#FFD700", outline=""
)
patty = canvas.create_rectangle(x+25, y+90, x+135, y+105, fill="#8B4513", outline="")  # patty

# Centered name in burger with outline effect
# First: outline (black)
name_outline = canvas.create_text(x+80, y+97, text="ASHLY BUENAOBRA", font=("Arial", 14, "bold"), fill="black")
# Then: foreground (white) slightly offset
name_text = canvas.create_text(x+80, y+96, text="ASHLY BUENAOBRA", font=("Arial", 14, "bold"), fill="white")

bottom_bun = canvas.create_oval(x, y+105, x+160, y+150, fill="#DEB887", outline="")  # bottom bun

# Group all burger parts
burger_parts = [top_bun] + seeds + [lettuce, tomato, cheese, patty, name_outline, name_text, bottom_bun]

# Function to change colors randomly
def change_burger_colors():
    canvas.itemconfig(top_bun, fill=random.choice(["#F4A460", "#D2B48C", "#DAA520"]))
    canvas.itemconfig(lettuce, fill=random.choice(["#32CD32", "#7CFC00", "#228B22"]))
    canvas.itemconfig(tomato, fill=random.choice(["#FF6347", "#DC143C", "#B22222"]))
    canvas.itemconfig(cheese, fill=random.choice(["#FFD700", "#FFA500", "#FFEB3B"]))
    canvas.itemconfig(patty, fill=random.choice(["#8B4513", "#A0522D", "#5C4033"]))
    canvas.itemconfig(bottom_bun, fill=random.choice(["#DEB887", "#CD853F", "#D2B48C"]))
    for seed in seeds:
        canvas.itemconfig(seed, fill=random.choice(["white", "ivory", "beige"]))

# Pause toggle function
def toggle_pause(event):
    global paused
    paused = not paused
    root.title(f"Stylized Bouncing Burger - {'Paused' if paused else 'Running'}")

# Animation
def move_burger():
    global x, y, dx, dy

    if not paused:
        x += dx
        y += dy

        bounced = False
        if x <= 0 or x + 160 >= 600:
            dx = -dx
            bounced = True
        if y <= 0 or y + 150 >= 400:
            dy = -dy
            bounced = True

        if bounced:
            change_burger_colors()

        for part in burger_parts:
            canvas.move(part, dx, dy)

    root.after(30, move_burger)

# Bind spacebar to pause/resume
root.bind("<space>", toggle_pause)

# Start animation
move_burger()

# Run the application
root.mainloop()