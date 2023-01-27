""" def main():
    yell("this is heloo world")

def yell(phrases):
        print(phrases.upper())
main() """

def main():
    yell("this is heloo world")

def yell(phrases):
        for phrase in phrases:
            print(phrase.upper(),end ="")
main()