from .core import *
from .helpers import any_close_tag as any_close_tag, any_open_tag as any_open_tag, delimited_list as delimited_list
from _typeshed import Incomplete

class pyparsing_common:
    """Here are some common low-level expressions that may be useful in
    jump-starting parser development:

    - numeric forms (:class:`integers<integer>`, :class:`reals<real>`,
      :class:`scientific notation<sci_real>`)
    - common :class:`programming identifiers<identifier>`
    - network addresses (:class:`MAC<mac_address>`,
      :class:`IPv4<ipv4_address>`, :class:`IPv6<ipv6_address>`)
    - ISO8601 :class:`dates<iso8601_date>` and
      :class:`datetime<iso8601_datetime>`
    - :class:`UUID<uuid>`
    - :class:`comma-separated list<comma_separated_list>`
    - :class:`url`

    Parse actions:

    - :class:`convertToInteger`
    - :class:`convertToFloat`
    - :class:`convertToDate`
    - :class:`convertToDatetime`
    - :class:`stripHTMLTags`
    - :class:`upcaseTokens`
    - :class:`downcaseTokens`

    Example::

        pyparsing_common.number.runTests('''
            # any int or real number, returned as the appropriate type
            100
            -100
            +100
            3.14159
            6.02e23
            1e-12
            ''')

        pyparsing_common.fnumber.runTests('''
            # any int or real number, returned as float
            100
            -100
            +100
            3.14159
            6.02e23
            1e-12
            ''')

        pyparsing_common.hex_integer.runTests('''
            # hex numbers
            100
            FF
            ''')

        pyparsing_common.fraction.runTests('''
            # fractions
            1/2
            -3/4
            ''')

        pyparsing_common.mixed_integer.runTests('''
            # mixed fractions
            1
            1/2
            -3/4
            1-3/4
            ''')

        import uuid
        pyparsing_common.uuid.setParseAction(tokenMap(uuid.UUID))
        pyparsing_common.uuid.runTests('''
            # uuid
            12345678-1234-5678-1234-567812345678
            ''')

    prints::

        # any int or real number, returned as the appropriate type
        100
        [100]

        -100
        [-100]

        +100
        [100]

        3.14159
        [3.14159]

        6.02e23
        [6.02e+23]

        1e-12
        [1e-12]

        # any int or real number, returned as float
        100
        [100.0]

        -100
        [-100.0]

        +100
        [100.0]

        3.14159
        [3.14159]

        6.02e23
        [6.02e+23]

        1e-12
        [1e-12]

        # hex numbers
        100
        [256]

        FF
        [255]

        # fractions
        1/2
        [0.5]

        -3/4
        [-0.75]

        # mixed fractions
        1
        [1]

        1/2
        [0.5]

        -3/4
        [-0.75]

        1-3/4
        [1.75]

        # uuid
        12345678-1234-5678-1234-567812345678
        [UUID('12345678-1234-5678-1234-567812345678')]
    """
    convert_to_integer: Incomplete
    convert_to_float: Incomplete
    integer: Incomplete
    hex_integer: Incomplete
    signed_integer: Incomplete
    fraction: Incomplete
    mixed_integer: Incomplete
    real: Incomplete
    sci_real: Incomplete
    number: Incomplete
    fnumber: Incomplete
    identifier: Incomplete
    ipv4_address: Incomplete
    ipv6_address: Incomplete
    mac_address: Incomplete
    @staticmethod
    def convert_to_date(fmt: str = '%Y-%m-%d'):
        '''
        Helper to create a parse action for converting parsed date string to Python datetime.date

        Params -
        - fmt - format to be passed to datetime.strptime (default= ``"%Y-%m-%d"``)

        Example::

            date_expr = pyparsing_common.iso8601_date.copy()
            date_expr.setParseAction(pyparsing_common.convertToDate())
            print(date_expr.parseString("1999-12-31"))

        prints::

            [datetime.date(1999, 12, 31)]
        '''
    @staticmethod
    def convert_to_datetime(fmt: str = '%Y-%m-%dT%H:%M:%S.%f'):
        '''Helper to create a parse action for converting parsed
        datetime string to Python datetime.datetime

        Params -
        - fmt - format to be passed to datetime.strptime (default= ``"%Y-%m-%dT%H:%M:%S.%f"``)

        Example::

            dt_expr = pyparsing_common.iso8601_datetime.copy()
            dt_expr.setParseAction(pyparsing_common.convertToDatetime())
            print(dt_expr.parseString("1999-12-31T23:59:59.999"))

        prints::

            [datetime.datetime(1999, 12, 31, 23, 59, 59, 999000)]
        '''
    iso8601_date: Incomplete
    iso8601_datetime: Incomplete
    uuid: Incomplete
    @staticmethod
    def strip_html_tags(s: str, l: int, tokens: ParseResults):
        '''Parse action to remove HTML tags from web page HTML source

        Example::

            # strip HTML links from normal text
            text = \'<td>More info at the <a href="https://github.com/pyparsing/pyparsing/wiki">pyparsing</a> wiki page</td>\'
            td, td_end = makeHTMLTags("TD")
            table_text = td + SkipTo(td_end).setParseAction(pyparsing_common.stripHTMLTags)("body") + td_end
            print(table_text.parseString(text).body)

        Prints::

            More info at the pyparsing wiki page
        '''
    comma_separated_list: Incomplete
    upcase_tokens: Incomplete
    downcase_tokens: Incomplete
    url: Incomplete
    convertToInteger = convert_to_integer
    convertToFloat = convert_to_float
    convertToDate = convert_to_date
    convertToDatetime = convert_to_datetime
    stripHTMLTags = strip_html_tags
    upcaseTokens = upcase_tokens
    downcaseTokens = downcase_tokens
