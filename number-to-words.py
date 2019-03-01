one=["", "one ", "two ", "three ", "four ","five ", "six ", "seven ",
     "eight ","nine ", "ten ", "eleven ", "twelve ",
     "thirteen ", "fourteen ", "fifteen ","sixteen ",
     "seventeen ", "eighteen ","nineteen "]
ten=["", "", "twenty ", "thirty ", "forty ","fifty ", "sixty ",
     "seventy ", "eighty ", "ninety "]
    
def numTowords(n,s):
    str = ""
    if n>19:
        str += ten[n//10] + one[n%10]
    else:
        str += one[n]
    if n:
        str += s

    return str
def convertowords(n):
    out = ""
    out += numTowords((n//10000000),"crore ")
    out += numTowords((n//100000)%100,"lakh ")
    out += numTowords((n//1000)%100,"thousand ")
    out += numTowords((n//100)%10,"hundred ")

    if n>100 and n%100:
        out += "and "
    out += numTowords(n%100,"")
    return out
t=int(input())
for i in range(t):
    n=int(input())
    print(convertowords(n))
