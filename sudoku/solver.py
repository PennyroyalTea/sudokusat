import pycosat


def construct_clauses(grid):
    # var in [0, 728]: value * 81 + pos

    clauses = []
    # initials: restricitions set by initial numbers
    for pos, val in enumerate(grid):
        val -= 1
        if val >= 0:
            clauses.append([val * 81 + pos + 1])
    # rows : every value should exist in every row
    for row in range(9):
        for val in range(9):
            clause = []
            for pos in range(row * 9, (row + 1) * 9):
                clause.append(val * 81 + pos + 1)
            clauses.append(clause)
    # cols : every value should exist in every col
    for col in range(9):
        for val in range(9):
            clause = []
            for pos in range(col, 81, 9):
                clause.append(val * 81 + pos + 1)
            clauses.append(clause)
    # boxes : every value should exist in every box
    box_adds = [0, 1, 2, 9, 10, 11, 18, 19, 20]
    box_firsts = [0, 3, 6, 27, 30, 33, 54, 57, 60]
    for first in box_firsts:
        for val in range(9):
            clause = []
            for add in box_adds:
                clause.append(val * 81 + (first + add) + 1)
            clauses.append(clause)
    # cells exist: every cell contains atleast one number
    for pos in range(81):
        clause = []
        for val in range(9):
            clause.append(val * 81 + pos + 1)
        clauses.append(clause)
    # cells determined: every cell contains no more than one number
    for pos in range(81):
        for val1 in range(9):
            for val2 in range(val1 + 1, 9):
                clauses.append([-(val1 * 81 + pos + 1), -(val2 * 81 + pos + 1)])
    return clauses

def solution_to_grid(solution):
    res = [-1] * 81
    for val in solution:
        if val > 0:
            color = (val - 1) // 81
            pos = (val - 1) % 81
            res[pos] = color + 1
    return res

def solve(grid):
    clauses = construct_clauses(grid)
    solution = pycosat.solve(clauses)
    if solution in ['UNSAT', 'UNKNOWN']:
        return solution
    return solution_to_grid(solution)