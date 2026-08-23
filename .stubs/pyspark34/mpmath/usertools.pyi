def monitor(f, input: str = 'print', output: str = 'print'):
    """
    Returns a wrapped copy of *f* that monitors evaluation by calling
    *input* with every input (*args*, *kwargs*) passed to *f* and
    *output* with every value returned from *f*. The default action
    (specify using the special string value ``'print'``) is to print
    inputs and outputs to stdout, along with the total evaluation
    count::

        >>> from mpmath import *
        >>> mp.dps = 5; mp.pretty = False
        >>> diff(monitor(exp), 1)   # diff will eval f(x-h) and f(x+h)
        in  0 (mpf('0.99999999906867742538452148'),) {}
        out 0 mpf('2.7182818259274480055282064')
        in  1 (mpf('1.0000000009313225746154785'),) {}
        out 1 mpf('2.7182818309906424675501024')
        mpf('2.7182808')

    To disable either the input or the output handler, you may
    pass *None* as argument.

    Custom input and output handlers may be used e.g. to store
    results for later analysis::

        >>> mp.dps = 15
        >>> input = []
        >>> output = []
        >>> findroot(monitor(sin, input.append, output.append), 3.0)
        mpf('3.1415926535897932')
        >>> len(input)  # Count number of evaluations
        9
        >>> print(input[3]); print(output[3])
        ((mpf('3.1415076583334066'),), {})
        8.49952562843408e-5
        >>> print(input[4]); print(output[4])
        ((mpf('3.1415928201669122'),), {})
        -1.66577118985331e-7

    """
def timing(f, *args, **kwargs):
    """
    Returns time elapsed for evaluating ``f()``. Optionally arguments
    may be passed to time the execution of ``f(*args, **kwargs)``.

    If the first call is very quick, ``f`` is called
    repeatedly and the best time is returned.
    """
