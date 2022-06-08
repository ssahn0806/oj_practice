def solution(numbers,hand):
    # 1,4,7,* : 왼손
    # 3,6,9,# : 오른손
    # 2,5,8,0 : 양손 중 가까운 손으로 누름
    '''
    1 2 3 - (0,0) (0,1) (0,2)
    4 5 6 - (1,0) (1,1) (1,2)
    7 8 9 - (2,0) (2,1) (2,2)
    * 0 # - (3,0) (3,1) (3,2)
    '''
    # 맨헤튼 거리로 계산 가능함 |x1-x2| + |y1-y2|
    
    # 초기 양손의 위치
    cur_left_pose = (3,0)
    cur_right_pose = (3,2)
    
    # 결과
    result = ''
    
    # 누를 숫자를 순서대로 탐색
    for num in numbers:
        
        # 왼손으로 누르는 번호
        if num in [1,4,7]:
            result+='L'
            cur_left_pose = (num//3,0)
            
        # 오른손으로 누르는 번호
        elif num in [3,6,9]:
            result+='R'
            cur_right_pose = (num//3-1,2)
        
        # 왼손 또는 오른손으로 누르는 번호
        else :
            
            # 0 예외처리
            if num == 0:
                num_pose = (3,1)
            else :
                num_pose = (num//3 + num%3 -2,1)
            
            # 양손으로부터 거리 계산
            left_dist = abs(cur_left_pose[0] - num_pose[0]) + abs(cur_left_pose[1] - num_pose[1])
            right_dist = abs(cur_right_pose[0] - num_pose[0]) + abs(cur_right_pose[1] - num_pose[1])
            
            # 거리 및 왼/오른손잡이에 따라 적용
            if left_dist < right_dist:
                result += 'L'
                cur_left_pose = num_pose
                
            elif left_dist > right_dist:
                result += 'R'
                cur_right_pose = num_pose
                
            else :
                if hand == 'left':
                    result += 'L'
                    cur_left_pose = num_pose
                    
                else :
                    result += 'R'
                    cur_right_pose = num_pose    
                
    return result