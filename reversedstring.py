s = "hello"
k=s[::-1]
print(list(reversed(s)))
print(k)

# two pointer
from typing import List
def reverseString(s: List[str]):
    l=0
    r=len(s)-1
    while (l<r):
        s[l],s[r]=s[r],s[l]
        l,r=l+1,r-1
    else:
        return s    
print(reverseString(["h","e","l","l","o"]))


# stack method
from typing import List
def rev(ar: List[str]):
    stack=[]
    for b in ar:
        stack.append(b)
    i=0
    while stack:
        ar[i]=stack.pop()
        i+=1
    else:
        return ar
#  driver code  
def main():
    ar = ["h","e","l","l","o"]
    print(rev(ar));
     
if __name__=="__main__":
    main()
    
       




# list comprehrnsion
def reverse(string):
    string = [string[i] for i in range(len(string)-1, -1, -1)]
    return "".join((string))

print (reverse("Natty"))




# using object
class gfg:
    nom = ['h', 'e', 'l', 'l', 'o']
    def __reversed__(self):
        return reversed(self.nom)
 
if __name__ == '__main__':
    obj = gfg()
    print(list(reversed(obj)))