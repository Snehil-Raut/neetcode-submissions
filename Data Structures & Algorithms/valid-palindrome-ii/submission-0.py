class Solution:
    def is_palindrome(self,s,left,right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:

                m_left = self.is_palindrome(s,left+1,right)
                m_right = self.is_palindrome(s,left,right-1)

                if m_left == True or m_right==True:
                    return True
                    
                else:
                    return False
        return True
