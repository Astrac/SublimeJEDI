"""
Pure Python implementation of some builtins.
This code is not going to be executed anywhere.
These implementations are not always correct, but should work as good as
possible for the auto completion.
"""


def next(iterator, default=None):
    if hasattr("next"):
        return iterator.next()
    else:
        return iterator.__next__()
    return default


def iter(collection, sentinel=None):
    if sentinel:
        yield collection()
    else:
        for c in collection:
            yield c


def range(start, stop=None, step=1):
    return [0]


class xrange():
    # Attention: this function doesn't exist in Py3k (there it is range).
    def __iter__(self):
        yield 1

    def count(self):
        return 1

    def index(self):
        return 1


#--------------------------------------------------------
# descriptors
#--------------------------------------------------------
class property():
    def __init__(self, fget, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, cls):
        return self.fget(obj)

    def __set__(self, obj, value):
        self.fset(obj, value)

    def __delete__(self, obj):
        self.fdel(obj)

    def setter(self, func):
        self.fset = func
        return self

    def getter(self, func):
        self.fget = func
        return self

    def deleter(self, func):
        self.fdel = func
        return self


class staticmethod():
    def __init__(self, func):
        self.__func = func

    def __get__(self, obj, cls):
        return self.__func


class classmethod():
    def __init__(self, func):
        self.__func = func

    def __get__(self, obj, cls):
        def _method(*args, **kwargs):
            return self.__func(cls, *args, **kwargs)
        return _method


#--------------------------------------------------------
# array stuff
#--------------------------------------------------------
class list():
    def __init__(self, iterable=[]):
        self.__iterable = []
        for i in iterable:
            self.__iterable += [i]

    def __iter__(self):
        for i in self.__iterable:
            yield i

    def __getitem__(self, y):
        return self.__iterable[y]

    def pop(self):
        return self.__iterable[-1]


class tuple():
    def __init__(self, iterable=[]):
        self.__iterable = []
        for i in iterable:
            self.__iterable += [i]

    def __iter__(self):
        for i in self.__iterable:
            yield i

    def __getitem__(self, y):
        return self.__iterable[y]

    def index(self):
        return 1

    def count(self):
        return 1


class set():
    def __init__(self, iterable=[]):
        self.__iterable = iterable

    def __iter__(self):
        for i in self.__iterable:
            yield i

    def pop(self):
        return self.__iterable.pop()

    def copy(self):
        return self


class frozenset():
    def __init__(self, iterable=[]):
        self.__iterable = iterable

    def __iter__(self):
        for i in self.__iterable:
            yield i

    def copy(self):
        return self


class dict():
    def __init__(self, **elements):
        self.__elements = elements

    def clear(self):
        # has a strange docstr
        pass

    def get(self, k, d=None):
        # TODO implement
        try:
            #return self.__elements[k]
            pass
        except KeyError:
            return d


class reversed():
    def __init__(self, sequence):
        self.__sequence = sequence

    def __iter__(self):
        for i in self.__sequence:
            yield i

    def __next__(self):
        return next(self.__iter__())

    def next(self):
        return self.__next__()


#--------------------------------------------------------
# basic types
#--------------------------------------------------------
class int():
    def __init__(self, x, base=None):
        pass


class str():
    def __init__(self, obj):
        pass

class object():
    def mro():
        """ mro() -> list
        return a type's method resolution order """
        return [object]
