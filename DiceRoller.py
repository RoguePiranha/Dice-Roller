import tkinter as tk
import random
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

#########################################################################
#                           Dice Roller GUI                             #
#########################################################################
#                                                                       #
# This program creates a simple dice roller application using tkinter.  #
# The application allows the user to select a dice type (e.g., D6, D20) #
# and roll the dice to get a random result. The result is displayed in  #
# text format over a topographical image of the dice, which I also made.#
#                                                                       #
#########################################################################
# Author: Andrew Swayze                                                 #
# Date: 2024-10-10                                                      #
#########################################################################


# Create the tkinter application
root = tk.Tk()
root.title("Dice Roller")
root.geometry("550x450")  # Set default window size

# Set the default font for the entire program
# I just like Fira Code, you can change it to any font you like
# The method here pulls from installed system fonts, so if you
# want to keep using Fira Code, you'll need to install it on your system
fira_code_font = ("Fira Code", 12)  # Font name and size
root.option_add("*Font", fira_code_font) # Set the default font for all widgets

# Path to the fira code font file, change the path if needed
# this font is used to draw the dice roll result on the images
font_path = os.path.join(os.path.dirname(__file__), "Font/FiraCode-Regular.ttf")
if not os.path.exists(font_path):
    font_path = None  # Fallback if font file not found

# Function to plot different dice topographies
def plot_dice(roll_result, num_sides, canvas_frame):
    # Clear previous canvas
    for widget in canvas_frame.winfo_children():
        # clears the canvas of any previous dice images
        widget.destroy() 

    if num_sides == 100:
        # For D100, represent as two D10 next to each other
        tens_result = (roll_result // 10) * 10 if roll_result < 100 else 90
        ones_result = roll_result % 10

        # Load the images for the two D10 dice
        tens_image_path = "Assets/D10.png"
        ones_image_path = "Assets/D10.png"

        # Load the images using PIL
        tens_img = Image.open(tens_image_path)
        ones_img = Image.open(ones_image_path)

        # Draw the text on each image
        draw_text_on_image(tens_img, str(tens_result), font_path)
        draw_text_on_image(ones_img, str(ones_result), font_path)

        # Convert to Tkinter-compatible format
        tens_img_tk = ImageTk.PhotoImage(tens_img)
        ones_img_tk = ImageTk.PhotoImage(ones_img)

        # Create labels to display the images side by side with flexible spacing
        tens_label = tk.Label(canvas_frame, image=tens_img_tk)
        tens_label.image = tens_img_tk  # Keep a reference to avoid garbage collection
        tens_label.place(relx=0.25, rely=0.5, anchor="center")

        ones_label = tk.Label(canvas_frame, image=ones_img_tk)
        ones_label.image = ones_img_tk  # Keep a reference to avoid garbage collection
        ones_label.place(relx=0.75, rely=0.5, anchor="center")
    else:
        # Define image file path based on the number of sides
        image_path = f"Assets/D{num_sides}.png"

        # Load the image using PIL
        img = Image.open(image_path)

        # Draw the roll result text on the image
        draw_text_on_image(img, str(roll_result), font_path)

        # Convert to Tkinter-compatible format
        img_tk = ImageTk.PhotoImage(img)

        # Create a label to display the image
        img_label = tk.Label(canvas_frame, image=img_tk)
        img_label.image = img_tk  # Keep a reference to avoid garbage collection
        img_label.place(relx=0.5, rely=0.5, anchor="center")

# Function to draw text on an image
def draw_text_on_image(image, text, font_path):
    draw = ImageDraw.Draw(image)
    font_size = 30
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()

    # Calculate the bounding box of the text to center it
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    position = ((image.width - text_width) // 2, (image.height - text_height) // 2)

    # Draw the text onto the image
    draw.text(position, text, font=font, fill="black")

# Function to roll the dice
def roll_dice():
    # Get selected dice type
    selected_dice = dice_var.get()

    # Determine the number of sides
    num_sides = int(selected_dice[1:])

    # Roll the dice and display the result
    result = random.randint(1, num_sides)
    result_label.config(text=f"You rolled a {result} on a {selected_dice}")

    # Draw topographical representation
    plot_dice(result, num_sides, canvas_frame)

# Available dice choices
dice_options = ["D4", "D6", "D8", "D10", "D12", "D20", "D100"]

# Create dropdown to select dice
dice_var = tk.StringVar(root)
dice_var.set(dice_options[0])  # Set default value
dice_menu = tk.OptionMenu(root, dice_var, *dice_options)
dice_menu.pack(pady=10)

# Button to roll the dice
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="Roll result will appear here")
result_label.pack(pady=10)

# Canvas for topographical representation
canvas_frame = tk.Frame(root, width=550, height=260, bg="white")  # Set the desired background color here
canvas_frame.pack(pady=10)

# Run the application
if __name__ == "__main__":
    root.mainloop()
