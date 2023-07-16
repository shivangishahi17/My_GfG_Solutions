#User function Template for python3

class Solution:
    def sortBySetBitCount(self, arr, n):
        # Your code goes here
        ones={}
        for i in range(n):
            ones[i]=bin(arr[i]).count("1")
        ones=sorted(ones.items(), key=lambda item:item[1], reverse=True)
        list=[]
        for k,v in ones:
            list.append(arr[k])
        arr[::]=list[::]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortBySetBitCount(arr, n)
        print(*arr)

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends