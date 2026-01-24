## Given a string s containing only the characters '(' , ')' , '{' , '}' , '[' , ']', 
# determine if the input string is valid.

def isValid(s) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for check in s:
        if check in mapping:
            if not stack or stack.pop() != mapping[check]:
                return False
        else:
            stack.append(check)
    
    return not stack

# Example usage:
s1 = "{[]}"
s2 = "{{{[]}"
s3 = "()[]{}"

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))
 