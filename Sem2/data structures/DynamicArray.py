class DynamicArray:
    def __init__(self, custom_resize_factor=2):
        self.__size = 0
        self.__capacity = 1
        self.__resize_factor = custom_resize_factor
        self.__array = [None] * self.__capacity

    def __resize(self):
        new_capacity = self.__capacity * self.__resize_factor
        new_array = [None] * new_capacity
        for i in range(self.__size):
            new_array[i] = self.__array[i]
        self.__array = new_array
        self.__capacity = new_capacity

    def insertAt(self, index, element):
        if index < 0 or index > self.__size:
            raise IndexError("Index out of bounds")
        if self.__size == self.__capacity:
            self.__resize()
        for i in range(self.__size, index, -1):
            self.__array[i] = self.__array[i - 1]
        self.__array[index] = element
        self.__size += 1

    def deleteAt(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.__size - 1):
            self.__array[i] = self.__array[i + 1]
        self.__size -= 1

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def rotateByK(self, k):
        k = k % self.__size
        self.__array = self.__array[-k:] + self.__array[:-k]

    def reverse(self):
        for i in range(self.__size // 2):
            self.__array[i], self.__array[self.__size - i - 1] = self.__array[self.__size - i - 1], self.__array[i]

    def append(self, element):
        if self.__size == self.__capacity:
            self.__resize()
        self.__array[self.__size] = element
        self.__size += 1

    def prepend(self, element):
        self.insertAt(0, element)

    def merge(self, other):
        merged_array = DynamicArray(max(self.__resize_factor, other.__resize_factor))
        for i in range(self.__size):
            merged_array.append(self.__array[i])
        for i in range(other.size()):
            merged_array.append(other.__array[i])
        return merged_array

    def interleave(self, other):
        interleaved_array = DynamicArray(max(self.__resize_factor, other.__resize_factor))
        i, j = 0, 0
        while i < self.__size or j < other.size():
            if i < self.__size:
                interleaved_array.append(self.__array[i])
                i += 1
            if j < other.size():
                interleaved_array.append(other.__array[j])
                j += 1
        return interleaved_array

    def mid(self):
        if self.isEmpty():
            return None
        return self.__array[self.__size // 2]

    def search(self, element):
        for i in range(self.__size):
            if self.__array[i] == element:
                return i
        return -1

    def splitAt(self, index):
        if index < 0 or index > self.__size:
            raise IndexError("Index out of bounds")
        first_half = DynamicArray(self.__resize_factor)
        second_half = DynamicArray(self.__resize_factor)
        for i in range(index):
            first_half.append(self.__array[i])
        for i in range(index, self.__size):
            second_half.append(self.__array[i])
        return first_half, second_half

    def __str__(self):
        return str(self.__array[:self.__size])

# Usage example
arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)
print(arr)
arr.insertAt(1, 4)
print(arr)
arr.deleteAt(2)
print(arr)
print(arr.size())
print(arr.isEmpty())
arr.rotateByK(1)
print(arr)
arr.reverse()
print(arr)
arr.prepend(5)
print(arr)
arr2 = DynamicArray()
arr2.append(6)
arr2.append(7)
merged = arr.merge(arr2)
print(merged)
interleaved = arr.interleave(arr2)
print( interleaved)
print(arr.mid())
print(arr.search(2))
split1, split2 = arr.splitAt(2)
print(split1)
print(split2)
