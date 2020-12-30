from aoc.util import multiple_line_records, test_solution


def score(hand):
    total = 0
    for idx, card in enumerate(hand[::-1]):
        total += (idx+1) * card
    return total


def compute1(records):
    hand1, hand2 = [[int(n) for n in r.split(': ')[1].split()] for r in records]
    while hand1 and hand2:
        card1 = hand1.pop(0)
        card2 = hand2.pop(0)
        if card1 > card2:
            hand1.append(card1)
            hand1.append(card2)
        else:
            hand2.append(card2)
            hand2.append(card1)
    if hand1:
        return score(hand1)
    else:
        return score(hand2)


def can_recurse(val, hand):
    return val <= len(hand)


def find_winner(card1, hand1, card2, hand2):
    if can_recurse(card1, hand1) and can_recurse(card2, hand2):
        winner1, _, __ = play(hand1[:card1], hand2[:card2])
        return winner1
    else:
        return card1 > card2


def play(hand1, hand2):
    states = set()
    while hand1 and hand2:
        if (tuple(hand1), tuple(hand2)) in states:
            return True, score(hand1), score(hand2)
        else:
            states.add((tuple(hand1), tuple(hand2)))
        card1 = hand1.pop(0)
        card2 = hand2.pop(0)
        winner1 = find_winner(card1, hand1, card2, hand2)
        if winner1:
            hand1.append(card1)
            hand1.append(card2)
        else:
            hand2.append(card2)
            hand2.append(card1)

    if hand1:
        return True, score(hand1), score(hand2)
    else:
        return False, score(hand1), score(hand2)


def compute2(records):
    hand1, hand2 = [[int(n) for n in r.split(': ')[1].split()] for r in records]
    winner1, score1, score2 = play(hand1, hand2)
    return score1 if winner1 else score2


if __name__ == '__main__':
    test_data = multiple_line_records(__file__, test=True)
    data = multiple_line_records(__file__)

    test_solution(compute1, test_data, 306)
    test_solution(compute1, data, 31314)
    test_solution(compute2, test_data, 291)
    test_solution(compute2, data, 32760)
