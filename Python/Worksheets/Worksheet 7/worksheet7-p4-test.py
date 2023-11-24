def compute_moving_average(nested_list):
    rows = len(nested_list)
    cols = len(nested_list[0])
    averaged_list = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            adjacent_cells = [
                nested_list[x][y] for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                if 0 <= x < rows and 0 <= y < cols
            ]
            average = sum(adjacent_cells) / len(adjacent_cells) if adjacent_cells else 0
            averaged_list[i][j] = round(average)

    return averaged_list

if __name__ == "__main__":
    nested_list = [[1, 4, 0, 1, 3, 1], 
                   [2, 2, 4, 2, 2, 3], 
                   [1, 0, 1, 0, 1, 0]]

    averaged_list = compute_moving_average(nested_list)
    print(averaged_list)