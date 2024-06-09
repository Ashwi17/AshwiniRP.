def search_element(arr, search):
    for i, element in enumerate(arr):
        if element == search:
            return i + 1
    return -1

def main():
    n = int(input("Enter the number of elements: "))
    arr = []
    
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)
    
    search = int(input("Enter the element to search: "))
    position = search_element(arr, search)
    
    if position != -1:
        print(f"Element found at position: {position}")
    else:
        print("Element not found in the array.")

if __name__ == "__main__":
    main()
