def data_types():
    my_int = 1
    my_str = "ren"
    my_float = 2.0
    my_bool = False
    my_list = [1, 2, 3]
    my_dict = {"Name":"Tema"}
    my_tuple = (1, 2, 3)
    my_set = {1, 2, 3}

    types_list = [type(my_int), type(my_str), type(my_float), type(my_bool),
    type(my_list), type(my_dict), type(my_tuple), type(my_set)]

    ## Var 1:
    print([t.__name__ for t in types_list])

    ## Var 2:
    ## formatted_list = [t.__name__ for t in types_list]
    ## print("[" + ", ".join(formatted_list) + "]")

if __name__ == '__main__':
    data_types()