def square_matrix_map(matrix=[]):
    sq = list(map(lambda x: (list(map(lambda y: y**2, x))), matrix))
    return sq
