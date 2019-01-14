def check_palindrome(word):
    for i in range(len(word)/2):
        if word[i] != word[-1*(i+1)]:           # We divide the word into two halves and ensure whether the first half has the same spelling backwards to the second half
            return False                       # For example; the word 'madam', if split into 2, we would have 'mad' and 'dam'. It's a palindrome because 'dam' is 'mad' spelt backwards.
    return True

def all_palindromes(string):

    left, right = 0, len(string)
    j = right
    results = []

    while left < right -1:
        temp = string[left:j] 
        j -= 1

        if check_palindrome(temp):
            results.append(temp)

        if j < left +2:
            left += 1 
            j = right

    return list(set(results))

print all_palindromes("geeks")
print all_palindromes("madam")
