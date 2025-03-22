# Daily Trivia Terminal Game

A simple Python terminal-based trivia game that fetches True/False questions from the OpenTriviaDB API. Players can answer questions, request hints, track scores, and view a leaderboard!

---

## Features

- Pulls a new trivia question (True/False) from OpenTriviaDB
- Accepts answers through terminal input
- Provides hints on request
- Tracks and saves user scores in `scores.json`
- Displays a leaderboard
- Option to reset all scores

---

## Setup Instructions

### Requirements
- Python 3.x
- `requests` library

### Install dependencies
- bash
- pip install requests


### Run the game
- bash
- python main.py




## Commands in Game

- `trivia` – Get a new trivia question
- `leaderboard` – View top player scores
- `reset` – Clear all scores
- `exit` – Quit the game



## File Structure


/trivia-game
  ├── main.py
  ├── scores.json
  └── README.md


> Note: `scores.json` is automatically created to store user progress.



## Trivia Source

All trivia questions are fetched from:  
[https://opentdb.com](https://opentdb.com)



## Team Members

- P.J. Cannon
- Jamie Cole
- Prae



## Project Info

Course: CPT127  
Group Project 1.4 – Trivia Bot  
Spring 2025
