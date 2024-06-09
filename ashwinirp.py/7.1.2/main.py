def replace_first_occurrence(s, old_char, new_char):
    new_s = ''
    found = False
    for char in s:
        if char == old_char and not found:
            new_s += new_char
            found = True
        else:
            new_s += char
    return new_s

def main():
    s = input("Enter the string: ")
    old_char = input("Enter the character to be replaced: ")
    new_char = input("Enter the character to replace with: ")
    
    result = replace_first_occurrence(s, old_char, new_char)
    print("Resultant string:", result)

if __name__ == "__main__":
    main()
