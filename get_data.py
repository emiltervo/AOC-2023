import os
import sys
import requests
from dotenv import load_dotenv

def fetch_aoc_input(day, year=2023, session_cookie=None):
    """
    Fetches the input for a given day from Advent of Code.

    Args:
    - day (int): The day of the Advent of Code to fetch input for.
    - year (int, optional): The year of the Advent of Code. Defaults to 2023.
    - session_cookie (str, optional): The session cookie for authentication.

    Returns:
    - str: The input data as a string.
    """
    if session_cookie is None:
        raise ValueError("Session cookie is required.")

    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cookies = {'session': session_cookie}
    response = requests.get(url, cookies=cookies)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch data: HTTP {response.status_code}")

def save_to_file(content, filename):
    """
    Saves the given content to a file.

    Args:
    - content (str): The content to save.
    - filename (str): The name of the file to save to.
    """
    with open(filename, 'w') as file:
        file.write(content)

def main(day=1, year=2023):
    try:
        # Load environment variables from .env file
        load_dotenv()
        print("Environment variables loaded.")

        # Get session cookie from environment variable
        session_cookie = os.getenv('SESSION_COOKIE')
        print(f"Session cookie: {session_cookie}")
        if not session_cookie:
            raise ValueError("Session cookie not found in environment variables.")

        # Fetch and save the input data
        input_data = fetch_aoc_input(day, session_cookie=session_cookie, year=year)
        input_data = input_data.rstrip('\n')
        save_to_file(input_data, f'inputday{day}.txt')

        print(f"Day {day} input saved to inputday{day}.txt")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    day = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    main(day)
