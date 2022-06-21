def list_division(my_list_1, my_list_2, list_length):
    """
    divides elements of lst 1 by list 2

    args:
        my_list_1: list 1
        my_list_2: list 2
        list_length: length of new list or result
    return: new list of result
    """
    result = []
    i = 0
    while i < list_length:
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            i += 1
            result.append(div)
    return result
