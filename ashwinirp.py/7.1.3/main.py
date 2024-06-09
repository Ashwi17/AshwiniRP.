def remove_duplicates(s):
    unique_chars = []
    for char in s:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)

def main():
    s = input("Enter a string: ")
    result = remove_duplicates(s)
    print("String after removing duplicates:", result)

if __name__ == "__main__":
    main()
