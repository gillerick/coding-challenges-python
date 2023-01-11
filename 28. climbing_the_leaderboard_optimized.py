from bisect import bisect_right


def climbing_leader_board(ranked, player):
    set_ranks = list(set(ranked))
    unique_ranks = list(set_ranks)
    unique_ranks.sort()
    ranks = []
    for game in player:
        if game in set_ranks:
            ranks.append(len(set_ranks) - set_ranks.index(game))
        else:
            idx = bisect_right(unique_ranks, game)
            rank = len(unique_ranks) - idx + 1
            ranks.append(rank)
            unique_ranks.insert(idx, game)
    for rank in ranks:
        print(rank, end="\n")


if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    climbing_leader_board(ranked, player)
