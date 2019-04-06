inputText = input("Enter string you want to check: ")


def reverse(reverse_string):
    return reverse_string[::-1]


def ispalindrome(reverse_string):
    rev = reverse(reverse_string)
    if reverse_string == rev:
        return True
    return False


reverseString = inputText
ans = ispalindrome(reverseString)

if ans == 1:
    print("Yes")
else:
    print("No")