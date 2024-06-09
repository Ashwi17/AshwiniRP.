def string_length(s):
    return len(s)

def string_copy(s):
    return s

def string_concatenate(s1, s2):
    return s1 + s2

def string_to_uppercase(s):
    return s.upper()

def compare_strings(s1, s2):
    if s1 < s2:
        return "First string is alphabetically before second string."
    elif s1 > s2:
        return "Second string is alphabetically before first string."
    else:
        return "Both strings are equal alphabetically."

def main():
    first_string = input("Enter the first string: ")
    second_string = input("Enter the second string: ")

    print("Length of first string:", string_length(first_string))
    print("Length of second string:", string_length(second_string))

    print("Copy of first string:", string_copy(first_string))

    concatenated_string = string_concatenate(first_string, second_string)
    print("Concatenation of both strings:", concatenated_string)

    print("Uppercase of first string:", string_to_uppercase(first_string))

    print(compare_strings(first_string, second_string))

if __name__ == "__main__":
    main()
