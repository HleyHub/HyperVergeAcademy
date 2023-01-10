# Determine if a word or phrase is an isogram.

# An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

#Examples of isograms:

# lumberjacks
# background
# downstream
# six-year-old

# The word *isograms*, however, is not an isogram, because the s repeats.

# Take a string as an input and print the following:
# 'Yes' if it is an isogram
# 'No' if it is not an isogram

def is_isogram(string):
    pass
    for item in string:
        space = " "
        hyphen = "-"
        if string.count(item) > 1:
            return False
        elif string.count(space) > 1 or string.count(hyphen) > 1:
            return True
        else:
            pass
    return True

word = input("Enter a word: ")
iso = is_isogram(word)
if iso == True:
    print("Yes")
else:
    print("No")