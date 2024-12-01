def merge(arry, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arry[left + i]

    for j in range(n2):
        R[j] = arry[mid + 1 + j]

    i, j, k = 0, 0, left 

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arry[k] = L[i]
            i += 1
        else:
            arry[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arry[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arry[k] = R[j]
        j += 1
        k += 1


def separate(arry, left, right):
    if left < right:
        mid = (left + right) // 2
        separate(arry, left, mid)
        separate(arry, mid + 1, right)
        merge(arry, left, mid, right)
    return arry  

def mergeSort(arry):
    return separate(arry, 0, len(arry)-1)

def binarySearch(arry, target):
    l = 0
    r = len(arry) -1

    while l <=  r:
        m = (l+r)//2
        if arry[m] < target:
            l = m + 1
        elif arry[m] > target:
            r = m - 1
        else:
            return m
    return -1    

def input(fileName):
    arry1 = []
    arry2 = []
    with open(fileName, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                arry1.append(int(parts[0]))  
                arry2.append(int(parts[1]))  

    return arry1, arry2

def n_in_arry(arry, target):
    index = binarySearch(arry, target)
    if index == -1:
        return 0
    
    count = 1  
    left, right = index - 1, index + 1

    while left >= 0 and arry[left] == target:
        count += 1
        left -= 1

    while right < len(arry) and arry[right] == target:
        count += 1
        right += 1

    return count


def sum_of_diffrence(file):
    sum = 0
    data = input(file)
    arry1 = mergeSort(data[0])
    arry2 = mergeSort(data[1])

    for i in range(len(arry1)):
        if arry1[i] >= arry2[i]:
            sum += arry1[i] - arry2[i]
            continue
        sum += arry2[i] - arry1[i]
            
    return sum

def sum_of_similarity(file):
    sum, index = 0, 0
    data = input(file)
    arry1 = mergeSort(data[0])
    arry2 = mergeSort(data[1])

    while index < len(arry1):
        n_arry = n_in_arry(arry1, arry1[index])
        sum += n_arry * arry1[index] * n_in_arry(arry2, arry1[index])
        index += n_arry
    
    return sum


print(sum_of_similarity("input.txt"))
print(sum_of_diffrence("input.txt"))

