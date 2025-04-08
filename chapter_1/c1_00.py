"""
パタトクカシーー
"""

def main():
    s1 = "パトカー"
    s2 = "タクシー"

    concat = ""
    for s1_i, s2_i in zip(s1, s2):
        concat += s1_i + s2_i

    print(concat)


if __name__ == "__main__":
    main()
