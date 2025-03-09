import random
import string
import requests

# Function that generates a single random character
def random_character():
    choices = string.ascii_letters + string.digits + string.punctuation
    return random.choice(choices)

# Ask the user for password length
while True:
    try:
        password_length = int(input("Enter the length of the strong password: "))
        if password_length < 4:  # Ensuring a minimum length for security
            print("Password length should be at least 4.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

# Function that generates a strong password
def generate_strong_password(length):
    return ''.join(random_character() for _ in range(length))

# Function to fetch a random word from the API
def fetch_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?length=6", timeout=5)
        response.raise_for_status()  # Raise error for bad responses
        word = response.json()[0]
        return word
    except (requests.RequestException, IndexError, ValueError):
        return "Fallback"  # Use fallback word if API fails

# Function to replace letters for a weaker password
def replace_letters(word):
    word = word.capitalize()  # Ensure first letter is uppercase
    word = word.replace("a", "@").replace("o", "0").replace("i", "1").replace("e", "3")
    return word

# Function to generate a weaker password
def generate_weaker_password():
    word1 = replace_letters(fetch_word())
    word2 = replace_letters(fetch_word())
    return word1 + word2

# Generate and print passwords
print("Strong Password:", generate_strong_password(password_length))
print("Weaker Password:", generate_weaker_password())


