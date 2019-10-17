l=[1,6,7,22,40]
print('existing list',l)
newlist=[]
print('newlist',newlist)
newlist=sorted(l)
print('newlist',newlist)
l.sort()
print(l)
print('descending order')
newlist=sorted(l,reverse=True)
print('newlist',newlist)
l.sort(reverse=True)
print(l)

def occurence(list,tup):
    count=0
    for i in tup:
        if i in list:
            count+=1
    return count
    
tup=('a','a','b','c')
list=['a']
print(occurence(list,tup))
