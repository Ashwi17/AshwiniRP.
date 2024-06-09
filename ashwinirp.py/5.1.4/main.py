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

def insert_element(arr, element, position):
    arr.insert(position, element)

def delete_element(arr, position):
    if 0 <= position < len(arr):
        arr.pop(position)
    else:
        print("Invalid position!")

def main():
    n = int(input("Enter the number of elements: "))
    arr = store_elements(n)
    
    display_elements(arr)
    
    element_to_insert = int(input("Enter the element to insert: "))
    insert_position = int(input("Enter the position to insert the element: "))
    insert_element(arr, element_to_insert, insert_position)
    
    display_elements(arr)
    
    delete_position = int(input("Enter the position to delete the element: "))
    delete_element(arr, delete_position)
    
    display_elements(arr)

if __name__ == "__main__":
    main()