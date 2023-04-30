# Input: ransomNote = "aa", magazine = "aab"
# Output: true



def canConstruct(ransomNote, magazine):
    s = len(ransomNote)
    n = len(magazine)
    count = 0
    for i in ransomNote.split():
        if i in magazine.split():
            magazine.remove(i)
            count+=1
    if count == s: return True
    return False

ransomNote = "aa"
magazine = "aab"


ransomNote = "aab"
magazine = "baa"
print(canConstruct(ransomNote, magazine))