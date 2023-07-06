#User function Template for python3


class Solution:
    def minFlips(self, S):
        # Code here
        counter1=0
        counter2=0
        for i in range(len(S)):
            if i&1 and S[i]=='0':
                counter1+=1
            if i%2==0 and S[i]=='1':
                    counter1+=1
            if i&1 and S[i]=='1':
                    counter2+=1
            if i%2==0 and S[i]=='0':
                counter2+=1
        return min(counter1, counter2)
        
        
        # flips=0 #8
        # for i in range(len(S)):
        #     if(i%2==0):
        #         if(S[i]=='0'):
        #             flips+=1
        #     elif(i%2!=0):
        #         if(S[i]=='1'):
        #             flips+=1
        # return min(flips,len(S)-flips) #min(1,2)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        Obj=Solution()
        ans=Obj.minFlips(S)
        print(ans)
# } Driver Code Ends