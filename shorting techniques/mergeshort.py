def split(arr):
   if len(arr) <= 1:
      return arr
   mid = len(arr) // 2
   left = split(arr[:mid])
   right = split(arr[mid:])
   return merge(left, right)

def merge(left, right):
    l = 0
    r = 0
    merged = []
    
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    
    merged.extend(left[l:])
    merged.extend(right[r:])
    
    return merged

if __name__ == '__main__':
   arr = [2, 3, 5, 1]
   sorted_arr = split(arr)
   print(sorted_arr)
