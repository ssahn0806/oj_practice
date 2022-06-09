# 사용자 이름, 닉네임, 상태 저장 객체
class User:
    def __init__(self,id,nick,state):
        self.id = id
        self.nick = nick
        self.state = "들어왔습니다" if state == 0 else "나갔습니다"
    
    def change_nick(self,new_name):
        self.nick = new_name
        
    def get_id(self):
        return self.id
    
    def get_nick(self):
        return self.nick

    def result(self):
        return f'{self.nick}님이 {self.state}.'
        
    
def solution(record):
    # Enter uid1234 Muzi
    # Leave uid1234
    # Change uid1234 Ryan
    
    # uid -> 닉네임 최신 정보 
    id_nick_dict = dict()
    
    # 임시 결과
    temp_lst = []
    
    # 최종 결과
    result = []
     
    # 모든 기록에 대하여 탐색 
    for state in record:
        
        # 공백을 기준으로 구분
        state_lst = state.split()
        
        # Leave
        if len(state_lst) == 2:
            uid = state_lst[1]
            temp_lst.append(User(uid,nick,1))
            
        else : # Enter / Change
            cmd,uid,nick = state_lst

            # 닉네임 최신화
            id_nick_dict[uid] = nick
            if cmd == 'Enter':
                temp_lst.append(User(uid,nick,0))
    # 모든 기록에 대하여, 닉네임을 최신화하여 변경
    for i in temp_lst:
        if id_nick_dict[i.get_id()] != i.get_nick():
            i.change_nick(id_nick_dict[i.get_id()])
        result.append(i.result())
            
    return result