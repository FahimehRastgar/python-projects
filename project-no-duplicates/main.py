def find_duplicate():

    x = input("enter a sentence :")
    x2 = x.lower().split(" ")

    count = 0
    for word1 in range(0, len(x2)): 
        for word2 in range(word1+1, len(x2)):
            if x2[word1] == x2[word2]: 
                count = 1
                break

    if count == 1:
        print("yes")
    else:
        print("no")


find_duplicate()