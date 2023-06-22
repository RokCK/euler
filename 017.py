# Problem 017: Number Letter Counts

def number_letter_counts():
    words = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
             11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
             15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
             19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
             50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
             90: 'ninety', 1000: 'onethousand'}
    for i in range(21, 1000):
        if i not in words:
            if i < 100:
                words[i] = words[i // 10 * 10] + words[i % 10]
            else:
                words[i] = words[i // 100] + 'hundred'
                if i % 100:
                    words[i] += 'and' + words[i % 100]
    return sum(len(word) for word in words.values())

print(number_letter_counts())
