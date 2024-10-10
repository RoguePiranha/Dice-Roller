# Dice Roller

A simple graphical dice roller application built using Python's Tkinter library. The program allows users to roll various types of dice, including D4, D6, D8, D10, D12, D20, and D100, with results displayed visually using dice images.

## Features

- Supports rolling a variety of dice, including D4, D6, D8, D10, D12, D20, and D100.
- Displays the rolled result on top of an image of the dice.
- For D100, represents the result using two D10 dice side by side.
- Allows users to select the type of dice from a dropdown menu.
- Uses Fira Code for displaying the results, which can be customized.

## Prerequisites

Before running the program, make sure you have the following:

- Python 3.x
- The `Pillow` library for image processing (`PIL`)
- `Tkinter`, which is included with most Python distributions

## Installation

1. **Clone the repository:**

   ```bash
   git clone <https://github.com/yourusername/dice-roller.git>
   cd dice-roller
   ```

2. **Install dependencies:**

   Install the required dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should only contain the following:

   ```bash
   pillow==10.4.0
   ```

3. **Add dice images:**

   Make sure you have the dice images in an `Assets/` directory. The directory should contain images named `D4.png`, `D6.png`, etc., up to `D100.png`.

4. **Run the program:**

   ```bash
   python DiceRoller.py
   ```

## Usage

1. Launch the application by running `DiceRoller.py`.
2. Select the type of dice you want to roll from the dropdown menu.
3. Click the "Roll Dice" button to roll the selected dice.
4. The rolled result will be displayed in the center of the window.

## Directory Structure

```bash
dice-roller/
├── Assets/
│   ├── D4.png
│   ├── D6.png
│   ├── D8.png
│   ├── D10.png
│   ├── D12.png
│   ├── D20.png
│   ├── D100.png
├── Font/
│   └── FiraCode-Regular.ttf
├── DiceRoller.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Customization

### Changing the Font

If you have a custom font (e.g., `FiraCode-Regular.ttf`), you can place it in the `Font/` directory. The program will try to use it; otherwise, it will fall back to the system's default font.

## Troubleshooting

### Font Issues

If the custom font isn't displaying correctly:

- Ensure that the font file (`FiraCode-Regular.ttf`) exists in the `Font/` directory.
- Make sure the path to the font file is correct.

### Missing Dependencies

If you have issues with missing dependencies, make sure you have installed the required packages using:

```bash
pip install -r requirements.txt
```
