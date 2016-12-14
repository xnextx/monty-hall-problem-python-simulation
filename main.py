from random import randint

# Many wins players.
player_1_wins = 0
player_2_wins = 0

number_of_trials = 500

for y in range(number_of_trials):
    boxes = ["[ ]", "[ ]", "[ ]"]

    # I random box with a win.
    random_index = randint(0, 2)
    boxes[random_index] = "[ $$ ]"

    # I delete a random empty box.
    for index, val in enumerate(boxes, start=0):
        if index != random_index:
            boxes.pop(index)
            break

    # If player_1 not change his mind.
    if boxes[0] == "[ $$ ]":
        player_1_wins += 1
    else:
        player_2_wins += 1

print("WooW O.o")
print("Player 1 wins: %s | Player 2 wins: %s" % (player_1_wins, player_2_wins))
