def solution(str1, str2):
    n, m = len(str1),len(str2)
    multiset_A = {}
    multiset_B = {}
    
    for i in range(n-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            if str1[i:i+2].lower() in multiset_A:
                multiset_A[str1[i:i+2].lower()]+=1
            else :
                multiset_A[str1[i:i+2].lower()]=1
    for i in range(m-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            if str2[i:i+2].lower() in multiset_B:
                    multiset_B[str2[i:i+2].lower()]+=1
            else :
                multiset_B[str2[i:i+2].lower()]=1
    
    
    if not multiset_A and not multiset_B:
        answer = 1
    else :
        intersection_set = {key : min(multiset_A[key],multiset_B[key]) for key in multiset_A if key in multiset_B}
        '''
        union_set = {key : max(multiset_A[key],multiset_B[key]) for key in intersection_set}
        for key in multiset_A:
            if key not in multiset_B:
                union_set[key] = multiset_A[key]
                
        for key in multiset_B:
            if key not in multiset_A:
                union_set[key] = multiset_B[key]
        '''
        union_set = {key : multiset_A[key] for key in multiset_A}
        for key in multiset_B:
            if key in union_set:
                union_set[key] = max(union_set[key],multiset_B[key])             
            else :
                union_set[key] = multiset_B[key]
                
        answer = sum(intersection_set.values())/sum(union_set.values())
    
    return int(answer*65536)