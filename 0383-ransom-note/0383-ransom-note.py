class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict1={}
        
        for i in magazine:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1

        for ch in ransomNote: 
            if ch not in dict1 or dict1[ch]==0:
                return False
            else:
                dict1[ch]-=1
        return True

            


        