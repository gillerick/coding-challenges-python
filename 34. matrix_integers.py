# You are given a matrix of integers field of size n × m representing a game field, and also a matrix of integers
# figure of size 3 × 3 representing a figure. Both matrices contain only 0s and 1s, where 1 means that the cell is
# occupied, and 0 means that the cell is free.
# You choose a position at the top of the game field where you put the figure and then drop it down. The figure falls
# down until it either reaches the ground (bottom of the field) or lands on an occupied cell,
# which blocks it from falling further. After the figure has stopped falling, some of the rows in the field may become
# fully occupied.
# Your task is to find the dropping position such that at least one full row is formed. As a dropping position
# you should consider the column index of the cell in game field which matches the top left corner of the figure
# 3 × 3 matrix. If there are multiple dropping positions satisfying the condition, feel free to return any of them.
# If there are no such dropping positions, return -1.
