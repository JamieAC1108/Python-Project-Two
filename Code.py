import requests

# API URL
url = 'https://opentdb.com/api.php?amount=1&category=9&type=boolean'

response = requests.get(url)


if response.status_code == 200:

    # Converts the response into a dictionary so we can work with it
    data = response.json()

    # Retrieving the question and correct answer from the dictionary
    question = data['results'][0]['question']
    correct_answer = data['results'][0]['correct_answer']

    # Asking the question and collecting input
    print(question, "True or False?")
    user_answer = input("Your answer:").strip().capitalize()

    # Checking if answer is correct or not then providing feedback
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect. The correct answer was:", correct_answer)
else:

    # If URL can't be reached
    print("Failed to retrive data:", response.status_code)
