
def input(file_path):
    arry = []
    with open(file_path, 'r') as file:
        for line in file:
            arry.append([int(num) for num in line.split()])
    return arry

def small_to_big(arry):
    for i in range(0, len(arry)-1):
        if ((arry[i] > arry[i+1]) or ((arry[i+1] - arry[i]) > 3) or ((arry[i]-arry[i+1]) == 0)):
            return 0 
    return 1


def big_to_small(arry):
    for i in range(0, len(arry)-1):
        if (arry[i] < arry[i+1]) or ((arry[i] - arry[i+1]) > 3) or ((arry[i+1]-arry[i]) == 0):
            return small_to_big(arry) 
    return 1


def check(file):
    data, sum = input(file), 0
    for sub in data:
        sum += big_to_small(sub)
    return sum


print(check("input.txt"))