dimension a(5,5), deta(5,5,5,5)
open(1,file = detin.txt)
open(2,file = detot.txt)
read(1,*)nncall read(a,nn)
call dt(nn,a,1,1,nn,nn,deta)
write(2,*)deta(1,1,nn,nn)
end
SUBROUTINE READ(A,NN)
dimension a(nn,nn)
do 10 i = 1,nn
10 read(1,*)(a(i,j),j = 1,nn)
end
RECURSIVE SUBROUTINE
DT(NN,A,M,N,P,Q,DETA)
integer p,q,p1,q1
dimension
a(nn,nn),deta(nn,nn,nn,nn)
20 format(<nn>f5.0)
if(p-m.eq.1)then
deta(m,n,p,q) = a(m,n)*a(p,q)-
a(p,n)*a(m,q)
end if
if(p-m.eq.0)then
deta(m,n,p,q) = a(m,n)
goto 100
end if
if(p-m.gt.1)then
p1 = p-1
q1 = q-1
m1=m+1
n1=n+1
call dt(nn,a,m,n,p1,q1,deta)
call dt(nn,a,m1,n1,p,q,deta)
call dt(nn,a,m,n1,p1,q,deta)
call dt(nn,a,m1,n,p,q1,deta)
call dt(nn,a,m1,n1,p1,q1,deta)
deta(m,n,p,q)=(deta(m,n,p1,q1)*deta(m1, n1,p,q)-
deta(m,n1,p1,q)*deta(m1,n,p,q1))
/deta(m1,n1,p1,q1)
end if
100 write(2,*)deta(m,n,p,q)
endO. 
