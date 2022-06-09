def solution(clothes):
    parse_dict = {}
    
    for name,section in clothes:
        if section in parse_dict.keys():
            parse_dict[section].append(name)
        else :
            parse_dict[section] = [name]

    total = 1
    for section,names in parse_dict.items():
        total *= (len(names)+1)
        
    return total-1