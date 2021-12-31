list='The quick Brow Fox'
i=0
capital=("A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z")
small=("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")
count1=0
count2=0
while i<len(list):
    if list[i] in capital:
        count1=count1+1
    elif list[i] in small:
        count2=count2+1
    else:
        pass
    i=i+1
print("lower case",count1)
print("upper case",count2)

