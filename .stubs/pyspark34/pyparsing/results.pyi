from _typeshed import Incomplete
from collections.abc import Iterator
from typing import Tuple

str_type: Tuple[type, ...]

class _ParseResultsWithOffset:
    tup: Incomplete
    def __init__(self, p1, p2) -> None: ...
    def __getitem__(self, i): ...

class ParseResults:
    '''Structured parse results, to provide multiple means of access to
    the parsed data:

    - as a list (``len(results)``)
    - by list index (``results[0], results[1]``, etc.)
    - by attribute (``results.<results_name>`` - see :class:`ParserElement.set_results_name`)

    Example::

        integer = Word(nums)
        date_str = (integer.set_results_name("year") + \'/\'
                    + integer.set_results_name("month") + \'/\'
                    + integer.set_results_name("day"))
        # equivalent form:
        # date_str = (integer("year") + \'/\'
        #             + integer("month") + \'/\'
        #             + integer("day"))

        # parse_string returns a ParseResults object
        result = date_str.parse_string("1999/12/31")

        def test(s, fn=repr):
            print("{} -> {}".format(s, fn(eval(s))))
        test("list(result)")
        test("result[0]")
        test("result[\'month\']")
        test("result.day")
        test("\'month\' in result")
        test("\'minutes\' in result")
        test("result.dump()", str)

    prints::

        list(result) -> [\'1999\', \'/\', \'12\', \'/\', \'31\']
        result[0] -> \'1999\'
        result[\'month\'] -> \'12\'
        result.day -> \'31\'
        \'month\' in result -> True
        \'minutes\' in result -> False
        result.dump() -> [\'1999\', \'/\', \'12\', \'/\', \'31\']
        - day: \'31\'
        - month: \'12\'
        - year: \'1999\'
    '''
    class List(list):
        '''
        Simple wrapper class to distinguish parsed list results that should be preserved
        as actual Python lists, instead of being converted to :class:`ParseResults`:

            LBRACK, RBRACK = map(pp.Suppress, "[]")
            element = pp.Forward()
            item = ppc.integer
            element_list = LBRACK + pp.delimited_list(element) + RBRACK

            # add parse actions to convert from ParseResults to actual Python collection types
            def as_python_list(t):
                return pp.ParseResults.List(t.as_list())
            element_list.add_parse_action(as_python_list)

            element <<= item | element_list

            element.run_tests(\'\'\'
                100
                [2,3,4]
                [[2, 1],3,4]
                [(2, 1),3,4]
                (2,3,4)
                \'\'\', post_parse=lambda s, r: (r[0], type(r[0])))

        prints:

            100
            (100, <class \'int\'>)

            [2,3,4]
            ([2, 3, 4], <class \'list\'>)

            [[2, 1],3,4]
            ([[2, 1], 3, 4], <class \'list\'>)

        (Used internally by :class:`Group` when `aslist=True`.)
        '''
        def __new__(cls, contained: Incomplete | None = None): ...
    def __new__(cls, toklist: Incomplete | None = None, name: Incomplete | None = None, **kwargs): ...
    def __init__(self, toklist: Incomplete | None = None, name: Incomplete | None = None, asList: bool = True, modal: bool = True, isinstance=...) -> None: ...
    def __getitem__(self, i): ...
    def __setitem__(self, k, v, isinstance=...) -> None: ...
    def __delitem__(self, i) -> None: ...
    def __contains__(self, k) -> bool: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __iter__(self) -> Iterator: ...
    def __reversed__(self) -> Iterator: ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def haskeys(self) -> bool:
        """
        Since ``keys()`` returns an iterator, this method is helpful in bypassing
        code that looks for the existence of any defined results names."""
    def pop(self, *args, **kwargs):
        '''
        Removes and returns item at specified index (default= ``last``).
        Supports both ``list`` and ``dict`` semantics for ``pop()``. If
        passed no argument or an integer argument, it will use ``list``
        semantics and pop tokens from the list of parsed tokens. If passed
        a non-integer argument (most likely a string), it will use ``dict``
        semantics and pop the corresponding value from any defined results
        names. A second default return value argument is supported, just as in
        ``dict.pop()``.

        Example::

            numlist = Word(nums)[...]
            print(numlist.parse_string("0 123 321")) # -> [\'0\', \'123\', \'321\']

            def remove_first(tokens):
                tokens.pop(0)
            numlist.add_parse_action(remove_first)
            print(numlist.parse_string("0 123 321")) # -> [\'123\', \'321\']

            label = Word(alphas)
            patt = label("LABEL") + Word(nums)[1, ...]
            print(patt.parse_string("AAB 123 321").dump())

            # Use pop() in a parse action to remove named result (note that corresponding value is not
            # removed from list form of results)
            def remove_LABEL(tokens):
                tokens.pop("LABEL")
                return tokens
            patt.add_parse_action(remove_LABEL)
            print(patt.parse_string("AAB 123 321").dump())

        prints::

            [\'AAB\', \'123\', \'321\']
            - LABEL: \'AAB\'

            [\'AAB\', \'123\', \'321\']
        '''
    def get(self, key, default_value: Incomplete | None = None):
        '''
        Returns named result matching the given key, or if there is no
        such name, then returns the given ``default_value`` or ``None`` if no
        ``default_value`` is specified.

        Similar to ``dict.get()``.

        Example::

            integer = Word(nums)
            date_str = integer("year") + \'/\' + integer("month") + \'/\' + integer("day")

            result = date_str.parse_string("1999/12/31")
            print(result.get("year")) # -> \'1999\'
            print(result.get("hour", "not specified")) # -> \'not specified\'
            print(result.get("hour")) # -> None
        '''
    def insert(self, index, ins_string) -> None:
        '''
        Inserts new element at location index in the list of parsed tokens.

        Similar to ``list.insert()``.

        Example::

            numlist = Word(nums)[...]
            print(numlist.parse_string("0 123 321")) # -> [\'0\', \'123\', \'321\']

            # use a parse action to insert the parse location in the front of the parsed results
            def insert_locn(locn, tokens):
                tokens.insert(0, locn)
            numlist.add_parse_action(insert_locn)
            print(numlist.parse_string("0 123 321")) # -> [0, \'0\', \'123\', \'321\']
        '''
    def append(self, item) -> None:
        '''
        Add single element to end of ``ParseResults`` list of elements.

        Example::

            numlist = Word(nums)[...]
            print(numlist.parse_string("0 123 321")) # -> [\'0\', \'123\', \'321\']

            # use a parse action to compute the sum of the parsed integers, and add it to the end
            def append_sum(tokens):
                tokens.append(sum(map(int, tokens)))
            numlist.add_parse_action(append_sum)
            print(numlist.parse_string("0 123 321")) # -> [\'0\', \'123\', \'321\', 444]
        '''
    def extend(self, itemseq) -> None:
        '''
        Add sequence of elements to end of ``ParseResults`` list of elements.

        Example::

            patt = Word(alphas)[1, ...]

            # use a parse action to append the reverse of the matched strings, to make a palindrome
            def make_palindrome(tokens):
                tokens.extend(reversed([t[::-1] for t in tokens]))
                return \'\'.join(tokens)
            patt.add_parse_action(make_palindrome)
            print(patt.parse_string("lskdj sdlkjf lksd")) # -> \'lskdjsdlkjflksddsklfjkldsjdksl\'
        '''
    def clear(self) -> None:
        """
        Clear all elements and results names.
        """
    def __getattr__(self, name): ...
    def __add__(self, other) -> ParseResults: ...
    def __iadd__(self, other) -> ParseResults: ...
    def __radd__(self, other) -> ParseResults: ...
    def as_list(self) -> list:
        '''
        Returns the parse results as a nested list of matching tokens, all converted to strings.

        Example::

            patt = Word(alphas)[1, ...]
            result = patt.parse_string("sldkj lsdkj sldkj")
            # even though the result prints in string-like form, it is actually a pyparsing ParseResults
            print(type(result), result) # -> <class \'pyparsing.ParseResults\'> [\'sldkj\', \'lsdkj\', \'sldkj\']

            # Use as_list() to create an actual list
            result_list = result.as_list()
            print(type(result_list), result_list) # -> <class \'list\'> [\'sldkj\', \'lsdkj\', \'sldkj\']
        '''
    def as_dict(self) -> dict:
        '''
        Returns the named parse results as a nested dictionary.

        Example::

            integer = Word(nums)
            date_str = integer("year") + \'/\' + integer("month") + \'/\' + integer("day")

            result = date_str.parse_string(\'12/31/1999\')
            print(type(result), repr(result)) # -> <class \'pyparsing.ParseResults\'> ([\'12\', \'/\', \'31\', \'/\', \'1999\'], {\'day\': [(\'1999\', 4)], \'year\': [(\'12\', 0)], \'month\': [(\'31\', 2)]})

            result_dict = result.as_dict()
            print(type(result_dict), repr(result_dict)) # -> <class \'dict\'> {\'day\': \'1999\', \'year\': \'12\', \'month\': \'31\'}

            # even though a ParseResults supports dict-like access, sometime you just need to have a dict
            import json
            print(json.dumps(result)) # -> Exception: TypeError: ... is not JSON serializable
            print(json.dumps(result.as_dict())) # -> {"month": "31", "day": "1999", "year": "12"}
        '''
    def copy(self) -> ParseResults:
        """
        Returns a new copy of a :class:`ParseResults` object.
        """
    def get_name(self):
        '''
        Returns the results name for this token expression. Useful when several
        different expressions might match at a particular location.

        Example::

            integer = Word(nums)
            ssn_expr = Regex(r"\\d\\d\\d-\\d\\d-\\d\\d\\d\\d")
            house_number_expr = Suppress(\'#\') + Word(nums, alphanums)
            user_data = (Group(house_number_expr)("house_number")
                        | Group(ssn_expr)("ssn")
                        | Group(integer)("age"))
            user_info = user_data[1, ...]

            result = user_info.parse_string("22 111-22-3333 #221B")
            for item in result:
                print(item.get_name(), \':\', item[0])

        prints::

            age : 22
            ssn : 111-22-3333
            house_number : 221B
        '''
    def dump(self, indent: str = '', full: bool = True, include_list: bool = True, _depth: int = 0) -> str:
        '''
        Diagnostic method for listing out the contents of
        a :class:`ParseResults`. Accepts an optional ``indent`` argument so
        that this string can be embedded in a nested display of other data.

        Example::

            integer = Word(nums)
            date_str = integer("year") + \'/\' + integer("month") + \'/\' + integer("day")

            result = date_str.parse_string(\'1999/12/31\')
            print(result.dump())

        prints::

            [\'1999\', \'/\', \'12\', \'/\', \'31\']
            - day: \'31\'
            - month: \'12\'
            - year: \'1999\'
        '''
    def pprint(self, *args, **kwargs) -> None:
        '''
        Pretty-printer for parsed results as a list, using the
        `pprint <https://docs.python.org/3/library/pprint.html>`_ module.
        Accepts additional positional or keyword args as defined for
        `pprint.pprint <https://docs.python.org/3/library/pprint.html#pprint.pprint>`_ .

        Example::

            ident = Word(alphas, alphanums)
            num = Word(nums)
            func = Forward()
            term = ident | num | Group(\'(\' + func + \')\')
            func <<= ident + Group(Optional(delimited_list(term)))
            result = func.parse_string("fna a,b,(fnb c,d,200),100")
            result.pprint(width=40)

        prints::

            [\'fna\',
             [\'a\',
              \'b\',
              [\'(\', \'fnb\', [\'c\', \'d\', \'200\'], \')\'],
              \'100\']]
        '''
    def __getnewargs__(self): ...
    def __dir__(self): ...
    @classmethod
    def from_dict(cls, other, name: Incomplete | None = None) -> ParseResults:
        """
        Helper classmethod to construct a ``ParseResults`` from a ``dict``, preserving the
        name-value relations as results names. If an optional ``name`` argument is
        given, a nested ``ParseResults`` will be returned.
        """
    asList = as_list
    asDict = as_dict
    getName = get_name
