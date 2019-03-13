# Generators

def get_multiples(num = 1, count = 10):
    '''
    Accepts a number and a count, and returns a generator that yields
    the first count multiples of the number.
    '''

    for n in range(num, (num * count) + num, num):

        yield n


# Generator Expressions

gen = (n for n in range(1, 10))
# Calling next() in a generator object yields next value till StopIteration


# Generator Memory Usage

import time


class Test:

    def __init__(self, tests):

        self._tests = []
        for t in tests:
            self._tests.append(t)


    def __test(self, func):

        print('Running test...')
        start_time = time.time()
        func()
        stop_time = time.time() - start_time
        print(f'Time: {stop_time}')


    def run_tests(self):

        for t in self._tests:
            self.__test(t)


    def add_tests(self, *tests):

        for test in tests:
            self._tests.append(test)


    @property
    def tests(self):

        return self._tests


def test_iterable():

    print(f'Iterable result: {sum([n for n in range(10000000)])}')


def test_generator():
    
    print(f'Generator result: {sum(n for n in range(10000000))}')


def main():

    tests = [test_iterable, test_generator]
    test_suite = Test(tests)
    test_suite.run_tests()


if __name__ == '__main__':

    main()
