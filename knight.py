"""
Get knight to the goal without dying to a static bishop.

From https://stackoverflow.com/questions/69775315/minimum-moves-of-a-knight-with-bishop
"""

from collections import deque


def moves(n: int, start_row: int, start_column: int, end_row: int, end_column: int, bishop_row: int, bishop_column: int) -> int:
    """
    Make an n x n board and calculate how many moves it takes a bishop threatened knight to get to its destination.

    Args:
        n (int): How big to make each side of the board.
        start_row (int): Start row of knight.
        start_column (int): Start column of knight.
        end_row (int): End row of knight.
        end_column (int): End column of knight.
        bishop_row (int): Row bishop is in.
        bishop_column (int): Column bishop is in.

    Returns:
        int: How many moves it takes the knight to get to its destination. Returns -1 if unreachable.
    """
    # Deal with trivial case
    if start_row == end_row and start_column == end_column:
        return 0

    possible_moves = ((2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1))
    queue = deque()
    queue.append((start_row, start_column, True, 0))  # Include that bishop is alive
    # Let visited be a set. Mark start as visited and include alive-status
    visited = set([(start_row, start_column, True)])
    while queue:
        current_row, current_column, bishop_alive, step_count = queue.popleft()
        for row_change, column_change in possible_moves:
            new_row = current_row + row_change
            new_column = current_column + column_change
            if new_row == end_row and new_column == end_column:  # When found, don't bother about queuing it
                return step_count + 1 # No need for a res variable 
            # Update alive-state, just for current path
            bishop_alive_in_current_path = bishop_alive and (new_row != bishop_row or new_column != bishop_column)
            # Neither new_row/new_column should be negative
            if 0 <= new_row < n and 0 <= new_column < n and (new_row, new_column, bishop_alive_in_current_path) not in visited and (
                    not bishop_alive_in_current_path or abs(new_row - bishop_row) != abs(new_column - bishop_column)):
                queue.append((new_row, new_column, bishop_alive_in_current_path, step_count + 1))  # Append alive-status too
                visited.add((new_row, new_column, bishop_alive_in_current_path))  # Visited should depend on alive

    return -1
