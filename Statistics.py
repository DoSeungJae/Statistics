import math
import sys
input=sys.stdin.readline

data=[41,32,30,23,24,32,11,39,24,46,60,40,41,14,33,50,38,25,\
      32,16,43,19,35,22,46,43,10,22,40,47,66,48,25,43,28,31,12,25,12,48]

#도수, 상대도수, 누적도수, 누적상대도수
#계급수, 계급 범위(간격), 계급값

f=[] #Frequency
rf=[] #Relative Frequency
cn=0 #ClassNumber
cr=[] #ClassRange
cv=[] #ClassValue
cvm=[]

mini=min(data)

def ClassNumber(): #List,f
    leng=len(data)
    if leng<200:
        return int(math.sqrt(leng))
    else:
        return int(1+3.3*math.log10(leng))


def ClassRange(): #List,cn
    return math.ceil((max(data)-min(data))/cn)

def ClassValue():  #cv,cr
    lowest=mini-0.5
    cv=[[lowest,lowest+cr]]
    
    for i in range(cn-1):
        cv.append([cv[-1][1], cv[-1][1]+cr])
    return cv



def Frequency():  #List,f,cv,cn
    for i in range(cn):
        f.append(0)
    for i in range(len(cv)): 
        for j in range(len(data)):
            if cv[i][0] <data[j] < cv[i][1]:
                f[i]+=1
                

    return f

            
def RelativeFrequency():
    leng=len(data)
    for i in range(cn):
        rf.append(0)

    for i in range(cn):
        rf[i]+=f[i]/leng

    return rf

def ClassValueMiddle():
    for i in range(cn):
        cvm.append(0)

    for i in range(cn):
        cvm[i]=(cv[i][0]+cv[i][1])/2

    return cvm




def fh(): #FrequencyHistogram
    
    print(' '*2,end='')
    for i in range(cn):
        print(f[i],end=' '*4)
    print()
    
        
    for i in range(max(f)+1):
        
        if i==max(f):
            print(*cvm)
        else:
            print(' '*2,end='')

            for j in range(cn):
                
                if f[j]!=max(f):
                    print(' ',end='')
                    f[j]+=1

                    print(' '*4, end='')
                elif f[j]==max(f):
                    print('*', end='')
                    print(' '*4, end='')
            print()

    print()
    print()



def fdt(): #FrequnecyDistributionTable
    cf=0
    crf=0
    print("| 계 급 |  계급간격 |도수| 상대도수 | 누적도수 | 누적상대도수 | 계급값 |")
    for i in range(len(f)):
        start=cv[i][0]
        end=cv[i][1]
        f_=f[i]
        cf+=f[i]

        
        print(f"|제{i+1}계급|{start:>4} ~ {end:>4}| {f_:>2} |  {f_/len(data):.3f}   |    {cf:>2}    |     {cf/len(data):.3f}    |  {(start+end)/2:>4}  |")

    print(f"| 합 계 |           | {len(data):>2} |   1.00   |          |              |        |")

    print()
    print()
    


cn=ClassNumber() #data,f
cr=ClassRange() #data,cn
cv=ClassValue() #cv,cr
f=Frequency() #data,f,cv,cn
rf=RelativeFrequency() #rf,f,data
cvm=ClassValueMiddle()
f_tuple=tuple(f)

while 1:
    print('input menu')
    print('1: Frequency Distribution Table')
    print('2: Frequency Histogram')
    print('0: quit')

    menu=int(input())
    if menu==0:
        break
    elif menu==1:
        fdt()

    elif menu==2:
        fh()
        f=list(f_tuple)
    else:
        print('wrong input')
        
        
    

