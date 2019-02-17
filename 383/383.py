#Runtime: 44 ms
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        def helper():
            for i in set(ransomNote) & set(magazine):
                if ransomNote.count(i) > magazine.count(i):
                    return False
            return True
        return len(set(ransomNote) - set(magazine)) is 0 and helper()
#Runtime: 52 ms
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote == "":
            return True
        list = []
        for i in ransomNote:
            list.append(i)
        ransomNote = list
        while True:
            if ransomNote.count(ransomNote[0]) > magazine.count(ransomNote[0]):
                return False
            x = ransomNote.count(ransomNote[0])
            while x > 0:
                x -= 1
                ransomNote.remove(ransomNote[0])
            if len(ransomNote) == 0:
                break
        return True
#Runtime: 184 ms
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
