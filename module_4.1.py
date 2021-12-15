palindrom_list = (['kajak', 'madam', 'potop'])
word = palindrom_list
print(palindrom_list)
print(palindrom_list[::-1])

def is_palindrom(word):
    new_word = word [::-1]
    if word == new_word:
        return True
    else:
        return False