# from random import randint

# a = []
# for i in range(10):
#     a.append(randint(1, 50))
# a.sort()
# print(a)
 
# value = int(input())
 
# mid = len(a) // 2
# low = 0
# high = len(a) - 1
 
# while a[mid] != value and low <= high:
#     if value > a[mid]:
#         low = mid + 1
#     else:
#         high = mid - 1
#     mid = (low + high) // 2
 
# if low > high:
#     print("No value")
# else:
#     print("ID =", mid)


def bubblesort(a):
    n = len(a)
    # a = []
    swapped = False

    for i in range(n):
        a.append(a)
    print(a)
    
    for i in range(n-1):
        
        for j in range(0, n-i-1):
 
            
            if a[j] > a[j + 1]:
                swapped = True
                a[j], a[j + 1] = a[j + 1], a[j]
         
        if not swapped:
            
            return
 


a = [39, 12, 18, 85, 72, 10, 2, 18]
 
print("Unsorted list is,")
print(a)
bubblesort(a)
print("Sorted Array is, ")
print(a)