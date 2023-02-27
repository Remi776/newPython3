
eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

eng_scrabble = {'AEIOULNSTR': 1,
                  'DG': 2,'BCMP': 3,
                  'FHVWY': 4, 'K': 5,
                  'JX': 8, 'QZ': 10}

rus_scrabble = {'АВЕИНОРСТ': 1,
                  'ДКЛМПУ': 2, 'БГЁЬЯ': 3,
                  'ЙЫ': 4, 'ЖЗХЦЧ': 5,
                  'ШЭЮ': 8, 'ФЩЪ': 10}

user_word = input('Enter the word: ').upper()

def ScrabblePoints():
    count = 0
    points_scrabble = dict()
    if user_word[0] in eng_alphabet:
        points_scrabble = eng_scrabble
    else:
        points_scrabble = rus_scrabble
    for char in user_word:
        for key in points_scrabble:
            if char in key:
                count += points_scrabble[key]
    return count

print('Your points:', ScrabblePoints())






