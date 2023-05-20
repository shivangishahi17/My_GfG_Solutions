#User function Template for python3

class Solution:
    def minValue(self, s, k):
        # code here
        dict={}
        ans=0
        for i in s:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        list1=list(dict.values())
        while k:
            list1.sort(reverse=True)
            list1[0]=list1[0]-1
            k-=1
        
        for i in list1:
            ans+=i*i
        return ans
            
        
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends