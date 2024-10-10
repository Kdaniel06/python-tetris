# Tetris game

This project is a simple implementation of the classic game ***"TETRIS"***. The project will be developed using python and the library pygame. The game will include typical Tetris features like falling tetrominoes, rotating pieces, clearing rows, and increasing difficulty levels.

## Project Structure

The game will be implemented using Python's Pygame library, and an isolated environment will be set up using Python's `venv`.

## Features
- Standard Tetris gameplay
- Score tracking
- Line clearing
- Game over detection

## Setup and Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/tetris-game.git
cd tetris-game
```

### Setting Up the Virtual Environment

To ensure that the project dependencies are managed correctly, a Python virtual environment will be used. Follow the steps below to set up the environment:

#### Step 1: Create a Virtual Environment

* Run the following command to create a virtual environment:

```bash
python -m venv venv
```

#### Step 2: Activate the Virtual Environment
* For Windows:

```bash
.\venv\Scripts\activate
```

* For macOS/Linux:

```bash
source venv/bin/activate
```

#### Step3: Install Dependencies
Once the virtual environment is activated, you can install Pygame with:

```bash
pip install -r requirements.txt
```

#### Step 4: Run the Game
After setting up everything, you can start the game (once implemented) with:

```bash
python main.py
```

## How to Play
* Use arrow keys to move the pieces.
* Rotate pieces with the up arrow key.
* Try to fill horizontal lines to clear them and score points.
