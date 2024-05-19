# War Cards Game

Welcome to the War Cards Game project! This project is built using Python and Django and implements the classic card game "War". This README file will guide you through the setup and usage of the project.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Introduction

War is a simple card game played between two players. In each round, both players draw a card from their decks, and the player with the higher card wins the round and takes both cards. The game continues until one player has all the cards or a specified number of rounds have been played.

## Features

- Start a new game
- Play rounds of War
- Track the progress and results of the game

## Requirements

- Python 3.8 or higher
- Django 3.2 or higher

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/war-cards-game.git
   cd war-cards-game
Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the dependencies:
pip install -r requirements.txt
Apply the database migrations:
python manage.py migrate
Run the development server:
python manage.py runserver
Open your web browser and navigate to:
http://127.0.0.1:8000/

Usage
Open the web application.
Start a new game.
Click "Draw Card" to play a round of War.
View the results of each round and track your progress.

Enjoy playing the War card game! If you have any questions or run into any issues, please open an issue on the GitHub repository. Happy gaming!
