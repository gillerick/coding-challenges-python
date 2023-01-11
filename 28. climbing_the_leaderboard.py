def climbing_leader_board(ranked, player):
    unique_ranked = list(sorted(set(ranked), reverse=True))
    for game in player:
        unique_ranked.append(game)
        print(list(sorted(unique_ranked, reverse=True)).index(game) + 1, end="\n")


if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    climbing_leader_board(ranked, player)
