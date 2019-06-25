def sum_all(n):

    if len(str(n)) == 1:
        return n
    else:
        return (n%10 + sum_all(n/10))
        # another solution can be using split. split function is use for string and give list

def word_split(phrase, list_of_words, output=None):
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)
    return output

print(sum_all(424234))
print(word_split('rwerwefwerwe'))