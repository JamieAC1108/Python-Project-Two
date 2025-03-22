import requests
import json
import html
import os
from datetime import datetime

# Load or initialize scores
SCORES_FILE = "scores.json"

try:
    with open(SCORES_FILE, "r") as f:
        scores = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    scores = {}

# Trivia state
current_question = None
current_answer = None
hint_given = False


def fetch_trivia():
    global current_question, current_answer, hint_given
    url = 'https://opentdb.com/api.php?amount=1&category=9&type=boolean'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current_question = html.unescape(data['results'][0]['question'])
        current_answer = data['results'][0]['correct_answer'].lower()
        hint_given = False
    else:
        print("\n[Error] Unable to fetch trivia question. Please check your internet connection.\n")
        current_question = None
        current_answer = None


def ask_question(player_name):
    global current_question, current_answer, hint_given
    fetch_trivia()

    if not current_question:
        return

    print(f"\n=== Trivia Time! ===\n{current_question} (True/False)\n")

    while True:
        user_input = input("Your answer (or type 'hint' or 'skip'): ").strip().lower()

        if user_input == "hint" and not hint_given:
            print("Hint: The answer is either True or False!\n")
            hint_given = True
        elif user_input == "skip":
            print("Question skipped.\n")
            break
        elif user_input in ["true", "false"]:
            if user_input == current_answer:
                scores[player_name] = scores.get(player_name, 0) + 1
                print(f"\n✅ Correct! {player_name}, your score: {scores[player_name]} point(s).\n")
            else:
                print(f"\n❌ Incorrect. The correct answer was: {current_answer.capitalize()}. {player_name}, your score: {scores.get(player_name, 0)} point(s).\n")

            with open(SCORES_FILE, "w") as f:
                json.dump(scores, f)

            break
        else:
            print("\nInvalid input. Please enter 'True', 'False', 'hint', or 'skip'.\n")


def show_leaderboard():
    if not scores:
        print("\n📊 Trivia Leaderboard\nNo scores available yet!\n")
        return

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print("\n📊 Trivia Leaderboard")
    print("----------------------")
    for i, (player, score) in enumerate(sorted_scores[:10], start=1):
        print(f"{i}. {player}: {score} point(s)")
    print()


def reset_scores():
    confirm = input("Are you sure you want to reset all scores? (yes/no): ").strip().lower()
    if confirm == "yes":
        scores.clear()
        if os.path.exists(SCORES_FILE):
            os.remove(SCORES_FILE)
        print("\n🧹 Scores have been reset.\n")
    else:
        print("\nScores not reset.\n")


def main():
    print("\n🎉 Welcome to the Daily Trivia Game! 🎉")
    print("Answer True/False questions, earn points, and climb the leaderboard!\n")

    player_name = input("Enter your player name: ").strip()

    while True:
        print("\nAvailable commands:")
        print(" trivia       - Get a new trivia question")
        print(" leaderboard  - View the top scores")
        print(" reset        - Reset all scores")
        print(" exit         - Quit the game\n")

        command = input(f"{player_name}, enter a command: ").strip().lower()

        if command == "trivia":
            ask_question(player_name)
        elif command == "leaderboard":
            show_leaderboard()
        elif command == "reset":
            reset_scores()
        elif command == "exit":
            print("\n👋 Goodbye, thanks for playing!\n")
            break
        else:
            print("\nUnknown command. Please try again.\n")


if __name__ == "__main__":
    main()
