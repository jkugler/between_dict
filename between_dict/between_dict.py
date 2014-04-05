class BetweenDict(dict):
    """
    This is like a dictionary except the key is in a range between two values.
    One specifies the type of range as an interval specification.

    See the test cases for examples.
    """
    @staticmethod
    def char_to_relational(char):
        """
        Maps one of the interval characters to a relational function.
        The first element of the tuple is the name, the second is the function.
        """
        if char in '()':
            return (('less than', lambda op1,op2: op1 < op2))
        elif char in '[]':
            return (('less than or equal to', lambda op1,op2: op1 <= op2))
        else:
            raise ValueError

    def __init__(self, d={}, interval='[)'):
        """
        d - the initial dictionary
        interval - defines how endpoints are handled. Used the standard
        mathematical notation. See
          http://en.wikipedia.org/wiki/Interval_(mathematics)
        Consists of two characters. The first character can be either
          '[' (inclusive) or
          '(' (exclusive).
        The second character can be either
          ']' (inclusive), or
          ')' (exclusive).
        Exclusive means to include the range value while exclusive means to
        not. For example, an interval of '[)' (the default) and a key of (1,2)
        matches keys in the range 1 <= key < 2.
        """
        # Type check and process the interval.
        try:
            if len(interval) != 2:
                raise ValueError('Interval must have a length of 2. Length was %s' % (len(interval),))
        except TypeError:
            raise TypeError('Interval must be an iterable '
                            'with length 2: %s' % (interval,))

        try:
            (self.lower_op_name, self.lower_op) = BetweenDict.char_to_relational(interval[0])
        except ValueError:
            raise ValueError("First interval specifier must be '[' or '('.: %s" % (interval[0],))

        try:
            (self.upper_op_name, self.upper_op) = BetweenDict.char_to_relational(interval[1])
        except ValueError:
            raise ValueError("Second interval specifier must be ')' or ']'.: %s" % (interval[1],))

        # Insert the data.
        for k,v in d.items():
            self[k] = v

    def __getitem__(self, key):
        for k, v in self.items():
            if self.lower_op(k[0], key) and self.upper_op(key,  k[1]):
                return v
        raise KeyError("Key '%s' is not between any values in the BetweenDict" % key)

    def __setitem__(self, key, value):
        try:
            if len(key) == 2:
                if self.upper_op(key[0], key[1]):
                    dict.__setitem__(self, (key[0], key[1]), value)
                else:
                    raise RuntimeError('First element of a BetweenDict key (%s) '
                                       'must be %s the '
                                       'second element (%s)' % (key[0],
                                                                self.upper_op_name,
                                                                key[1]))
            else:
                raise ValueError('Key of a BetweenDict must be an iterable '
                                 'with length 2, length was %s' % (len(key),))
        except TypeError:
            raise TypeError('Key of a BetweenDict must be an iterable '
                            'with length 2: %s' % (key,))

    def __contains__(self, key):
        try:
            return bool(self[key])
        except KeyError:
            return False
