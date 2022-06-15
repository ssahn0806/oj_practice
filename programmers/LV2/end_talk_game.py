def solution(n, words):
    
    word_dict = {}
    for idx,word in enumerate(words):
        # 첫번째 사람은 탈락할 수 없음. 사전에 추가
        if idx==0:
            word_dict[word] = 1
        else :
            # 이전에 말한 사람의 마지막 문자와 현재 말한 사람의 단어의 첫문자가 같아야 계속 진행이 가능함
            if word[0] == words[idx-1][-1]:
                if word not in word_dict:
                    word_dict[word] = 1
                else :
                    # 이미 말했던 단어라면 현재 사람이 탈락자가 된다.
                    return [(idx)%n+1,((idx)//n)+1]
            # 규칙을 지키지 않았으므로 현재 사람이 탈락자가 된다.
            else :
                return [(idx)%n+1,((idx)//n)+1]
    # 모두 통과했으므로 게임이 현재 끝나지 않은 상태
    return [0,0]