
"""

This module contains a function decorator that calculates the speed of a function.
It has an optional argument for whether the user wants the results of the function or just the raw speed.

"""

import time
import functools


def clock(results=None):
    def clock_wrap(func):
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
            if results == 'show':
                print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
            else:
                print('%s(%s) - > [%0.8fs]' % (name, arg_str, elapsed))

            return result

        return clocked

    return clock_wrap
