#Q1 - Febonocci series

num1=0
num2=1
count = 2
l=[0,1]
while count<10:
    next_num = num1+num2
    l.append(next_num)
    num1=num2
    num2=next_num
    count+=1
print(l)

#Q2 - Need to remove every # and char just before that
'''
s = "ab##cd#hg"
present = True
while present:
    if '#'in s:
        index_ = s.index('#')
        #sub_str = s[index_-1:index_+1]
        #s = s.replace(sub_str,"")
        s = s[:index_-1] + s[index_+1:]
    else:
        present = False
print(s)
'''
#Q3
'''
l=[0,0,2,5,4,0,3]
#outpur = [2,5,4,3,0,0,0] without using any other list
for i in l:
    if i==0:
        l.remove(i)
        l.append(i)
print(l)
'''
#Q4: list comprehensan
#Q5: mutable/immutable
#Q6: Decorator
#Q7: Generator
#Q8: Variable types
