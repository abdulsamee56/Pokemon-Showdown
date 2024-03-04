import tkinter as tk
from PIL import Image, ImageTk
import os
import turtle

# Function to convert an image to turtle graphics code.
def convert_image_to_turtle_code(filename, background_color=(255, 255, 255)):
    # Open the image file and convert it to RGB format.
    image = Image.open(filename).convert("RGB")


    # Setup turtle screen size slightly larger than the image size.
    turtle.setup(image.width + 50, image.height + 50)

    # Speed up the drawing process.
    turtle.tracer(80)

    # Create a turtle object for drawing.
    turtle_obj = turtle.Turtle()
    turtle_obj.speed(0)  # Set drawing speed to the fastest.
    dot_size = 3  # Size of the dot to draw.

    # Iterate over each pixel in the image to draw it.
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))  # Get the RGB value of the pixel.

            # Skip drawing if the pixel color matches the background color.
            if (r, g, b) == background_color:
                continue

            # Calculate the turtle's position.
            turtle_x = x - (image.width // 2)
            turtle_y = (image.height // 2) - y

            turtle_obj.penup()
            turtle_obj.goto(turtle_x, turtle_y)
            turtle_obj.pendown()

            # Set the turtle's color based on the pixel's RGB values and draw a dot.
            turtle_obj.pencolor(r / 255, g / 255, b / 255)
            turtle_obj.dot(dot_size)

    # Hide the turtle after drawing is complete and update the screen.
    turtle_obj.hideturtle()
    turtle.update()

# Function called when a Pokémon is selected from the dropdown.
def on_pokemon_select(pokemon_idx):
    # Get the selected Pokémon's name.
    selected_pokemon_name = pokemon_names[pokemon_idx]

    # Get the current directory and build the path to the image file.
    current_dir = os.path.dirname(os.path.realpath(__file__))
    base_path = os.path.join(current_dir, 'TurtleSprites')
    filename = os.path.join(base_path, f"{selected_pokemon_name}.png")

    # Convert the image to turtle graphics code.
    convert_image_to_turtle_code(filename)

# Function to create the main Tkinter window for selecting Pokemon.
def create_pokemon_selection_window():
    selection_window = tk.Tk()
    selection_window.title("Choose Your Pokemon")
    selection_window.geometry("800x400")

    # Set background image
    background_image = Image.open("lab.png")
    background_image = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(selection_window, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Add title label
    title_label = tk.Label(selection_window, text="Select Your Pokemon", font=("Helvetica", 20), bg="#87ceeb", padx=20, pady=10)
    title_label.place(relx=0.5, rely=0.05, anchor='n')

    # Create an array to hold all the buttons
    pokemon_buttons = []
    for i, pokemon_name in enumerate(pokemon_names):
        pokemon_button = tk.Button(
            selection_window,
            text=pokemon_name,
            command=lambda idx=i: on_pokemon_select(idx),
            bg='#ffcccb',  # Light coral color
            padx=10,
            pady=5
        )
        pokemon_button.place(relx=0.2 + (i % 4) * 0.2, rely=0.2 + (i // 4) * 0.15, relwidth=0.15, relheight=0.1)
        pokemon_buttons.append(pokemon_button)

    selection_window.mainloop()

# Array that will hold the Users pokemon
pokemon_names = [
    "Snorlax", "Slowbro", "Swampert", "Lickilicky", "Mr. Mime",
    "Blaziken", "Sceptile", "Electivire", "Heracross", "Garchomp",
    "Mamoswine", "Magnezone", "Metagross", "Flygon", "Lucario",
    "Empoleon", "Charizard", "Drapion", "Tyranitar", "Gengar", "Scizor"
]

# Call the function to create the Tkinter window for selecting Pokemon.
create_pokemon_selection_window()
