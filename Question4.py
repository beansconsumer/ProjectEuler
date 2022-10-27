def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return s

    

largestPalindrome = 0
for a in range (89,10,-1):
    if a % 10 == 0:
        continue
    for b in range(999,99,-1):
        if b % 10 == 0:
            continue
        possiblePalindrome = 11 * a * b
        if possiblePalindrome < largestPalindrome:
            break
        if is_palindrome(possiblePalindrome):
            largestPalindrome = possiblePalindrome

print(largestPalindrome)
