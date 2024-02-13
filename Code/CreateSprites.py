import os
import turtle
from PIL import Image
import tkinter as tk
from tkinter import ttk

# Function to convert an image to turtle graphics code.
def convert_image_to_turtle_code(filename, background_color=(255, 255, 255)):
    # Open the image file and convert it to RGB format.
    image = Image.open(filename).convert("RGB")
    
    # Setup turtle screen size based on the image size.
    turtle.setup(image.width, image.height)
    
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

# Function to print a Pokémon sprite using turtle graphics.
def printPokemon(pokemon):
    # Get the current directory and build the path to the image file.
    current_dir = os.path.dirname(os.path.realpath(__file__))
    base_path = os.path.join(current_dir, 'TurtleSprites')
    filename = os.path.join(base_path, f"{pokemon}.png")

    # Convert the image to turtle graphics code.
    convert_image_to_turtle_code(filename)

# Function called when a Pokémon is selected from the dropdown.
def onPokemonSelect(event):
    # Get the selected Pokémon's name.
    pokemon = pokemon_var.get()
    # Print the Pokémon using turtle graphics.
    printPokemon(pokemon)

# Main function to create the GUI.
def main():
    global pokemon_var  # Global variable to hold the selected Pokémon's name.
    
    # Create the Tkinter window.
    root = tk.Tk()
    root.title("Choose a Pokémon")

    # List of Pokémon names.
    pokemon_list = [
        'Charizard', 'Snorlax', 'Slowbro', 'Swampert', 'Lickilicky', 'Mr. Mime', 'Blaziken', 'Sceptile', 'Electivire', 
        'Heracross', 'Garchomp', 'Mamoswine', 'Magnezone', 'Metagross', 'Flygon', 'Lucario', 'Empoleon', 'Tyranitar',
        'Drapion', 'Gengar', 'Scizor'
    ]

    # Tkinter string variable to hold the selected Pokémon's name.
    pokemon_var = tk.StringVar()
    
    # Create a dropdown menu with the list of Pokémon.
    pokemon_dropdown = ttk.Combobox(root, textvariable=pokemon_var, values=pokemon_list, state="readonly")
    pokemon_dropdown.pack()
    
    # Bind the selection event to the onPokemonSelect function.
    pokemon_dropdown.bind("<<ComboboxSelected>>", onPokemonSelect)

    # Start the Tkinter event loop.
    root.mainloop()
main()
