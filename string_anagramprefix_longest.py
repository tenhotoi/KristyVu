# https://www.geeksforgeeks.org/length-of-longest-prefix-anagram-which-are-common-in-given-two-strings/?ref=rp

# Since I don't understand their way, I created my own way:
def longest_anagram(s, t):
    min_len = min(len(s), len(t))
    max_anagram = 0

    for i in range(min_len):
        if sorted(s[:i]) == sorted(t[:i]):
            max_anagram = i

    return max_anagram

# Driver code:
if __name__ == '__main__':
    print(longest_anagram('abaabcdezzwer', 'caaabbttyh'))    
