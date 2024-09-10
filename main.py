import random
import copy
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def to_check(row, column):
    to_check = [
        [row - 1, column - 1], [row - 1, column], [row - 1, column + 1],
        [row, column - 1], [row, column + 1],
        [row + 1, column - 1], [row + 1, column], [row + 1, column + 1]
    ]
    return to_check


def get_difficulty():
    global difficulty, by, hidden_base
    difficultylist = [1, 2, 3]
    while difficulty not in difficultylist:
        difficulty = int(input("1, 2, 3: "))
        # difficulty = 1
        if difficulty == 1:
            for _ in range(10):
                base.append([])
            by = 10
        elif difficulty == 2:
            for _ in range(15):
                base.append([])
            by = 15
        elif difficulty == 3:
            for _ in range(20):
                base.append([])
            by = 20
    hidden_base = copy.deepcopy(base)


def setup():
    global base, hidden_base, difficulty, by, running
    base = []
    hidden_base = []
    difficulty = 0
    by = 0
    running = True
    get_difficulty()
    for row in hidden_base:
        for _ in range(0, by):
            row.append([])
    for row in base:
        for _ in range(0, by):
            row.append([])
    for o, row in enumerate(base):
        for j, _ in enumerate(row):
            base[o][j] = "⬜"
    for row in hidden_base:
        for i in row:
            if random.randint(0, 101) <= 25: #BOMB PERCENTAGE IMPORTANT FOR FUTURE TEST! (default 25)
                i.append("B")
            else:
                i.append(" ")
    o = -1
    g = -1
    for i in hidden_base:
        o += 1
        if o >= len(hidden_base):
            o = 0
        for j in i:
            g += 1
            if g >= len(i):
                g = 0
            if j != ["B"]:
                hidden_base[o][g] = [bombs_nearby(o, g)]
                if hidden_base[o][g] == [0]:
                    base[o][g] = "🟩"
                else:
                    base[o][g] = "⬜"


def bombs_nearby(row, column):
    global hidden_base
    nearby = 0
    for crow, ccolumn in to_check(row, column):
        if 0 <= crow < len(hidden_base) and 0 <= ccolumn < len(hidden_base[0]):
            if hidden_base[crow][ccolumn] == ["B"]:
                nearby += 1
    return nearby


color_dict = {
    0: "🟩",
    1: "🟨",
    2: "🟧",
    3: "🟥",
    4: "🟦",
    5: "🟪",
    6: "🟫",
    7: "⬛",
    8: "💀"
}

def check_win():
    global hidden_base, running, base
    hidden_b_count = 0
    base_white_count = 0
    for row in base:
        for char in row:
            if char == "⬜":
                base_white_count += 1
    for row in hidden_base:
        for char in row:
            if char == ["B"]:
                hidden_b_count += 1
                if hidden_b_count == base_white_count:
                    return True
    # input(f"{hidden_b_count}, {base_white_count}")


def handle_play():
    global running
    won = check_win()
    if won:
        print("You won!")
        input("Press |Enter| to play again ")
        running = False
        return

    while True:
        try:
            played = input("COLUMN | ROW: ")
            column, row = played.split(" ")
            row = int(row) - 1
            column = int(column) - 1
            if row > len(base[1]):
                print("Error, row exceeded")
            if column > by:
                print("Error column exceeded")
            else:
                break
        except ValueError:
            print("Error")
    if "B" in hidden_base[row][column]:
        input("You lost! Press |Enter| to accept ")
        running = False
    else:
        if hidden_base[row][column] == [0]:
            base[row][column] = "🟩"
        if hidden_base[row][column] == [1]:
            base[row][column] = "🟨"
        if hidden_base[row][column] == [2]:
            base[row][column] = "🟧"
        if hidden_base[row][column] == [3]:
            base[row][column] = "🟥"
        if hidden_base[row][column] == [4]:
            base[row][column] = "🟦"
        if hidden_base[row][column] == [5]:
            base[row][column] = "🟪"
        if hidden_base[row][column] == [6]:
            base[row][column] = "🟫"
        if hidden_base[row][column] == [7]:
            base[row][column] = "⬛"
        if hidden_base[row][column] == [8]:
            base[row][column] = "💀"


def handle_zeros():
    global base
    for row in range(len(base)):
        for column in range(len(base[row])):
            if base[row][column] == "🟩":
                for crow, ccolumn in to_check(row, column):
                    if 0 <= crow < len(hidden_base) and 0 <= ccolumn < len(hidden_base[0]):
                        if hidden_base[crow][ccolumn] == [0]:
                            base[crow][ccolumn] = "🟩"
                        elif hidden_base[crow][ccolumn] == [1]:
                            base[crow][ccolumn] = "🟨"
                        elif hidden_base[crow][ccolumn] == [2]:
                            base[crow][ccolumn] = "🟧"
                        elif hidden_base[crow][ccolumn] == [3]:
                            base[crow][ccolumn] = "🟥"
                        elif hidden_base[crow][ccolumn] == [4]:
                            base[crow][ccolumn] = "🟦"
                        elif hidden_base[crow][ccolumn] == [5]:
                            base[crow][ccolumn] = "🟪"
                        elif hidden_base[crow][ccolumn] == [6]:
                            base[crow][ccolumn] = "🟫"
                        elif hidden_base[crow][ccolumn] == [7]:
                            base[crow][ccolumn] = "⬛"
                        elif hidden_base[crow][ccolumn] == [8]:
                            base[crow][ccolumn] = "💀"


def play():
    cls()
    for number, emoji in color_dict.items():
        print(f"{number}: {emoji}")
    print("\n \n")
    o = 0
    num_marker = " "
    for i in range(len(base[0])):
        o += 1
        num_marker += str(f"{o} ")
    print(num_marker)
    o = 0
    handle_zeros()
    for i in base:
        o += 1
        line = ""
        for char in i:
            line += char
        print(f"{line}{o}")

    print("\n \n")
    # for i in hidden_base:
    # print(i)
    print("\n \n")
    handle_play()
    check_win()

while True:
    setup()
    while running:
        play()

