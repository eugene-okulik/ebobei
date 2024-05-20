text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

modified_words = []
for word in text.split():
    if word.endswith(','):
        modified_word = word[:-1] + 'ing' + ','
    elif word.endswith('.'):
        modified_word = word[:-1] + 'ing' + '.'
    else:
        modified_word = word + 'ing'
    modified_words.append(modified_word)
modified_text = ' '.join(modified_words)
print(modified_text)
