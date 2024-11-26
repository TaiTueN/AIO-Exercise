def character_count(word):
    character_statistic = {}
    word = word.lower()
    for char in word:
        character_statistic[char] = character_statistic.get(char, 0) + 1
    return character_statistic


print(character_count('Happiness'))
print(character_count('smiles'))
