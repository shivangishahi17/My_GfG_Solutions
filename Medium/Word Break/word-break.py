#User function Template for python3

def wordBreak(line, dictionary):
    # Complete this function
    if line in dictionary:
        return True
    for i in range(1, len(line)):
        if line[0:i] in dictionary and wordBreak(line[i:], dictionary):
            return True
    return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends