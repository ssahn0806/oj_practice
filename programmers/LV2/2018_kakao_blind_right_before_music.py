def parse(melody):
    n = len(melody)
    melody_dict = {'C':'1','C#':'2','D':'3','D#':'4','E':'5','E#':'13','F':'6','F#':'7','G':'8','G#':'9','A':'10','A#':'11','B':'12'}
    
    result = []
    
    idx = 0
    
    while idx<n:
        if idx+1 == n or melody[idx+1] !='#':
            result.append(melody_dict[melody[idx]])
            idx+=1
        else :
            result.append(melody_dict[melody[idx:idx+2]])
            idx+=2
    return result

def get_minite(t1,t2):
    
    result = 0
    h1,m1 = map(int,t1.split(':'))
    h2,m2 = map(int,t2.split(':'))
    
        
    if h1==h2:
        result = (m2-m1)
    else :
        result = (60-m1)
        for i in range(h1+1,h2):
            result += 60
        result += m2
    return result

def solution(m, musicinfos):
    answer = []
    
    parsed_m = ''.join(parse(m))
    
    full_musics = []
    
    for idx,musicinfo in enumerate(musicinfos):
        music = musicinfo.split(',')
        
        play_length = get_minite(music[0],music[1])
        
        temp_melody = parse(music[3])
        
        play_melody = [temp_melody[i%len(temp_melody)] for i in range(play_length)]
        
        if parsed_m in ''.join(play_melody):
            answer.append((music[2],play_length,idx))
            
    if not answer:
        return "(None)"
    
    answer.sort(key=lambda x : (-x[1],x[2]))
    return answer[0][0]