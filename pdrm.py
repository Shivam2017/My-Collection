a="mam"
rev=""
l=len(a)-1
while(l>=0):
    rev=rev+a[l]
    l=l-1
if(rev==a):
    print("p")
else:
    print("n p")
