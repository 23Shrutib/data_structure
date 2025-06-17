#List
#Note:-for loop can be used anywhere(when you know the definite times to run the loop) and for in loop only in data structure

#List:-
'''
a=[13,12,16,'a',8.3]
#  0   1  2  3  4
#  -5 -4 -3 -2 -1

#accessing single element:-
print(a[1])
print(a[-1])

#accessing multiple elements:-
for i in a:
    print(i)

#calculate length:-
print(len(a))

#check element exists or not:-
if 15 in a:
    print("exists")
else:
    print("not exists")

#change/update element:-
a[1]=100
print(a)
'''
#########################################

#List Methods:-
'''
a=[11,14,10,11,23,43,21]

#append
a.append(31)
print(a)

#clear
a.clear()
print(a)

#copy
new_a=a.copy()
print(new_a)

#count
c=a.count(11)
print(c)

#extend
a.extend([22,33,44])
print(a)

#index
i=a.index(43)
print(a[i])

#insert
a.insert(2,66) #on 2nd index add 66
print(a)

#pop
i=a.index(23)
a.pop(i)
print(a)

#remove
a.remove(43)
print(a)
'''
'''
#sort
a.sort()
print(a)

#reverse
a.reverse()
print(a)
'''




#Tuple
'''
a=(10,20,'a',4.5,10)

#accessing single element:-
print(a[1])
print(a[-2])

#for loop can be used anywhere and for in loop only in data structure

#accessing multiple elements:-
for i in a:
    print(i)

#calculate length:-
    print(len(a))

#check element exists or not:-
    if 15 in a:
        print("exists")
    else:
        print("not exists")

#change/update element:-
#Tuple is immutable, element values cannot be changed
a[1]=100
print(a) #error

#count
c=a.count(10)
print(c)

#index
i=a.index('a')
print(a[i])

'''


#Set
'''
s={10,20,33,'a',8.6,10}

#accessing multiple elements:-
for i in s:
    print(i)

#calculate length:-
print(len(s))

#check element exists or not:-
if 12 in s:
        print("exists")
else:
        print("not exists")
'''
'''
s={10,20,30,44,1.5,'a'}

#add
s.add(11)
print(s)

#clear
s.clear()
print(s)  #o/p:-set()

new_s=s.copy()
print(new_s)
'''

#remove error deta h discard nahi deta h error
'''
#pop
s.pop()
print(s)
'''
'''
#remove
s.remove(30)
print(s)
'''
'''
#discard
s.discard(300)
print(s)
'''

'''
#update
s.update({10,20,4,5,6})
print(s)
'''

#Union,Intersection,Difference
'''
s1={10,20,30,40,50}
s2={11,22,33,10,20}
'''

'''
u=s1.union(s2)
print(u)
'''

'''
i=s1.intersection(s2)
print(i)
'''

'''
d=s1.difference(s2)
print(d)
'''
'''
d=s2.difference(s1)
print(d)
'''


'''
#Dictionary:-
d={'roll':22,'name':'shruti','marks':75.8}

#accessing single element:-
print(d['roll'])

#accessing multiple elements:-
for i in d:
    print(d[i])

#length
print(len(d))
'''

'''
#update
d['name']="raj"
print(d)
'''



#Methods:-
'''
d={'roll':22,'name':'shruti','marks':75.8}
'''
'''
#clear
d.clear()
print(d)
'''
'''
#copy
new_d=d.copy()
print(new_d)
'''

'''
k=(1,2,3,4)
v='a'
new_d=dict.fromkeys(k,v)
print(new_d)
'''

'''
#get
v=d.get('roll','element not found')
print(v)

#items
new_d=d.items()
print(new_d)

#keys
k=d.keys()
print(k)

#values
v=d.values()
print(v)
'''


'''
#update
#for changing/updating values
d.update({'name':'rahul'})
print(d)


#for adding element
d.update({'city':'pune'})
print(d)

#pop  #pop mein any element according to our wish delete hota h!
d.pop('name','not found')
print(d)

#popitem    #popitem mein last element delete hota h!
d.popitem()
print(d)
'''


#Data structure Type Conversion:-

#list
'''
a=[10,20,30,40,50]

#list into tuple
t=tuple(a)
print(t)

#list into set
s=set(a)
print(s)
'''


#tuple
'''
a=(10,20,30,40,50)

#tuple into list
l=list(a)
print(l)

#tuple into set
s=set(a)
print(s)
'''

#set
a={10,20,30,40,50}

#set into list
l=list(a)
print(l)

#set into tuple
t=tuple(a)
print(t)
