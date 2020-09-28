import json

from solver import solve


def lambda_handler(event, _context):

    grid = event['queryStringParameters']['data'] # now it's a string: '012345...'
    grid = list(map(int, grid)) # now it's 1d array

    solution = solve(grid)
    print(grid)
    print(solution)
    return {
        'statusCode': 200,
        'body': str(solution)
    }


