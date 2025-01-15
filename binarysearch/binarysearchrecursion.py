def binarysearch(number_list,number_find,left,right,mid):
    mid=(left+right)//2
    if number_list[mid] == number_find:
            return mid
    if number_list[mid]> number_find:
           return  binarysearch(number_list,number_find,left,mid-1,mid)
    else:
             return  binarysearch(number_list,number_find,mid+1,right,mid)
    return -1   
if __name__ =='__main__':
    list=[4,9,16,25,36,46,64,81,100]  
    number=100
    left=0
    right=len(list)-1
    mid=(left+right)//2
    fun=binarysearch(list,number,left,right,mid)
    print("the index of the number is:",fun) 