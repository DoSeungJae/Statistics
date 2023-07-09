import numpy as np
import pandas as pd

mean=0
std=1
max_=100000
size=(max_,100) #( 0: number of SAMPLE,  1: SIZE of sample)
samples=np.random.normal(mean,std,size)

AS=[]#Average of Samples
S=[] #State
for i in range(size[0]):
    AS.append(sum(samples[i])/size[1])

cnt=0
std=0.1
for i in range(size[0]):
    if AS[i]-(1.96*std) <= mean <= AS[i]+(1.96*std):
        S.append('Included')
        cnt+=1
    else:
        S.append('Excluded')



raw_data={'Sample Number':[i+1 for i in range(size[0])],'Sample Mean':[AS[i] for i in range(size[0])],\
           'Lowest':[AS[i]-(1.96*std) for i in range(size[0])] ,\
           'Highest':[AS[i]+(1.96*std) for i in range(size[0])],'State of P Mean':[S[i] for i in range(size[0])] }
df=pd.DataFrame(raw_data,columns=['Sample Number','Sample Mean','Lowest','Highest','State of P Mean'])


print(df)
p=cnt/size[0]
print()

print('%d Samples include the population mean in Range'%cnt)
print('Probability :',p)




