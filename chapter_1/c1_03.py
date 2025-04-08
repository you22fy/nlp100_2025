"""
円周率
"""

def main():
    sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    sentence = sentence.replace(",", "").replace(".", "")
    split_sentence = sentence.split(" ")

    ans = [len(ss) for ss in split_sentence]
    print(ans)

if __name__ == "__main__":
    main()
