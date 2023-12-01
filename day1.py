def main():
    file = read_file()
    print("This is the part1 answer: " + str(part1(file)))
    print("This is the part2 answer: " + str(part2(file)))

def read_file():
    with open('inputday1.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
    return lines

def part1(x):
    sum = 0
    digits = ""
    for line in x:
        for char in line:
            if char.isdigit():
                digits += char
                break
        for char in reversed(line):
            if char.isdigit():
                digits += char
                break
        sum += int(digits)
        digits = ""
    return sum

def part2(x):
    total_sum = 0
    digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for line in x:
        first_num = ""
        last_num = ""

        # Find the first number
        for i in range(len(line)):
            if line[i].isdigit():
                first_num = line[i]
                break
            else:
                for word, digit in digit_map.items():
                    if line.startswith(word, i):
                        first_num = digit
                        break
                if first_num:
                    break

        # Find the last number
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                last_num = line[i]
                break
            else:
                for word, digit in digit_map.items():
                    if line.endswith(word, 0, i + 1):
                        last_num = digit
                        break
                if last_num:
                    break

        # Add the numbers to the total sum if both are found
        if first_num and last_num:
            total_sum += int(first_num + last_num)

    return total_sum
    

if __name__ == '__main__':
    main()