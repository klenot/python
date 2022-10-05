#imported modules
import random

# global constants
MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1

ROWS = 5
COLS = 3

symbol_count = {
    "A": 3,
    "B": 4,
    "C": 5,
    "D": 6
}

symbol_value = {
    "A": 8,
    "B": 7,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# a function for the slot machine interface
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def deposit():
    # I am starting with a deposit amount check function
    while True:
        amount = input("How much you would like to deposit? €")
        # the isdigit method has to be before the convert method otherwise it would not work (we can't
        # convert a string into an integer)
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                # here the function breaks if everything thus far is True
                break
            else:
                print("Amount has to be greater than zero.")
        else:
            print("Please, enter a number.")

    return amount


# Basically the check deposit function runs until it gets a valid input of a digit (integer) that is greater than zero.

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please, enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("How much you would like to bet on each line? €")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount has to be between €{MIN_BET} - €{MAX_BET}.")
        else:
            print("Please, enter a number.")

    return amount

# the main function starts here
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        # let's check if the player has sufficient funds for the game
        if total_bet > balance:
            print(
                f"You have insufficient funds for the bet. Your current balance is €{balance}.")
        else:
            break

    print(f"You are betting €{bet} on {lines} lines. Total bet is equal to €{total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won: €{winnings}.")
    print(f"You win on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is €{balance}.")
        answer = input("Press enter to play or 'Q' to quit the slot machine.")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with €{balance}.")

main()
