class Solution:
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        maxLength = 0
        currentLength = 0
        pointer1 = 0

        for i in range(0,len(s)):
            if(s[i] not in hashmap or hashmap[s[i]] == 0):
                hashmap[s[i]] = 1
                currentLength += 1
            else:
                while(hashmap[s[i]] != 0 and pointer1 <= i):
                    hashmap[s[pointer1]] = 0
                    pointer1 += 1
                    currentLength -= 1
                hashmap[s[i]] = 1
                currentLength += 1

            if(currentLength > maxLength):
                maxLength = currentLength
            
            print(s[pointer1:i+1], maxLength)

        return maxLength

print(Solution().lengthOfLongestSubstring("pwwkew"))
# 10