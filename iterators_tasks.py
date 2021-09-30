# get item
my_list = ['hello', 'world']


class MyContainer:

    def __init__(self, m_lst):
        self.lst = m_lst

    def __getitem__(self, key):
        try:
            return self.lst[key]
        except:
            return 'length of list(%s) is less than '

my_container = MyContainer(my_list)
print(my_container[3])


class Counter:

    def __init__(self, start, stop):
        self.start = start - 1
        self.stop = stop - 1

    def __iter__(self):
        return self

    def __next__(self):
        if isinstance(self.start, int) and isinstance(self.stop, int):
            if self.start < self.stop:
                self.start += 1
                return self.start
            raise StopIteration
        raise ArithmeticError

    # def __getitem__(self, item):


# a = Counter(1, 2.3)
for i in Counter(3, 10):
    print(i)


# another way
def my_counter(num):
    start = -1
    while num - 1 > start:
        start += 1
        yield start


gen = my_counter(5)
for i in my_counter(5):
    print(i)
# WHILE
lst = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(lst)):
    print(lst[i])

i = 0
while i < len(lst):
    print(lst[i])
    i += 1
