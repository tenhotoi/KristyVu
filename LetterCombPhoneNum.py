# https://leetcode.com/problems/letter-combinations-of-a-phone-number/solutions/8063/python-solution/
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations1(self, digits: str):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if (len(digits) == 0) or (len(digits) > 4) or ('1' in digits) or ('0' in digits):
            return 'Invalid input'

        try:
            num = int(digits)
        except:
            return 'Invalid input'
        else:
            if num < 0 :
                return 'Invalid input'
        
        if len(digits) == 1:
            return list(mapping[digits])

        print('checking digits[:-1]: ', digits[:-1])
        prev = self.letterCombinations1(digits[:-1])
        print('checking digits[-1]: ', digits[-1])
        additional = mapping[digits[-1]]
        print('prev is now: ', prev)
        print('additional is now: ', additional)
        return [s + c for s in prev for c in additional]

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        interpret_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}

        if (len(digits) == 0) or (len(digits) > 4) or ('1' in digits) or ('0' in digits):
            return 'Invalid input'

        try:
            num = int(digits)
        except:
            return 'Invalid input'
        else:
            if num < 0 :
                return 'Invalid input'
        
        if len(digits) == 1:
            return list(interpret_digit[digits])

        all_combinations = [''] if digits else []
        for digit in digits:
            current_combinations = list()
            for letter in interpret_digit[digit]:
                for combination in all_combinations:
                    current_combinations.append(combination + letter)
            all_combinations = current_combinations
        return all_combinations

    def letterCombinations3(self, digits):
        dictionary = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
            '8':"tuv", '9':"wxyz"}
    
        if (len(digits) == 0) or (len(digits) > 4) or ('1' in digits) or ('0' in digits):
            return 'Invalid input'

        try:
            num = int(digits)
        except:
            return 'Invalid input'
        else:
            if num < 0 :
                return 'Invalid input'
        
        if len(digits) == 1:
            return list(dictionary[digits])

        cmb = [''] if digits else []
        for d in digits:
            cmb = [p + q for p in cmb for q in dictionary[d]]
        return cmb

    def letterCombinations4(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_ = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        if (len(digits) == 0) or (len(digits) > 4) or ('1' in digits) or ('0' in digits):
            return 'Invalid input'

        try:
            num = int(digits)
        except:
            return 'Invalid input'
        else:
            if num < 0 :
                return 'Invalid input'
        
        if len(digits) == 1:
            return list(map_[digits])

        result = []
        
        def make_combinations(i, cur):
            if i == len(digits):
                if len(cur) > 0:
                    result.append(''.join(cur))
                return
            for ch in map_[digits[i]]:
                cur.append(ch)
                make_combinations(i+1, cur)
                cur.pop()
        
        make_combinations(0, [])
        
        return result

    def letterCombinations5(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if (len(digits) == 0) or (len(digits) > 4) or ('1' in digits) or ('0' in digits):
            return 'Invalid input'

        try:
            num = int(digits)
        except:
            return 'Invalid input'
        else:
            if num < 0 :
                return 'Invalid input'
        
        if len(digits) == 1:
            return list(mapping[digits])

        if not digits: return ''
        prev, additional = mapping[digits[0]], self.letterCombinations5(digits[1:])
        return prev if not additional else [a + b for a in prev for b in additional]

    def letterCombinations6(self, digits):
        MAPPING = ('0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')

        if (len(digits) == 0) or (len(digits) > 4) or ('1' in digits) or ('0' in digits):
            return 'Invalid input'

        try:
            num = int(digits)
        except:
            return 'Invalid input'
        else:
            if num < 0 :
                return 'Invalid input'

        res = ['']
        for d in digits:
            res = [pre + cur for pre in res for cur in MAPPING[int(d)]]
        return res if len(digits) > 0 else []

    def letterCombinations7(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if (len(digits) == 0) or (len(digits) > 4) or ('1' in digits) or ('0' in digits):
            return 'Invalid input'

        try:
            num = int(digits)
        except:
            return 'Invalid input'
        else:
            if num < 0 :
                return 'Invalid input'
        
        if len(digits) == 1:
            return list(mapping[digits])

        # cmb = [''] if digits else []
        cmb = ['']
        for d in digits:
            print(d, digits, ":\n")
            print(cmb := [p + q for p in cmb for q in mapping[d]])

        return cmb

"""
        letters = test().letterCombinations1(each)
        print(letters)

        letters = test().letterCombinations2(each)
        print(letters)

        letters = test().letterCombinations3(each)
        print(letters)

        letters = test().letterCombinations4(each)
        print(letters)

        letters = test().letterCombinations5(each)
        print(letters)

        letters = test().letterCombinations6(each)
        print(letters)  
"""

if __name__ == '__main__':
    test = Solution    
    for each in ['23', '1', '', '2', '-2', '191919', '123kdfjkd', '780', '8847', '123', '456732']:
    # for each in ['8847']:
        print("\n", each, ":\n", test().letterCombinations7(each))  

"""
2 23 :

['a', 'b', 'c']
3 23 :

['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

 23 :
 ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

 1 :
 Invalid input

  :
 Invalid input

 2 :
 ['a', 'b', 'c']

 -2 :
 Invalid input

 191919 :
 Invalid input

 123kdfjkd :
 Invalid input

 780 :
 Invalid input
8 8847 :

['t', 'u', 'v']
8 8847 :

['tt', 'tu', 'tv', 'ut', 'uu', 'uv', 'vt', 'vu', 'vv']
4 8847 :

['ttg', 'tth', 'tti', 'tug', 'tuh', 'tui', 'tvg', 'tvh', 'tvi', 'utg', 'uth', 'uti', 'uug', 'uuh', 'uui', 'uvg', 'uvh', 'uvi', 'vtg', 'vth', 'vti', 'vug', 'vuh', 'vui', 'vvg', 'vvh', 'vvi']
7 8847 :

['ttgp', 'ttgq', 'ttgr', 'ttgs', 'tthp', 'tthq', 'tthr', 'tths', 'ttip', 'ttiq', 'ttir', 'ttis', 'tugp', 'tugq', 'tugr', 'tugs', 'tuhp', 'tuhq', 'tuhr', 'tuhs', 'tuip', 'tuiq', 'tuir', 'tuis', 'tvgp', 'tvgq', 'tvgr', 'tvgs', 'tvhp', 'tvhq', 'tvhr', 'tvhs', 'tvip', 'tviq', 'tvir', 'tvis', 'utgp', 'utgq', 'utgr', 'utgs', 'uthp', 'uthq', 'uthr', 'uths', 'utip', 'utiq', 'utir', 'utis', 'uugp', 'uugq', 'uugr', 'uugs', 'uuhp', 'uuhq', 'uuhr', 'uuhs', 'uuip', 'uuiq', 'uuir', 'uuis', 'uvgp', 'uvgq', 'uvgr', 'uvgs', 'uvhp', 'uvhq', 'uvhr', 'uvhs', 'uvip', 'uviq', 'uvir', 'uvis', 'vtgp', 'vtgq', 'vtgr', 'vtgs', 'vthp', 'vthq', 'vthr', 'vths', 'vtip', 'vtiq', 'vtir', 'vtis', 'vugp', 'vugq', 'vugr', 'vugs', 'vuhp', 'vuhq', 'vuhr', 'vuhs', 'vuip', 'vuiq', 'vuir', 'vuis', 'vvgp', 'vvgq', 'vvgr', 'vvgs', 'vvhp', 'vvhq', 'vvhr', 'vvhs', 'vvip', 'vviq', 'vvir', 'vvis']

 8847 :
 ['ttgp', 'ttgq', 'ttgr', 'ttgs', 'tthp', 'tthq', 'tthr', 'tths', 'ttip', 'ttiq', 'ttir', 'ttis', 'tugp', 'tugq', 'tugr', 'tugs', 'tuhp', 'tuhq', 'tuhr', 'tuhs', 'tuip', 'tuiq', 'tuir', 'tuis', 'tvgp', 'tvgq', 'tvgr', 'tvgs', 'tvhp', 'tvhq', 'tvhr', 'tvhs', 'tvip', 'tviq', 'tvir', 'tvis', 'utgp', 'utgq', 'utgr', 'utgs', 'uthp', 'uthq', 'uthr', 'uths', 'utip', 'utiq', 'utir', 'utis', 'uugp', 'uugq', 'uugr', 'uugs', 'uuhp', 'uuhq', 'uuhr', 'uuhs', 'uuip', 'uuiq', 'uuir', 'uuis', 'uvgp', 'uvgq', 'uvgr', 'uvgs', 'uvhp', 'uvhq', 'uvhr', 'uvhs', 'uvip', 'uviq', 'uvir', 'uvis', 'vtgp', 'vtgq', 'vtgr', 'vtgs', 'vthp', 'vthq', 'vthr', 'vths', 'vtip', 'vtiq', 'vtir', 'vtis', 'vugp', 'vugq', 'vugr', 'vugs', 'vuhp', 'vuhq', 'vuhr', 'vuhs', 'vuip', 'vuiq', 'vuir', 'vuis', 'vvgp', 'vvgq', 'vvgr', 'vvgs', 'vvhp', 'vvhq', 'vvhr', 'vvhs', 'vvip', 'vviq', 'vvir', 'vvis']
 
 123 :
 Invalid input

 456732 :
 Invalid input
 """            
