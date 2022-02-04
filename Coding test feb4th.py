L =[23,1,0,-12,48, 15, 9, 20, -11, 42,7, -5, 13]

#Q2
product=1
for i in L:
    product=product*i
    #print(product)

#Q3
for i in range(0,10001,1):
    print(i)
  
#Q1
number=0
for i in L[1:len(L):2]:
    number=number+i
    print(number)

#Q4
string=str('Code Happy')
for i in string:
    print(i)


#Q5
num1=float(input('Enter the length of the rectangle:'))
num2=float(input('Enter the width of the rectangle:'))
area=num1*num2
print(area)

#Q6
character= True
while character:
    txt=input('Enter a character:')
    if txt=='Z' or txt=='z':
        character=False
    else:
        print('Enter another character:')

#Q7
file1=open('CS04022022.txt','w')
file1.write('Leunig - How to get there\n')
file1.write('\nGo to the end of the path until you get to the gate.')
file1.write('\nGo through the gate and head straight out towards the horizon')
file1.write('\nKeep going towards the horizon')
file1.write('\nSit down and have a rest every now and again,')
file1.write('\nBut keep on going, just keep on with it')
file1.write('\nKeep on going as far as you can.')
file1.write('\nThat is how you get there.')
file1.close()
