import string
def is_palindrome(teststr):
    punctuations = list(string.punctuation)
    teststr = teststr.lower()
    punctuations.append(" ")
    for element in teststr:
        if element in punctuations:
            teststr = teststr.replace(element, "")
    revstr = teststr[::-1]
    if revstr == teststr:
        return True
    else:
        return False
    
if __name__ == "__main__":
    total = 0
    test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.",
        "Race car!"]
    for word in test_words:
        total += is_palindrome(word)
    print(total)