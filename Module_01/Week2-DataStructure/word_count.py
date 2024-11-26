def word_count(file_path):
    counter = {}
    with open(file_path, 'r') as f:
        data = f.read()
    data = data.lower()
    data = data.split()
    for word in data:
        counter[word] = counter.get(word, 0) + 1
    return counter


file_path = 'P1_data.txt'
print(word_count(file_path))
