def compare_strings(str1, str2):
    if str1 == str2:
        return f"{str1} is equal to {str2}"
    elif str1 > str2:
        return f"{str1} is greater than {str2}"
    else:
        return f"{str1} is less than {str2}"

def main():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    if len(str1) == len(str2):
        print(f"{str1} length equal to {str2} length")
    else:
        print(f"{str1} length not equal to {str2} length")

    print(compare_strings(str1, str2))

if __name__ == "__main__":
    main()
