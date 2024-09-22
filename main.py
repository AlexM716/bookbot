def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        words = text.split()
        alphadict = {}
        lowertext = text.lower()
        for c in lowertext:
            if c in alphadict:
                alphadict[c] += 1
            else:
                alphadict[c] = 1

        print("--- REPORT ---")
        for c in alphadict:
            print(f"The character {c} was found {alphadict[c]} times.")
main()