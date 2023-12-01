import get_data
import datetime

# Get the current date
current_date = datetime.datetime.now()

# Extract the day number
day_number = current_date.day
year_number = current_date.year

# Get the Advent of Code input for the day
# But only if it hasn't been fetched already
try:
    with open(f'inputday{day_number}.txt', 'r') as file:
        input_data = file.read()
        print("Input data already fetched.")
except FileNotFoundError:
    input_data = get_data.main(day_number, year_number)
try:
    with open(f'day{day_number}.py', 'r') as file:
        input_data = file.read()
        print("Input data already fetched.")
except FileNotFoundError:
    with open(f'day{day_number}.py', 'w') as file:
        file.write("")
        print("Input data saved to file.")