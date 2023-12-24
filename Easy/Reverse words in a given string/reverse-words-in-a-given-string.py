# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here
        result = ""
        words = []
        curr_word = ""
        
        #initially reversing individual words of the given string one by one.
        for i in range(len(s)):
            
            #if '.' is encountered, we store the word in list.
            if(s[i] == '.'):
                words.append(curr_word)
                curr_word = ""
                
            #else adding the characters in current word in such
            #a way that original words get reversed.
            else:
                curr_word += s[i]
        
        #storing the last remaining word in list.
        words.append(curr_word)
        
        #now reversing the whole modified string by adding all 
        #the elements of list in a single string in reverse order.
        for i in range(len(words) - 1, -1, -1):
            result += words[i]
            if(i):
                result += "."
    
        #returning the result.
        return result


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends