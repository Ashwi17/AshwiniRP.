def count_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def main():
    s = input("Enter a string: ")
    frequency = count_frequency(s)
    
    print("Character frequency:")
    for char, count in frequency.items():
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()
