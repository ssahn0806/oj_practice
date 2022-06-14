def solution(n):
    bin_n = bin(n)[2:]
    nth_count = bin_n.count('1')
    for i in range(n+1,1000001):
        bin_i = bin(i)[2:]
        ith_count = bin_i.count('1')
        if ith_count == nth_count:
            return int(bin(i),2)