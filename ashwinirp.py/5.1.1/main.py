def store_elements(n):
    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)
    return arr

def display_elements(arr):
    print("The elements of the array are:")
    for element in arr:
        print(element, end=' ')
    print()

def main():
    n = int(input("Enter the number of elements: "))
    arr = store_elements(n)
    display_elements(arr)

if __name__ == "__main__":
    main()
