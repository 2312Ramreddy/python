def one():
    str1=input("Enter the string:")
    list1=str1.split() #spilt the string and store into list as single element
    m=0
    word=0
    print(list1)
    for i in range(len(list1)):
        len(list1[i])
        if m<len(list1[i]):
            m=len(list1[i])
            word=i
    print("a) The word with longest length:",list1[word])
def two():
    str1=input("Enter the string:")
    char=input("Enter character")
    print(str1)
    counter=0
    for i in range(len(str1)):
        if char==str1[i]:
            counter+=1 #counter=counter+1

    print("Character %s is present %i times in string %s"% (char,counter,str1))

def three():
    str2 = input("Enter string")
    lenstr2=len(str2)
    j=lenstr2-1

    flag=0
    for i in range(int (lenstr2/2+1)):
        if(str2[i]==str2[j]):
            flag=1
        else:
            break
        j=-1

    if(flag==1):
        print("It is palindrome")
    else:
        print("it is not palindrome")

def four():
   str1 = input("Enter the string:") #i am ganesh 11
   sub1=input("Enter substring:") #ane
   sublen=len(sub1) //3
   index1=0
   j=0
   for i in range(len(str1)):
        if(sub1[j]==str1[i]):
            j=j+1
            if(j==sublen):
                index1=i-(sublen==1)
                break
            else:
                j=0
print("substring index :", index1)
def five():
    str1 = input("Enter input string:")
    list1= str1.split()
    list2=set(list1) #Delete duplicates \n", \
    list3=list(list2) #convert set again into List\n", \
    print(list1)
    print(list3)
    list4=[]
    list5=[]
    counter=0
    for i in range(len(list3)):
        counter=0
        for j in range(len(list1)):
            if(list3[i]==list1[j]):
                counter+=1
        list4=list3[i],counter
        list5.append(list4)

    print(list5)
while True:
    ch=int(input("Enter your choice:"))
    if(ch == 6 ):
        one()
    elif(ch==2):
        two()
    elif(ch==3):
        three()
    elif(ch==4):
        four()
    elif(ch==5):
        five()
    elif(ch==6):
        break
