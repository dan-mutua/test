
def find_max_min(matrix):
    output = []
    for i, row in enumerate(matrix):
        max_value = max(row)
        max_index = row.index(max_value)
        is_min = True
        for j in range(len(matrix)):
            if matrix[j][max_index] < max_value:
                is_min = False
                break
        if is_min:
            output.append(max_value)
    return output

matrix1 = [[5,16,20],[9,11,18],[15,16,17]]
print(find_max_min(matrix1))  # Output: [17]

matrix2 = [[100,60,20, 50],[70,80,10,90],[10,50,44,30]]
print(find_max_min(matrix2))  # Output: [50]


# def test_find_max_min():
#     # Test 1
#     matrix1 = [[5, 16, 20], [9, 11, 18], [15, 16, 17]]
#     assert find_max_min(matrix1) == [17]

#     # Test 2
#     matrix2 = [[100, 60, 20, 50], [70, 80, 10, 90], [10, 50, 44, 30]]
#     assert find_max_min(matrix2) == [50]

#     # Test 3: Minimum and maximum value are the same
#     matrix3 = [[2, 1], [1, 2]]
#     assert find_max_min(matrix3) == [2]

#     # Test 4: Multiple values meet criteria
#     matrix4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     assert find_max_min(matrix4) == [3, 6, 9]

#     # Test 5: Matrix with a single value
#     matrix5 = [[5]]
#     assert find_max_min(matrix5) == [5]

#     print("All tests pass")

# test_find_max_min()

    