# Poker hands

import os
import numpy as np


def solve():
    data = np.loadtxt(os.path.join("..", "data", "p054.txt"),
                      delimiter=" ",
                      dtype=str)

    player1 = data[:, :5]
    player2 = data[:, 5:]

    return sum(
        score(player1[game]) > score(player2[game]) for game in range(1_000))


def score(hand):
    """Return a number representing the score of a particular hand"""

    ROYAL_FLUSH = ["T", "J", "Q", "K", "A"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    # Test for royal flush
    failed = False
    if len(set(card[1] for card in hand)) == 1:
        for card in hand:
            if card[0] not in ROYAL_FLUSH:
                failed = True
    else:
        failed = True
    if not failed:
        return 9.13

    # Test for straight flush
    failed = False
    if len(set(card[1] for card in hand)) == 1:
        indexes = []
        for card in hand:
            indexes.append(RANKS.index(card[0]))
        if max(indexes) - min(indexes) != 4:
            failed = True
        else:
            val1 = max(indexes) + 1
            if len(str(val1)) == 1:
                val1 = f"0{val1}"
    else:
        failed = True
    if not failed:
        return float(f"8.{val1}")

    # Test for four of a kind
    failed = False
    numbers = []
    for card in hand:
        numbers.append(card[0])
    mode = max(set(numbers), key=numbers.count)
    if numbers.count(mode) != 4:
        failed = True
    else:
        val1 = RANKS.index(mode) + 1
        val2 = RANKS.index([x for x in numbers if x != mode][0]) + 1
        if len(str(val1)) == 1:
            val1 = f"0{val1}"
        if len(str(val2)) == 1:
            val2 = f"0{val2}"
    if not failed:
        return float(f"7.{val1}{val2}")

    # Test for full house
    failed = False
    if len(set(card[0] for card in hand)) == 2:
        mode = max(set(numbers), key=numbers.count)
        val1 = RANKS.index(mode) + 1
        val2 = RANKS.index([x for x in numbers if x != mode][0]) + 1
        if len(str(val1)) == 1:
            val1 = f"0{val1}"
        if len(str(val2)) == 1:
            val2 = f"0{val2}"
    else:
        failed = True
    if not failed:
        return float(f"6.{val1}{val2}")

    # Test for flush
    failed = False
    if len(set(card[1] for card in hand)) == 1:
        numbers = [card[0] for card in hand]
        numbers = sorted(map(RANKS.index, numbers))
        val1 = numbers[4] + 1
        val2 = numbers[3] + 1
        val3 = numbers[2] + 1
        val4 = numbers[1] + 1
        val5 = numbers[0] + 1
        if len(str(val1)) == 1:
            val1 = f"0{val1}"
        if len(str(val2)) == 1:
            val2 = f"0{val2}"
        if len(str(val3)) == 1:
            val3 = f"0{val3}"
        if len(str(val4)) == 1:
            val4 = f"0{val4}"
        if len(str(val5)) == 1:
            val5 = f"0{val5}"
    else:
        failed = True
    if not failed:
        return float(f"5.{val1}{val2}{val3}{val4}{val5}")

    # Test for straight
    failed = False
    if len(set(card[0] for card in hand)) != 5:
        failed = True
    else:
        numbers = [card[0] for card in hand]
        numbers = sorted(map(RANKS.index, numbers))
        if numbers[4] - numbers[0] != 4:
            failed = True
        else:
            val1 = numbers[4] + 1
            if len(str(val1)) == 1:
                val1 = f"0{val1}"
    if not failed:
        return float(f"4.{val1}")

    # Test for three of a kind
    failed = False
    numbers = [card[0] for card in hand]
    mode = max(set(numbers), key=numbers.count)
    if numbers.count(mode) != 3:
        failed = True
    else:
        val1 = RANKS.index(mode) + 1
        numbers = sorted(map(RANKS.index, [x for x in numbers if x != mode]))
        val2 = numbers[1] + 1
        val3 = numbers[0] + 1
        if len(str(val1)) == 1:
            val1 = f"0{val1}"
        if len(str(val2)) == 1:
            val2 = f"0{val2}"
        if len(str(val3)) == 1:
            val3 = f"0{val3}"
    if not failed:
        return float(f"3.{val1}{val2}{val3}")

    # Test for two pairs
    failed = False
    if len(set(card[0] for card in hand)) == 3:
        numbers = [card[0] for card in hand]
        numbers = map(RANKS.index, numbers)
        numbers = sorted(numbers, reverse=True)
        numbers = sorted(numbers, key=numbers.count, reverse=True)
        val1 = numbers[0] + 1
        val2 = numbers[2] + 1
        val3 = numbers[4] + 1
        if len(str(val1)) == 1:
            val1 = f"0{val1}"
        if len(str(val2)) == 1:
            val2 = f"0{val2}"
        if len(str(val3)) == 1:
            val3 = f"0{val3}"
    else:
        failed = True
    if not failed:
        return float(f"2.{val1}{val2}{val3}")

    # Test for one pair
    failed = False
    if len(set(card[0] for card in hand)) == 4:
        numbers = [card[0] for card in hand]
        numbers = map(RANKS.index, numbers)
        numbers = sorted(numbers, reverse=True)
        numbers = sorted(numbers, key=numbers.count, reverse=True)
        val1 = numbers[0] + 1
        val2 = numbers[2] + 1
        val3 = numbers[3] + 1
        val4 = numbers[4] + 1
        if len(str(val1)) == 1:
            val1 = f"0{val1}"
        if len(str(val2)) == 1:
            val2 = f"0{val2}"
        if len(str(val3)) == 1:
            val3 = f"0{val3}"
        if len(str(val4)) == 1:
            val4 = f"0{val4}"
    else:
        failed = True
    if not failed:
        return float(f"1.{val1}{val2}{val3}{val4}")

    # Highest card
    numbers = [card[0] for card in hand]
    numbers = map(RANKS.index, numbers)
    numbers = sorted(numbers, reverse=True)
    val1 = numbers[0] + 1
    val2 = numbers[1] + 1
    val3 = numbers[2] + 1
    val4 = numbers[3] + 1
    val5 = numbers[4] + 1
    if len(str(val1)) == 1:
        val1 = f"0{val1}"
    if len(str(val2)) == 1:
        val2 = f"0{val2}"
    if len(str(val3)) == 1:
        val3 = f"0{val3}"
    if len(str(val4)) == 1:
        val4 = f"0{val4}"
    if len(str(val5)) == 1:
        val5 = f"0{val5}"
    return float(f"0.{val1}{val2}{val3}{val4}{val5}")


if __name__ == "__main__":
    print(solve())
