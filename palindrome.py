# is it a palindrome?
def is_palindrome(word: str) -> bool:
    word = word.replace(" ", "").lower()
    return word == word[::-1] # reverse the word and compare it to the original word, Ana == anA

def run():
    word = input("Enter a word: ")
    if is_palindrome(word):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")

if __name__ == "__main__":
    print(is_palindrome("racecar")) # True
    print(is_palindrome(12321)) # we will detect this as a string, but using mypy we can detect it as a number, and it will fail. 