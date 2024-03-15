def palindrome_filter(word):
    if word == word[::-1]:
        return word


given_words = input().split()
given_palindrome = input()
palindrome_list = [word for word in given_words if palindrome_filter(word)]
print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(given_palindrome)} times")




given_words = input().split(" ")
given_palindrome = input()
palindrome_list = []
for word in given_words:
    if word == "".join(reversed(word)):
        palindrome_list.append(word)
print(f"{palindrome_list}")
print(f"Found palindrome {palindrome_list.count(given_palindrome)} times")
