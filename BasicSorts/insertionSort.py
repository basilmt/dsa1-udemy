def insertionSort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j >= 0:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1

    return my_list


l = [4,2,6,5,1,3]
print(insertionSort(l))