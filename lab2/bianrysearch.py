def binary_search_iterative(elements, target):
    start = 0
    end = len(elements) - 1

    while start <= end:
        
        midpoint = (start + end) // 2
        if elements[midpoint] == target:
            return midpoint
        elif target < elements[midpoint]:
            end = midpoint - 1
        else:
            start = midpoint + 1

    return None