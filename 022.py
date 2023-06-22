# Problem 022: Names Scores

def name_scores(filename):
    with open(filename, 'r') as f:
        names = f.read().replace('"', '').split(',')
        names.sort()
    total_score = 0
    for i, name in enumerate(names, start=1):
        name_score = sum(ord(char) - ord('A') + 1 for char in name)
        total_score += i * name_score
    return total_score

print(name_scores('022_names.txt'))
