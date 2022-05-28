# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

a = str(input("what is the first word?"))
b = str(input("what is the second word?"))

a= a.lower()
b= b.lower()



def find_anagram(word, anagram):
    # [assignment] Add your code here
    if sorted(word) == sorted (anagram):
        return True
    else:
            return False
print (find_anagram(a,b))


