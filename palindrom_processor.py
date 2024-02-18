from collections import deque

def is_string_palindrome(text_string):
    text_string = text_string.lower().replace(" ", "")
    
    char_queue = deque()
    for char in text_string:
        char_queue.append(char)
    
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    return True

def main():
    test_strings = ["level", "Anna", "A man a plan a canal Panama", "hello"]
    for text_string in test_strings:
        print(f"'{text_string}' is palindrome.") if is_string_palindrome(text_string) else print(f"'{text_string}' is not palindrom.")

if __name__ == "__main__":
    main()
