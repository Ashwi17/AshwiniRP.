def find_largest_and_smallest(arr):
    largest = arr[0]
    smallest = arr[0]
    
    for num in arr:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    
    return largest, smallest

def main():
    n = int(input("Enter the number of elements: "))
    arr = []
    
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)
    
    largest, smallest = find_largest_and_smallest(arr)
    
    print(f"The largest element is: {largest}")
    print(f"The smallest element is: {smallest}")

if __name__ == "__main__":
    main()
