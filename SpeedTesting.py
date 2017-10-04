
"""

This module contains to function decorators
that calculate the speed at which a function runs.
the clock function outputs the speed and the output of the function
it decorates and speed just outputs the speed and not the function output

"""

import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []

        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))

        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))

        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result

    return clocked


def speed(func):
    @functools.wraps(func)
    def speeded(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []

        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))

        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))

        arg_str = ', '.join(arg_list)
        print('%s(%s) - > [%0.8fs]' % (name, arg_str, elapsed))
        return result

    return speeded
