class Solution:
    def isPalindrome(self, s: str) -> bool:
        m=s.lower()
        n=[]
        for i in m:
            if i.isalnum() == True:
                n.append(i)
        flag=1
        l,r=0,len(n)-1
        while l<r:
            if n[l]!=n[r]:
                flag=0
                return False
            else:
                l=l+1
                r=r-1
        if flag==1:
            return True
        