def is_isogram(word):
    if word == "":
        return  (word, False)
    elif type(word) != str:
        raise TypeError("Argument should be a string")
    else:
        if len(set(word)) == len(word):
            return (word, True)
        else:
            return (word, False)
        
print is_isogram("sh");