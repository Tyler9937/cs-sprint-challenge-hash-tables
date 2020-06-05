def intersection(arrays):
    '''
    takes in nested list of numbers
    '''
    dict_list = []
    main_dict = {}

    # Turning each array into dict
    for index, array in enumerate(arrays):
        dict1 = {}
        for num in array:
            dict1.update({num: None})

        # Adding newly created dict to main dict
        if len(main_dict) == 0:
            main_dict = dict1
        else:
            main_dict = {x:dict1[x] for x in dict1
                            if x in main_dict}

    return list(main_dict)


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])


    print(intersection(arrays))
