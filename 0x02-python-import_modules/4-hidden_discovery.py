#!/usr/bin/python3

import hidden_4
if __name__ == "__main__":
    """Display function:
        prints names defined by compiled mo
        Return:
        """
    for i in dir(hidden_4):
        if i[:2] != '__':
            print(i)
