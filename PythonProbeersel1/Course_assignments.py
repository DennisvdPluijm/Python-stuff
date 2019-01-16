import random


def user_input(s_input, b_float=False):
    # request valid user input, default integer
    while True:
        keyb_input = input(s_input+": ")
        try:
            if b_float:
                proc_input = float(keyb_input)
            else:
                proc_input = int(keyb_input)
            break  # jumps out of the while loop
        except ValueError:
            if b_float:
                print("Invalid entry. Please provide a valid number (e.g. '2.5')")
            elif keyb_input in ["Done", "done"]:
                proc_input = keyb_input
                break
            elif len(keyb_input) < 1:  # check for empty line
                proc_input = "Done"
                break
            else:
                print("Invalid entry. Please provide a valid integer")
    return proc_input


def compute_pay():
    name = input("What is your name? ")
    print("Hello", name + "! I can calculate your pay.")

    f_hours = user_input("Number of hours", True)
    f_rate = user_input("Pay rate", True)

    pay = min(f_hours, 40) * f_rate
    if f_hours > 40:
        pay = pay + (f_hours - 40) * (f_rate * 1.5)

    print("Your pay is: {pay:5.2f} euros".format(pay=pay))


def random_number_game():
    # find largest number & calculate sum
    no_items = user_input("Number of random integers")
    print("Define range of random numbers...")
    start_range = max(user_input("  Range starts at (min 0)"), 0)
    end_range = min(user_input("  Range ends at (max 100)"), 100)
    largest_so_far = None
    running_total = 0
    found42 = False
    #todo waiting time
    print("Randomizing...")
    print("\nindex | number | largest so far | running total")
    print("-------------------------------------------------")
    for count, number in enumerate(random.sample(range(start_range, end_range), no_items), start=1):
        if largest_so_far is None:
            largest_so_far = number
        elif number > largest_so_far:
            largest_so_far = number
        running_total = running_total + number
        print("{0:5} | {1:6} | {2:14} | {3:8}".format(count, number, largest_so_far, running_total))
        if number == 42:
            found42 = True
            break
    print("\nLargest number is:", largest_so_far)
    print("Sum of all numbers is:", running_total)
    print("The average number equals:", float(running_total)/count)
    print("Found number 42?", found42)


def number_list():
    user_list = list()
    while True:
        inp = user_input("Enter a number, or type 'Done' to end")
        if inp in ["Done", "done"]:
            break
        user_list.append(inp)
    sum_list = 0
    for count, number in enumerate(user_list, start=1):
        sum_list += number
    print("Average: {avg:2.2f}".format(avg=float(sum_list)/count))


def text_tests():
    text = input("What is the text? ")
    matched_letter = input("Which letter to count? ")
    # TODO add check on input == 1
    #index = 0
    match = 0
    for letter in text:
        # print(letter)  # letter can be used as the iteration variable
        if letter.lower() == matched_letter:  # helpful: use dir(variable) to find all allowed methods for that type
            match += 1  # matches letter ignoring case
    print("Letter '{0}' matched {1} times".format(matched_letter, match))
    print("Text sliced up to, but not including, character #10: ", text[:10])  # in Python, index # is BEFORE character
    # position, not AT character position:
    #  b a n a n a
    # 0 1 2 3 4 5 6
    print("Does the text contain 'x'? {answer}".format(answer='x' in text))
    # TODO add .replace('e','3'), .strip() (removes whitespace at begin and end), .startswith('A')
    try:
        apos = text.lower().find('a')  # what if no or multiple a?
        zpos = text.lower().find('z', apos)  # find z, starts at a position
        print("Text between 'a' and 'z': ", text[apos + 1:zpos].strip())  # prints text between first a and z
    except:
        print("Text doesn't contain 'a' and 'z'")
    string1 = "d.vdpluijm@ofdataanalytics.com SENT: 30-11-2018"
    string2 = "X-DSPAM-Confidence: 0.875"
    print("Example string 1 to parse: ", string1)
    at = string1.find('@')
    com = string1.find(' ')
    domain = string1[at+1:com]
    print("  Domain: ", domain)
    print("Example string 2 to parse: ", string2)
    valuepos = string2.find(':')
    try:
        value = float(string2[valuepos+1:].strip())
        print("  Value: ", value, type(value))
    except ValueError:
        print("  ERROR: Could not convert to a number...")


if __name__ == '__main__':
    # TODO let user select the function
    #pay_compute()
    #random_number_game()
    #number_list()
    text_tests()
