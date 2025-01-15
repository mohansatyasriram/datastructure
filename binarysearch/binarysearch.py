def binarysearch(number_list,number_find):
    left=0
    right=len(number_list)-1
    while left <=right :
        mid=(left+right)//2
        if number_list[mid] == number_find:
            return mid
        if number_list[mid]> number_find:
            right = mid-1
        else:
            left=mid+1
    return -1   
if __name__ =='__main__':
    list=[4,9,16,25,36,46,64,81,100]  
    number=64
    fun=binarysearch(list,number)
    print("the index of the number is:",fun)   