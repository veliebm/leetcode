"""
Get knight to the goal without dying to a static bishop.

From https://stackoverflow.com/questions/69775315/minimum-moves-of-a-knight-with-bishop
"""

from collections import deque


def moves(n: int, startRow: int, startCol: int, endRow: int, endCol: int, bishopRow: int, bishopCol: int) -> int:
    """
    Make an n x n board and calculate how many moves it takes a bishop threatened knight to get to its destination.

    Args:
        n (int): How big to make each side of the board.
        startRow (int): Start row of knight.
        startCol (int): Start column of knight.
        endRow (int): End row of knight.
        endCol (int): End column of knight.
        bishopRow (int): Row bishop is in.
        bishopCol (int): Column bishop is in.

    Returns:
        int: How many moves it takes the knight to get to its destination. Returns -1 if unreachable.
    """    
    if startRow == endRow and startCol == endCol:  # Deal with trivial case
        return 0
    moves = ((2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1))
    queue = deque()
    queue.append((startRow, startCol, True, 0))  # Include that bishop is alive
    # Let visited be a set. Mark start as visited and include alive-status
    visited = set([(startRow, startCol, True)])
    while queue:
        i, j, alive, steps = queue.popleft()
        for di, dj in moves:
            cr = i + di
            cc = j + dj
            if cr == endRow and cc == endCol:  # When found, don't bother about queuing it
                return steps + 1 # No need for a res variable 
            # Update alive-state, just for current path
            stillalive = alive and (cr != bishopRow or cc != bishopCol)
            # Neither cr/cc should be negative
            if 0 <= cr < n and 0 <= cc < n and (cr, cc, stillalive) not in visited and (
                    not stillalive or abs(cr - bishopRow) != abs(cc - bishopCol)):
                queue.append((cr, cc, stillalive, steps + 1))  # Append alive-status too
                visited.add((cr, cc, stillalive))  # Visited should depend on alive
    return -1
