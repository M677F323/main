""" def main():
    yell("this is heloo world")

def yell(phrases):
        print(phrases.upper())
main() """

""" def main():
    yell("this is heloo world")

def yell(phrases):
        for phrase in phrases:
            print(phrase.upper(),end ="")
main() """


""" def main():
    yell("this", "is", "heloo", "world")

def yell(*phrases):
     upper_case=[]
     for phrase in phrases:
        upper_case.append(phrase.upper())
     print(*upper_case)
main() """

def main():
    yell("this", "is", "heloo", "world")

def yell(*phrases):
    uppercase = map(str.upper,phrases)
    print(*uppercase)
main()