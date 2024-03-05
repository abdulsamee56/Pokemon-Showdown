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

    # Get the corresponding description for the selected Pokémon.
    pokemon_description = pokemon_info[pokemon_idx]

    # Get the corresponding stats for the selected Pokémon.
    selected_pokemon_stats = next((pokemon for pokemon in stats if pokemon["name"] == selected_pokemon_name), None)

    if selected_pokemon_stats:
        # Get the current directory and build the path to the image file.
        current_dir = os.path.dirname(os.path.realpath(__file__))
        base_path = os.path.join(current_dir, 'TurtleSprites')
        filename = os.path.join(base_path, f"{selected_pokemon_name}.png")

        # Convert the image to turtle graphics code.
        convert_image_to_turtle_code(filename)

        # Create Pokemon information window
        create_pokemon_info_window(selected_pokemon_name, pokemon_description, selected_pokemon_stats)
    else:
        print(f"Stats not found for {selected_pokemon_name}")


# Function to create the main Tkinter window for selecting Pokemon.
def create_pokemon_selection_window():
    selection_window = tk.Tk()
    selection_window.title("Choose Your Pokemon")
    selection_window.geometry("800x400")

    # Set background image
    current_dir = os.path.dirname(os.path.abspath(__file__))
    background_image_path = os.path.join(current_dir, "lab.png")
    background_image = Image.open(background_image_path)
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
            padx=5,  # Adjust horizontal padding
            pady=2,  # Adjust vertical padding
        )
        # Calculate button position based on grid layout
        row = i // 5  # Adjust the number of buttons per row as needed
        col = i % 5
        button_x = 0.1 + col * 0.18  # Adjust x-position
        button_y = 0.2 + row * 0.15  # Adjust y-position
        pokemon_button.place(relx=button_x, rely=button_y, relwidth=0.15, relheight=0.1)  # Adjust button size
        pokemon_buttons.append(pokemon_button)

    selection_window.mainloop()


def create_pokemon_info_window(pokemon_name, pokemon_description, pokemon_stats):
    info_window = tk.Toplevel()
    info_window.title(f"{pokemon_name} Information")
    info_window.geometry("800x600")

    # Set background image
    current_dir = os.path.dirname(os.path.abspath(__file__))
    background_image_path = os.path.join(current_dir, "pokedex.png")
    background_image = Image.open(background_image_path)
    background_image = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(info_window, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Add title label
    title_label = tk.Label(info_window, text=f"{pokemon_name}", font=("Helvetica", 20), padx=10, pady=10, borderwidth=5, relief="groove", fg="black")
    title_label.place(relx=0.5, rely=0.1, anchor='n')

    # Add description label
    description_label = tk.Label(info_window, text=f"{pokemon_description}", font=("Helvetica", 12), wraplength=700, justify="left", padx=10, pady=10, borderwidth=5, relief="groove", fg="black")
    description_label.place(relx=0.5, rely=0.25, anchor='n')

    # Add stats label
    stats_label = tk.Label(info_window, text="Stats:", font=("Helvetica", 16, "bold"), padx=10, pady=10, borderwidth=5, relief="groove", fg="black")
    stats_label.place(relx=0.5, rely=0.5, anchor='n')

    # Add points label
    points_text = "\n".join([f"{stat}: {value}" for stat, value in pokemon_stats.items()])
    points_label = tk.Label(info_window, text=points_text, font=("Helvetica", 14), justify="left", padx=10, pady=10, borderwidth=5, relief="groove", fg="black")
    points_label.place(relx=0.5, rely=0.6, anchor='n')

    info_window.mainloop()




# Array that will hold the Users pokemon
pokemon_names = [
    "Snorlax", "Slowbro", "Swampert", "Lickilicky", "Mr. Mime",
    "Blaziken", "Sceptile", "Electivire", "Heracross", "Garchomp",
    "Mamoswine", "Magnezone", "Metagross", "Flygon", "Lucario",
    "Empoleon", "Charizard", "Drapion", "Tyranitar", "Gengar", "Scizor"
]

#Array to hold the pokemon Descriptions
pokemon_info = [
    "Snorlax is the heaviest species of all known Pokémon, with some weighing more than one thousand pounds. Snorlax's hunger isn't satisfied until it consumes 900 pounds of food. Then it goes back to sleep.",
    "Slowbro's tail has a Shellder firmly attached with a bite. As a result, the tail can't be used for fishing anymore. This causes Slowbro to grouse.",
    "Swampert is very strong. It has enough power to easily drag a boulder weighing more than a ton. This Pokémon also has powerful vision that lets it see even in murky water.",
    "Lickilicky can eat anything, even if it happens to be a little moldy. It feels nauseous when this Pokémon happens to eat something bad.",
    "Mr. Mime is a master of pantomime. Its gestures and motions convince watchers that something unseeable actually exists. Once the watchers are convinced, the unseeable thing exists as if it were real.",
    "Blaziken has incredibly strong legs—it can easily clear a 30-story building in one leap. This Pokémon's blazing punches leave its foes scorched and blackened.",
    "Sceptile has seeds growing on its back. They are said to be bursting with nutrients that revitalize trees. This Pokémon raises the trees in a forest with loving care.",
    "Electivire's body always carries an electrical charge. By shuffling its feet, it generates electricity. In the moment before an Electivire begins to fight, the air around it becomes ELECTRIFIED with the sound of crackling sparks.",
    "Heracross charges in a straight line at its foe, slips beneath the foe's grasp, and then scoops up and hurls the opponent with its mighty horn. This Pokémon even has enough power to topple a massive tree.",
    "Garchomp makes its home in volcanic mountains. It flies through the sky as fast as a jet airplane, hunting down as much prey as it can.",
    "Mamoswine lived in the ice age approximately ten thousand years ago. Its huge tusks are actually ancient icicles that are made of the same material as an Alolan Sandslash's spikes.",
    "Magnezone controls electromagnetic fields. It is said that Magneton emerged when Magnemite evolved in the presence of a magnetic field. Of the three, Magneton is the only one that does not evolve.",
    "Metagross has four brains that are joined by a complex neural network. As a result of integration, this Pokémon is smarter than a supercomputer. It uses psychic power to coordinate its four brains.",
    "Flygon is nicknamed \"the elemental spirit of the desert.\" Because its flapping wings whip up a cloud of sand, this Pokémon is always enveloped in a sandstorm while flying.",
    "Lucario reads its opponent's feelings with its aura waves. It finds out things it would rather not know, so it gets stressed out easily.",
    "The steel spikes on Empoleon's wings are harder than diamonds. This Pokémon flies at speeds of Mach 1. Empoleon is also known to compress air and shoot itself like a bullet to attack its prey.",
    "Charizard flies around the sky in search of powerful opponents. It breathes fire of such great heat that it melts anything. However, it never turns its fiery breath on any opponent weaker than itself.",
    "Drapion's body is encased in a sturdy shell. Its head rotates 180 degrees, eliminating blind spots. Its tail is loaded with that even a scratch could prove fatal.",
    "Tyranitar is so overwhelmingly powerful, it can bring down a whole mountain to make its nest. This Pokémon wanders about in mountains seeking new opponents to fight.",
    "Gengar hides in the shadows. It is said that if Gengar is hiding, it cools the area by nearly 10 degrees Fahrenheit.",
    "Scizor has a body with the hardness of steel. It is not easily fazed by ordinary sorts of attacks. This Pokémon flaps its wings to regulate its body temperature.",
]
stats = [
    {"name": "Snorlax", "HP": 160, "ATK": 110, "SPATK": 65, "DEF": 65, "SPDEF": 110, "TYPE": "Normal"},
    {"name": "Slowbro", "HP": 95, "ATK": 75, "SPATK": 100, "DEF": 110, "SPDEF": 80, "TYPE": "Water/Psychic"},
    {"name": "Swampert", "HP": 100, "ATK": 110, "SPATK": 85, "DEF": 90, "SPDEF": 90, "TYPE": "Water/Ground"},
    {"name": "Lickilicky", "HP": 110, "ATK": 85, "SPATK": 80, "DEF": 95, "SPDEF": 95, "TYPE": "Normal"},
    {"name": "Mr. Mime", "HP": 40, "ATK": 45, "SPATK": 100, "DEF": 65, "SPDEF": 120, "TYPE": "Psychic/Fairy"},
    {"name": "Blaziken", "HP": 80, "ATK": 120, "SPATK": 110, "DEF": 70, "SPDEF": 70, "TYPE": "Fire/Fighting"},
    {"name": "Sceptile", "HP": 70, "ATK": 85, "SPATK": 105, "DEF": 65, "SPDEF": 85, "TYPE": "Grass"},
    {"name": "Electivire", "HP": 75, "ATK": 123, "SPATK": 95, "DEF": 67, "SPDEF": 85, "TYPE": "Electric"},
    {"name": "Heracross", "HP": 80, "ATK": 125, "SPATK": 40, "DEF": 75, "SPDEF": 95, "TYPE": "Bug/Fighting"},
    {"name": "Garchomp", "HP": 108, "ATK": 130, "SPATK": 80, "DEF": 95, "SPDEF": 85, "TYPE": "Dragon/Ground"},
    {"name": "Mamoswine", "HP": 110, "ATK": 130, "SPATK": 70, "DEF": 60, "SPDEF": 60, "TYPE": "Ice/Ground"},
    {"name": "Magnezone", "HP": 70, "ATK": 70, "SPATK": 130, "DEF": 115, "SPDEF": 90, "TYPE": "Electric/Steel"},
    {"name": "Metagross", "HP": 80, "ATK": 135, "SPATK": 95, "DEF": 130, "SPDEF": 90, "TYPE": "Steel/Psychic"},
    {"name": "Flygon", "HP": 80, "ATK": 100, "SPATK": 80, "DEF": 80, "SPDEF": 80, "TYPE": "Ground/Dragon"},
    {"name": "Lucario", "HP": 70, "ATK": 110, "SPATK": 115, "DEF": 70, "SPDEF": 70, "TYPE": "Fighting/Steel"},
    {"name": "Empoleon", "HP": 84, "ATK": 86, "SPATK": 111, "DEF": 88, "SPDEF": 101, "TYPE": "Water/Steel"},
    {"name": "Charizard", "HP": 78, "ATK": 84, "SPATK": 109, "DEF": 78, "SPDEF": 85, "TYPE": "Fire/Flying"},
    {"name": "Drapion", "HP": 70, "ATK": 90, "SPATK": 60, "DEF": 110, "SPDEF": 75, "TYPE": "Poison/Dark"},
    {"name": "Tyranitar", "HP": 100, "ATK": 134, "SPATK": 95, "DEF": 110, "SPDEF": 100, "TYPE": "Rock/Dark"},
    {"name": "Gengar", "HP": 60, "ATK": 65, "SPATK": 130, "DEF": 60, "SPDEF": 75, "TYPE": "Ghost/Poison"},
    {"name": "Scizor", "HP": 70, "ATK": 130, "SPATK": 55, "DEF": 100, "SPDEF": 80, "TYPE": "Bug/Steel"}
]
#Start the pokemon selection window
create_pokemon_selection_window()
