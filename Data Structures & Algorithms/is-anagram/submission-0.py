class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_occurances = {}
        t_occurances = {}
        for character in s:
            if character not in s_occurances: 
                s_occurances[character] = 1
            else:
                s_occurances[character] += 1

        for character in t:
            if character not in t_occurances:
                t_occurances[character] = 1
            else: 
                t_occurances[character] += 1


        if s_occurances != t_occurances:
            return False
        else: 
            return True
        