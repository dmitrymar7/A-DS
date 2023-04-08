
import random


def heapSort(array):

    for i in range(len(array) // 2 - 1, -1, -1):
        heapify(array, len(array), i)

    for i in range(len(array) - 1, -1, -1):
        array[0], array[i] = array[i], array[0]

        heapify(array, i, 0)


def heapify(array, heapSize, index):

    largest = index
    leftChild = 2 * index + 1
    rightChild = 2 * index + 2

    if leftChild < heapSize and array[leftChild] > array[largest]:
        largest = leftChild

    if rightChild < heapSize and array[rightChild] > array[largest]:
        largest = rightChild

    if largest != index:
        array[index], array[largest] = array[largest], array[index]

        heapify(array, heapSize, largest)


def ex():
    n = 10
    lst = [random.randint(0, 10) for _ in range(n)]
    print(lst)
    heapSort(lst)
    print(lst)


if __name__ == '__main__':
    ex()
