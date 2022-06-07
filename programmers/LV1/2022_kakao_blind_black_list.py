def solution(id_list,report,k):
    
    # 전체 사용자 수
    n = len(id_list)
    
    # 각 사용자가 신고한 유저의 목록
    report_lst = {} 
    
    for id in id_list:
        report_lst[id] = []
        
    # 각 사용자가 신고당한 횟수
    reported_cnt_lst = {}
    # reported_list = {x : 0 for x in id_list}
    
    for id in id_list:
        reported_cnt_lst[id] = 0
        
    # 중복 신고 제거
    cut_duplicate_report = list(set(report))
    
    # 각 신고에 대해 신고자와 피신고자를 구분하여 목록과 횟수 반영
    for report in cut_duplicate_report:
        rep,des = report.split()
        report_lst[rep].append(des)
        reported_cnt_lst[des]+=1
    
    # 정지 대상자 목록 추출
    ban_lst = [id for id,cnt in reported_cnt_lst.items() if cnt>=k]
    
    # 결과 통보 횟수 기록 
    result = []
    
    # 각 사용자 신고 유저가 정지 대상자인 경우 카운팅
    for rep,des in report_lst.items():
        cnt = 0
        for ban_candidate in des:
            if ban_candidate in ban_lst:
                cnt+=1
        result.append(cnt)
    
    return result