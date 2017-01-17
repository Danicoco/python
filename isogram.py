def is_isogram(word):
    if word == "":
        return  (word, False)
    elif type(word) != str:
        raise TypeError("Argument should be a string")
    else:
        #Now doing the real stuff :p
        
        for i in word:
            if word.count(i)>1:
                return (word, False)
        
        return (word, True)
        
print is_isogram("yeear");