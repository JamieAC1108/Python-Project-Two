import requests
import json
import html

# Load or initialize scores
try:
    with open("scores.json", "r") as f:
        scores = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    scores = {}

# Trivia question storage
current_question = None
current_answer = None

def fetch_trivia():
    global current_question, current_answer
    url = 'https://opentdb.com/api.php?amount=1&category=9&type=boolean'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current_question = html.unescape(data['results'][0]['question'])  
        current_answer = data['results'][0]['correct_answer'].lower()
    else:
        print(f'Trivia unable to be fetched, sorry!')
        current_question = None
        current_answer = None

def ask_question(player_name):
    global current_answer
    fetch_trivia()
    if current_question:
        print(f"Trivia Time! {current_question} (True/False)")
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer == "hint":
            print("Hint: The answer is either True or False!")
            user_answer = input("Your answer: ").strip().lower()
        
        if user_answer in ["true", "false"]:
            if user_answer == current_answer:
                scores[player_name] = scores.get(player_name, 0) + 1
                print(f"Correct! {player_name}, your current score: {scores[player_name]} points.")
            else:
                print(f"Incorrect. The correct answer was: {current_answer.capitalize()}. {player_name}, your current score: {scores.get(player_name, 0)} points.")
            
            with open("scores.json", "w") as f:
                json.dump(scores, f)
            
            current_answer = None  # Reset question after answering
        else:
            print("Invalid answer! Please enter 'True' or 'False'.")

def show_leaderboard():
    if not scores:
        print("Trivia Leaderboard\nNo scores available yet!")
        return
    
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print("Trivia Leaderboard")
    for player, score in sorted_scores[:10]:  # Leaderboard
        print(f"{player}: {score} points")

def main():
    player_name = input("Enter your player name: ").strip()
    while True:
        command = input(f"\n{player_name}, type 'trivia' to get a question, 'leaderboard' to view scores, or 'exit' to quit: ").strip().lower()
        
        if command == "trivia":
            ask_question(player_name)
        elif command == "leaderboard":
            show_leaderboard()
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command! Please enter 'trivia', 'leaderboard', or 'exit'.")

if __name__ == "__main__":
    main()