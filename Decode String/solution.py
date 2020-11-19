class Solution:
    def decodeString(self, s: str) -> str:
        # loop through string and append brackets to stack
        inside_str = ""
        multiplier = ""
        rtn_str = int(multiplier) * inside_str

        
        for i in range(len(s)):
            char = s[i]
            char_next = s[i + 1]
            if char.isdigit():
                multiplier += char
            if char.isalpha():
                inside_str += char
            if char == "[":
               inside_str += self.decodeString(s[char + 1:])
            if char == "]":
                return rtn_str

        

        # base case: hit a closing bracket

        # if it detect an integer and the next el isn't an integer, store
        #if it comes across an open bracket, call the function
        # if it detect letters and the next element isn't a leetter, store it

        # return string
class Solution2:
    def decodeString(self, s):
        it, num, stack = 0, 0, [""]
        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] == "[":
                stack.append(num)
                num = 0
                stack.append("")
            elif s[it] == "]":
                str1 = stack.pop()
                rep = stack.pop()
                str2 = stack.pop()
                stack.append(str2 + str1 * rep)
            else:
                stack[-1] += s[it]              
            it += 1           
        return "".join(stack)