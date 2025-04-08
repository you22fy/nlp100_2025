"""
タクシー
"""

def main():
    s = "パタトクカシーー"
    concat = ""
    for i in range(1, len(s), 2):
        concat += s[i]

    print(concat)

if __name__ == "__main__":
    main()
