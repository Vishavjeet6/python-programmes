#Anagram
MAX=256#ASCII
def compare(arr1,arr2):
    for i in range(MAX):
        if arr1[i]!=arr2[i]:
            return False
    return True
    
def finder(txt,pat):
    
    M=len(pat)
    N=len(txt)
    countP=[0]*MAX
    countTW=[0]*MAX
    
    for i in range(M):
        
        (countP[ord(pat[i])]) += 1
        (countTW[ord(txt[i])]) += 1
    for i in range(M,N):

        if compare(countP,countTW):
            print("Index at :",(i-M))
            
        (countTW[ord(txt[i])]) += 1
        (countTW[ord(txt[i-M])]) -= 1
    
    if compare(countP,countTW):
            print("Index at :",(N-M))
        
    
txt=input("Enter Text :")
pat=input("Enter Pattern :")
finder(txt,pat)
