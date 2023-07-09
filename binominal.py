import sys

input=sys.stdin.readline
import matplotlib.pyplot as plt


def Combination(n,k):
    def Factorial(n):
        f=[1,1,2,6]
            

        if n<=3:
            return f[n]
        else:
            for i in range(4,n+1):
                f.append(int(i*f[i-1]))

            return f[n]

    nCk=int(Factorial(n)/(Factorial(k)*Factorial(n-k)))

    return nCk


def BDG(n_list,p): #Binominal Distribution Graph
    for i in range(len(n_list)):
        x_list=[j for j in range(1,n_list[i]+1)] #
        y_list=[Combination(n_list[i],x)*(p**x)*((1-p)**(n_list[i]-x)) for x in range(1,n_list[i]+1)] #n_list[i]+1
        plt.plot(x_list,y_list)
    plt.show()

n_list=[20,30,40,50]
p=1/6
BDG(n_list,p)


p=2/6
BDG(n_list,p)

p=3/6
BDG(n_list,p)


