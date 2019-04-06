import cmath
import numpy as np
index1=['A','B','A','B','A','B','A','B']
index2=['A','A','B','B','A','A','B','B']
index3=['A','A','A','A','B','B','B','B']
re = 0.707
img = 0.707
z = complex(re,img); 
c0 = 1
j = cmath.sqrt(-1)
c1 = 0.707- 0.707j
c2 = -j
c3 = -0.707- 0.707j
C1=[c0,c0,c0,c0]
C2=[c0,c2,c0,c2]
C3=[c0,c1,c2,c3]

def AplusBC(a,b,c):
    return  a+b*c
def AminusBC(a,b,c):
    return a-b*c
def comp(tup,c):
    A,B=[],[]
    for t in tup:
        if t[0]=='A':
            A.append(t[1])
        else :
            B.append(t[1])

    ansA,ansB=[],[]
    for i,c_ in enumerate(c):
        ans1=AplusBC(A[i],B[i],c_)
        ans2=AminusBC(A[i],B[i],c_)
# =============================================================================
#         print("{}+{}*{}={}".format(A[i],B[i],c_,ans1))
#         print("======================================")
#         print("{}-{}*{}={}".format(A[i],B[i],c_,ans2))
# =============================================================================
        ansA.append(ans1)
        ansB.append(ans2)
    return ansA,ansB

def result_arr(index,A,B):
    
    res=[]
    a,b=0,0
    for v in index:
        
        if v=='A':
            res.append(A[a])
            a+=1
        else :
            res.append(B[b])
            b+=1
        
    return res


def main_res(index,c,arr): 
    
    tup=list(zip(index,arr))
    s1,s2=comp(tup,c)
    arr=result_arr(index,s1,s2)
    return arr       


if __name__=='__main__':
    x = list(map(int, input("Enter 8 values: ").split()))
    arr =np.array([x[0],x[4],x[2],x[6],x[1],x[5],x[3],x[7]]) 
    print(arr)
    arr = main_res(index1,C1,arr)
    print("step1=",arr)
    arr = main_res(index2,C2,arr)
    print("step2=",arr)
    arr = main_res(index3,C3,arr)
    print("step3=",arr)



