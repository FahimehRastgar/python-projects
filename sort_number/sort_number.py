def sorted_number ():

    numbers_list_string = input("Enter your numbers (seperated by space):")
    numbers_list = numbers_list_string.split(" ")
    #print(numbers_list)
    numbers = [int(x) for x in numbers_list]
    #print (numbers)

    x = sorted(numbers)


    numbers2 = [str(i) for i in x]



    print(' '.join(numbers2))
    

sorted_number()