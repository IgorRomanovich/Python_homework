# Напишите функцию для нахождения k-го минимального элемента (k_min), используя алгоритм представленный в лекции.
# Предусмотрите обработку исключительных ситуаций.


def exep(A, n):
    ln = len(A)
    if ln == 0:
        print("EmptyError: array is empty")
        exit()
    if ln == 1:
        return A[0]
    if ln < n:
        print("SizeError: k is more than the length of the array")
        exit()


def srchIndq(A, left, right, q):
    p = A[q]
    A[q] = A[right]
    A[right] = p
    l = left
    for j in range(left, right):
        if A[j] <= p:
            tmp = A[l]
            A[l] = A[j]
            A[j] = tmp
            l = l + 1
    tmp = A[l]
    A[l] = A[right]
    A[right] = tmp
    return l


def k_min(A, left, right, n):
    q = srchIndq(A, left, right, (left + right) // 2)
    if left == right:
        return A[left]
    if q == n:
        return A[q]
    if n < q:
        return k_min(A, left, q - 1, n)
    elif n > q:
        return k_min(A, q + 1, right, n)


lst = input("Write list:").split()
try:
    for i in range(len(lst)):
        a = int(lst[i])
except ValueError:
    print("TypeError: array contains different types")
    exit()
print(f"Our list {lst}")
try:
    k = int(input("k:"))
except ValueError:
    print("TypeError: k is not an integer")
    exit()
exep(lst, k)
print(f"Result: {k_min(lst, 0, len(lst) - 1, k - 1)}")
