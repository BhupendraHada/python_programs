"""
Q) how to get player with maximum runs in tuple format like (player_name, runs)
"""

data = {'match1': {'player1': 57, 'player2': 38}, 'match2': {'player3': 9, 'player1': 42},'match3':
    {'player2': 41, 'player4': 63, 'player3': 91}}


def orange_cap(d):
    from collections import Counter
    c = Counter()
    for key, value in d.items():
        c.update(Counter(value))
    max_scorer = max(c.items(), key=lambda t: t[1])
    print max_scorer
    return max_scorer

    # Second Trick below:
    # player = {}
    # for key, value in d.items():
    #     for i, k in value.items():
    #         if i not in player:
    #             player[i] = k
    #         else:
    #             player[i] += k
    # print player
    # max_scorer = max(player.items(), key=lambda t: t[1])


if __name__ == "__main__":
    orange_cap(data)
