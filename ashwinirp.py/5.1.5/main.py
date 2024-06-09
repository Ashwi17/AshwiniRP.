import math

def store_elements(n):
    arr = []
    for i in range(n):
        element = float(input(f"Enter element {i+1}: "))
        arr.append(element)
    return arr

def calculate_mean(arr):
    return sum(arr) / len(arr)

def calculate_variance(arr, mean):
    variance = sum((x - mean) ** 2 for x in arr) / len(arr)
    return variance

def calculate_deviation(variance):
    return math.sqrt(variance)

def main():
    n = int(input("Enter the number of elements: "))
    arr = store_elements(n)
    
    mean = calculate_mean(arr)
    variance = calculate_variance(arr, mean)
    deviation = calculate_deviation(variance)
    
    print(f"The mean is: {mean}")
    print(f"The variance is: {variance}")
    print(f"The deviation is: {deviation}")

if __name__ == "__main__":
    main()
