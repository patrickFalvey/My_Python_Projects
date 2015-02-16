code = input("Please enter your code to be cracked here")
code_dict = {"a": "c", "b": "d", "c": "e", "d": "f", "e": "g", "f": "h", "g": "i", "h": "j", "i": "k", "j": "l", "k": "m", "l": "n", "m": "o", "n": "p", "o": "q", "p": "r", "q": "s", "r": "t", "s": "u", "t": "v", "u": "w", "v": "x", "w": "y", "x": "z", "y": "a", "z": "b"}
solution =  str("")
for c in str(code):
    if c != " ":
        if c in code_dict.keys():
            solution = solution + code_dict[c]
        else: solution = solution + str(c)
    else:
        solution = solution + str(" ")
print(solution)

    
        
    
