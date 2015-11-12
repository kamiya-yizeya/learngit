def best(tr,a,b):          
    i = a
    y1 = []
    y2 = []
    y0 = []
    z = []
    fin = []
    while i > a - 1 and i < b:
        x = f.readline().split()
        y0.append(x[0])
        y1.append(x[2])
        y2.append(x[4])
        i = i + 1
    while i < b:
        if y1[i] == tr:
            z.append(y2[i])
            i = i + 1
    leastmoney = min(z)
    while i < b:
        if least != y2[i]:
            i = i + 1
        elif leastmoney == y2[i]:
            fin.extend([y0[i],y1[i],y2[i]])    
    return fin[0:3]

def twice(x):                        
    i = 0
    a = 500*x - 500
    b = 500*x
    q0 = best(0.9,a,b)
    q1 = best(0.91,a,b)
    q2 = best(0.92,a,b)
    q3 = best(0.93,a,b)
    q4 = best(0.94,a,b)
    q5 = best(0.95,a,b)
    q6 = best(0.96,a,b)
    q7 = best(0.97,a,b)
    q8 = best(0.98,a,b)
    q9 = best(0.99,a,b)
    q10 = best(1,a,b)
    q = q0+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10
    Q = q0[2]+q1[2]+q2[2]+q3[2]+q4[2]+q5[2]+q6[2]+q7[2]+q8[2]+q9[2]+q10[2]
    temp = []
    while i < 11:
        if Q[i] != min(Q):
            del Q[i]
        else:
            temp.append(Q[i])
            del Q[i]
        i = i + 1
    while i < 11:
        if q[i][2] not in temp:
            del q[i]
    return q
     
def third(A,x,y):
    i=0
    while i < len(A):
        if A[i][2] > y:
            del A[i]
        elif A[i][1] < x:
            del A[i]
    return A
            
def one(A,B,C,D,G):
    A1 = third(A,0.92,10)
    B1 = third(B,0.92,10)
    C1 = third(C,0.92,10)
    D1 = third(D,0.92,10)
    G1 = third(G,0.92,10)
    i = 0
    x = []
    y = []
    z = []
    p = []
    q = []
    while i < len(A1):
        z.append(A1[i][0])
        while i < len(B1):
            z.append(B1[i][0])
            while i < len(C1):
                z.append(C1[i][0])
                while i < len(D1):
                    z.append(D[i][0])
                    while i < len(G1):
                        z.append(G1[i][0])
                        x.append(A1[i][1]*B1[i][1]*C1[i][1]*D1[i][1]*G1[i][1])
                        y.append(A1[i][2]+B1[i][2]+C1[i][2]+D1[i][2]+G1[i][2])
                        p.append(z)
                        q.append(x[i]-y[i]/100)
    a = min(q)
    while i < len(q):
        if a != q[i]:
            i = i + 1
        elif a == q[i]:
            b = j
    print(p[b])
    print(",Reliability=")
    print(x[b])
    print(",Cost=")
    print(y[b])
    print(",Q=")
    print(a)

def two(A,B,C,D,E,G,H,K):
    A1 = third(A,0.90,15)
    B1 = third(B,0.90,15)
    C1 = third(C,0.90,15)
    D1 = third(D,0.90,15)
    E1 = third(E,0.90,15)
    G1 = third(G,0.90,15)
    H1 = third(H,0.90,15)
    K1 = third(K,0.90,15)
    i = 0
    x = []
    y = []
    z = []
    p = []
    q = []
    while i < len(A1):
        z.append(A1[i][0])
        while i < len(B1):
            z.append(B1[i][0])
            while i < len(C1):
                z.append(C1[i][0])
                while i < len(D1):
                    z.append(D[i][0])
                    while i < len(E1):
                        z.append(E1[i][0])
                        while i < len(G1):
                            z.append(G1[i][0])
                            while i < len(H1):
                                z.append(H1[i][0])
                                while i < len(K1):
                                    z.append(K1[i][0])
                                    x.append(A1[i][1]*B1[i][1]*C1[i][1]*D1[i][1]*E1[i][1]*G1[i][1]*H1[i][1]*K1[i][1])
                                    y.append(A1[i][2]+B1[i][2]+C1[i][2]+D1[i][2]+E1[i][2]+G1[i][2]+H1[i][2]+K1[i][2])
                                    p.append(z)
                                    q.append(x[i]-y[i]/100)
    a = min(q)
    while i < len(q):
        if a != q[i]:
            i = i + 1
        elif a == q[i]:
            b = i
    print(p[b])
    print(",Reliability=")
    print(x[b])
    print(",Cost=")
    print(y[b])
    print(",Q=")
    print(a)
    
def three(A,B,C,D,E,F,G,H,I,J,K,L):
    A1 = third(A,0.85,25)
    B1 = third(B,0.85,25)
    C1 = third(C,0.85,25)
    D1 = third(D,0.85,25)
    E1 = third(E,0.85,25)
    F1 = third(F,0.85,25)
    G1 = third(G,0.85,25)
    H1 = third(H,0.85,25)
    I1 = third(I,0.85,25)
    J1 = third(J,0.85,25)
    K1 = third(K,0.85,25)
    L1 = third(L,0.85,25)
    i = 0
    x = []
    y = []
    z = []
    p = []
    q = []
    while i < len(A1):
        z.append(A1[i][0])
        while i < len(B1):
            z.append(B1[i][0])
            while i < len(C1):
                z.append(C1[i][0])
                while i < len(D1):
                    z.append(D[i][0])
                    while i < len(E1):
                        z.append(E1[i][0])
                        while i < len(F1):
                            z.append(F1[i][0])
                            while i < len(G1):
                                z.append(G1[i][0])
                                while i < len(H1):
                                    z.append(H1[i][0])
                                    while i < len(I1):
                                        z.append(I1[i][0])
                                        while i < len(J1):
                                            z.append(J1[i][0])
                                            while i < len(K1):
                                                z.append(K1[i][0])
                                                while i < len(L1):
                                                    z.append(L1[i][0])
                                                    x.append(A1[i][1]*B1[i][1]*C1[i][1]*D1[i][1]*E1[i][1]*F1[i][1]*G1[i][1]*H1[i][1]*I1[i][1]*J1[i][1]*K1[i][1]*L1[i][1])
                                                    y.append(A1[i][2]+B1[i][2]+C1[i][2]+D1[i][2]+E1[i][2]+F1[i][2]+G1[i][2]+H1[i][2]+I1[i][2]+J1[i][2]+K1[i][2]+L1[i][2])
                                                    p.append(z)
                                                    q.append(x[i]-y[i]/100)
    a = min(q)
    while i < len(q):
        if a != q[i]:
            i = i + 1
        elif a == q[i]:
            b = i
    print(p[b])
    print(",Reliability=")
    print(x[b])
    print(",Cost=")
    print(y[b])
    print(",Q=")
    print(a)

def four(A,B,C,D,E,F,G,H,I,J,K,L,M,N):
    A1 = third(A,0.80,30)
    B1 = third(B,0.80,30)
    C1 = third(C,0.80,30)
    D1 = third(D,0.80,30)
    E1 = third(E,0.80,30)
    F1 = third(F,0.80,30)
    G1 = third(G,0.80,30)
    H1 = third(H,0.80,30)
    I1 = third(I,0.80,30)
    J1 = third(J,0.80,30)
    K1 = third(H,0.80,30)
    L1 = third(L,0.80,30)
    M1 = third(M,0.80,30)
    N1 = third(N,0.80,30)
    i = 0
    x = []
    y = []
    z = []
    p = []
    q = []
    while i < len(A1):
        z.append(A1[i][0])
        while i < len(B1):
            z.append(B1[i][0])
            while i < len(C1):
                z.append(C1[i][0])
                while i < len(D1):
                    z.append(D[i][0])
                    while i < len(E1):
                        z.append(E1[i][0])
                        while i < len(F1):
                            z.append(F1[i][0])
                            while i < len(G1):
                                z.append(G1[i][0])
                                while i < len(H1):
                                    z.append(H1[i][0])
                                    while i < len(I1):
                                        z.append(I1[i][0])
                                        while i < len(J1):
                                            z.append(J1[i][0])
                                            while i < len(K1):
                                                z.append(K1[i][0])
                                                while i < len(L1):
                                                    z.append(L1[i][0])
                                                    while i < len(M1):
                                                        z.append(M1[I][0])
                                                        while i < len(N1):
                                                            z.append(N1[i][0])
                                                            x.append(A1[i][1]*B1[i][1]*C1[i][1]*D1[i][1]*E1[i][1]*F1[i][1]*G1[i][1]*H1[i][1]*I1[i][1]*J1[i][1]*K1[i][1]*L1[i][1]*M1[i][1]*N1[i][1])
                                                            y.append(A1[i][2]+B1[i][2]+C1[i][2]+D1[i][2]+E1[i][2]+F1[i][2]+G1[i][2]+H1[i][2]+I1[i][2]+J1[i][2]+K1[i][2]+L1[i][2]+M1[i][2]+N1[i][2])
                                                            p.append(z)
                                                            q.append(x[i]-y[i]/100)
    a = min(q)
    while i < len(q):
        if a != q[i]:
            i = i + 1
        elif a == q[i]:
            b = i
    print(p[b])
    print(",Reliability=")
    print(x[b])
    print(",Cost=")
    print(y[b])
    print(",Q=")
    print(a)
    
f = open('C:/SERVICE.txt','r')
A = twice(1)
B = twice(2)
C = twice(3)
D = twice(4)
E = twice(5)
F = twice(6)
G = twice(7)
H = twice(8)
I = twice(9)
J = twice(10)
K = twice(11)
L = twice(12)
M = twice(13)
N = twice(14)
one(A,B,C,D,G)
two(A,B,C,D,E,G,H,K)
three(A,B,C,D,E,F,G,H,I,J,K,L)
four(A,B,C,D,E,F,G,H,I,J,K,L,M,N)
f.close()