a=[45,54]
b=[15,45]
row="surya"
print("(ard)%s"%row)

for x in a:
    print(x)
print("----"*15)    
for x in "alex":
    print(x)
    if x=="l":
        print("l is reached")
        continue
print("----"*15)     
for x in range(2,4):
    print(x)
    if x=="l":
        print("l is reached")
        continue

for n in a:
    for n1 in b:
        print(n+n1)