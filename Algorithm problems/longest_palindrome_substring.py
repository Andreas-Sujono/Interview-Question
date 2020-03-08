class Solution:
    def longestPalindrome(self, s):
        #using dynamic programming
        start = 0
        k = 1
        maxK = 1
        n = len(s)
        table = [ [0 for i in range(n)] for j in range(n) ]
        #for k =1, it's always true
        for i in range(n):
            table[i][i] = True 
            k = 1


        #for k = 2
        for i in range(n-1):
            if(s[i] == s[i+1]):
                table[i][i+1] = True
                maxK = 2
                start = i
        
        #for k >= 3
        k = 3
        while(k <= n):
            endN = n - k + 1
            for i in range(0,endN):
                currentStart = i 
                currentEnd = i + k -1
                if(s[currentStart] == s[currentEnd] and table[currentStart+1][currentEnd-1]):
                    table[currentStart][currentEnd] = True
                    maxK = k 
                    start = i
            k += 1 
        print(maxK)
        return s[start:start+maxK]

print(Solution().longestPalindrome("babad"))
