class Sol:
    def mountain_arr_index(self,arr):
        left , right=0, len(arr)
        while True:
            mid=(left+right)//2
            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                return mid
            elif arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]:
                left=mid
            elif arr[mid]<arr[mid-1] and arr[mid]>arr[mid+1]:
                right=mid

if __name__ == '__main__':
    p = Sol()
    print(p.mountain_arr_index(arr=[24,69,100,99,79,78,67,36,26,19]))
