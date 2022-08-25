# Iterators and generators
# A iterator is an object that can be iterated over. --iter method, next method
# A iterator allows you to iterate over a collection of items, without storing all the items in memory, so we can store infinite amount of items. It has the mathematical formula to access the next item in the collection.

# The iterator protocol is defined as follows:
# A class is a mathematical function.

# The fibonacci sequence is a mathematical function that generates a sequence of numbers.
import time
class FiboIter():
    def __iter__(self):
        self.num1 = 0
        self.num2 = 1
        self.count = 0
        return self
    def __next__(self):
        if self.count == 0:
            self.count += 1
            return self.num1
        elif self.count == 1:
            self.count += 1
            return self.num2
        else:
            self.aux = self.num1 + self.num2
            self.num1, self.num2 = self.num2, self.aux
            self.count += 1
            return self.aux

if __name__ == '__main__':
    fibonacci = FiboIter()
    for element in fibonacci:
        if element > 100:
            break
        print(element)
        #time.sleep(0.1)
