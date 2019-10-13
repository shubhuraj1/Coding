#Given a String Find First UpperCase

str1 = "moHit"
str2 = "Mohit"
str3 = "mOhIt"
str4 = "mohit"


# Iterative Approach
def find_uppercase_iterative(str):
    for i in range(len(str) - 1):
        if str[i].isupper():
            return str[i]
    return "No UpperCase Letter Found"


# Recursive Approach
def find_uppercase_recursive(str, index=0):
    if str[index].isupper():
        return str[index]
    if index == len(str) - 1:
        return "No Uppercase Letter Found"
    return find_uppercase_recursive(str, index + 1)


print(find_uppercase_recursive(str1))
print(find_uppercase_recursive(str2))
print(find_uppercase_recursive(str3))
print(find_uppercase_recursive(str4))
