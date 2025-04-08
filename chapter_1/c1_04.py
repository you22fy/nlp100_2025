"""
元素記号
"""

from collections import defaultdict

def main():
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"
    split_sentence = sentence.split(" ")
    get_one_idx = [1,5,6,7,8,9,15,16,19]
    ans = defaultdict(int)

    for idx, ss_i in enumerate(split_sentence):
        if idx + 1 in get_one_idx:
            ans[ss_i[0]] = idx + 1
        else:
            ans[ss_i[:2]] = idx + 1

    for k, v in sorted(ans.items(), key=lambda x: x[1]):
        print(k, v)


if __name__ == "__main__":
    main()
