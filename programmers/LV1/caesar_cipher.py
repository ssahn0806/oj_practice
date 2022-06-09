# 각 알파벳을 일정한 거리만큼 shift 

# 알파벳 소문자, 대문자, 공백으로만 구성
# 공백은 아무리 밀어도 공백
# n는 1이상 25이하 자연수

# 대문자 -> 대문자 유지, 소문자 -> 소문자 유지
# a,b,c,d,e,f,g / h,i,j,k,l,m,n / o,p,q,r,s,t,u / v,w,x,y,z : 26개
# A,B,C,D,E,F,G / H,I,J,K,L,M,N / O,P,Q,R,S,T,U / V,W,X,Y,Z : 26개

def solution(s,n):
    result = ''
    
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch)+n-ord('A'))%26 + ord('A'))
            else:
                result += chr((ord(ch)+n-ord('a'))%26 + ord('a'))
            
        else :
            result += ch    
    
    return result