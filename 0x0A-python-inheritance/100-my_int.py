#!/usr/bin/python3
"""Module 100-my_int
inherits from object int
"""


class MyInt(int):
    """inverts equal to with not eaqual to"""

    def __eq__(self, other):
        """invert to not equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """turn it to mean eaqual to"""
        return super().__eq__(other)
