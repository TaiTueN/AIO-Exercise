def levenshtein(src, tar):
    m = len(src)
    n = len(tar)

    distances = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        distances[i][0] = i

    for i in range(n+1):
        distances[0][i] = i

    for i in range(1, m+1):
        for j in range(1, n+1):
            if src[i-1] == tar[j-1]:
                distances[i][j] = distances[i-1][j-1]
            else:
                distances[i][j] = 1 + min(distances[i][j-1],
                                          distances[i-1][j], distances[i-1][j-1])
    return distances[m][n]


print(levenshtein('kitten', 'sitting'))
print(levenshtein('yu', 'you'))
print(levenshtein('hi', 'hello'))
print(levenshtein('hola', 'hello'))
