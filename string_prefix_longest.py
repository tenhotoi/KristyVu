
"""
# https://medium.com/@d_dchris/10-methods-to-solve-the-longest-common-prefix-problem-using-python-leetcode-14-a87bb3eb0f3a

With all the efforts above, interestingly, Python has a built-in commonprefix()function to solve the problem in single-line:

return os.path.commonprefix(strs)

# https://www.geeksforgeeks.org/python-ways-to-determine-common-prefix-in-set-of-strings/

Given a set of strings, find the longest common prefix. 
Examples:

Input  : {“geeksforgeeks”, “geeks”, “geek”, “geezer”}
Output : "gee"

Input  : {"apple", "ape", "april"}
Output : "ap"

# https://www.pythontutorial.net/python-string-methods/python-string-startswith/

s = 'Make it work, make it right, make it fast.'
result = s.startswith('make')
print(result)

Output: True
"""
def max_prefix0(strings):
    if len(strings) == 0:
        return ''
    
    if len(strings) == 1:
        return strings[0]
    
    prefix = ''
    tmp_pre = strings[0]

    for next in strings[1:]:
        print(f'next now is {next}')
        print(f'tmp_pre is now {tmp_pre}')
        for char in tmp_pre:
            print(f'char is now {char}')
            print(next.startswith(prefix + char))
            if next.startswith(prefix + char):
                prefix = prefix + char
                print(f'prefix is now {prefix}')
            else:
                tmp_pre = prefix
                prefix = ''
                print(f'prefix is now {tmp_pre}'.center(30, '!'))
                break
    return tmp_pre

def max_prefix(strings):
    if len(strings) == 0:
        return ''
    
    if len(strings) == 1:
        return strings[0]
    
    tmp_pre = ''
    prefix = strings[0]

    for next in strings[1:]:
        print(f'next now is {next}')
        print(f'tmp_pre is now {prefix}')
        for char in prefix:
            print(f'char is now {char}')
            print(next.startswith(tmp_pre + char))
            if next.startswith(tmp_pre + char):
                tmp_pre += char
                print(f'prefix is now {tmp_pre}')
            else:
                prefix = tmp_pre
                tmp_pre = ''
                print(f'prefix is now {prefix}'.center(30, '!'))
                break
    return prefix

def max_prefix_withsort(strings):
    print(sorted_strs := sorted(strings))
    prefix = ''
    first = sorted_strs[0]

    not_found = 0
    for char in first:
        for next in sorted_strs[1:]:
            if not next.startswith(prefix + char):
                not_found = 1
                break
        if not_found:
            break
        else:
            prefix += char

    return prefix
            
# Another way with sort, but I don't understand it: https://www.geeksforgeeks.org/longest-common-prefix-using-sorting/?ref=rp

# https://www.geeksforgeeks.org/find-the-longest-common-prefix-between-two-strings-after-performing-swaps-on-second-string/?ref=rp
def max_prefix_swapsecondstr(s, t):
    # t_sorted = ''.join(sorted(t))
    # print(f't_sorted is {t_sorted}')            # t_sorted is ddeffhjjkkrt for t = 'therfjdkfjdk', s = 'here'

    prefix = ''

    for char in s:
        print('index of char {} is : {}'.format(char, s.index(char)))
        print(f'prefix is {prefix} and char is {char}')
        if (prefix + char) in t:
            prefix += char
        else:
            break

    print('Loingest prefix found is {}'.format(prefix))
    return len(prefix)



# Driver Code
if __name__ == "__main__":
  
    input = ["geeksforgeeks", "geeks", "geek", "geezer"]
    print(pre := max_prefix(input).center(60, '='))

    input = ["apple", "ape", "april"]
    print(pre := max_prefix(input).center(60, '='))

    input = ["geeksforgeeks", "geeks", "geek", "geezer"]
    print(pre := max_prefix_withsort(input).center(60, '='))
    
    input = ["apple", "ape", "april"]
    print(pre := max_prefix_withsort(input).center(60, '='))

    print(pre := str(max_prefix_swapsecondstr('here', 'there')).center(60, '='))
    print(pre := str(max_prefix_swapsecondstr('here', 'therfjdkfjdk')).center(60, '='))
    print(pre := str(max_prefix_swapsecondstr('you', 'me')).center(60, '='))

