# def solution(book_time):
#     book_time = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:]) + 10) for s, e in book_time]
#     book_time.sort(key=lambda x:(x[0], x[1]))
#     rooms = []
#     answer = 0
#     for start, end in book_time:
#         print(start, end)
#         if not rooms or start < min(rooms):
#             rooms.append(end)
#         else:
#             for i in range(len(rooms)):
#                 if rooms[i] <= start:
#                     del rooms[i]
#                     break
#         print(rooms)
#         answer = max(answer, len(rooms))
#     return answer

def solution(book_time):
    book_time = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:]) + 10) for s, e in book_time]
    events = []
    for start, end in book_time:
        events.append((start, 1))  # 시작 이벤트를 1로 표시
        events.append((end, -1))   # 종료 이벤트를 -1로 표시
    
    events.sort(key = lambda x:(x[0], x[1]))
    
    print(events)
    
    count = 0  # 현재 사용 중인 방의 개수를 나타내는 변수
    max_rooms = 0  # 최대로 필요한 방의 개수를 나타내는 변수

    for event in events:
        n, m = event  # 이벤트의 시각과 타입을 가져옵니다.
        count += m  # 이벤트 타입에 따라 방의 개수를 업데이트합니다.
        max_rooms = max(max_rooms, count)  # 최대 방 개수 업데이트
        
    return max_rooms

# def solution(book_time):
#     book_time = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:]) + 10) for s, e in book_time]
#     print(book_time)
#     book_time.sort(key=lambda x: x[1])  # 종료 시각을 기준으로 정렬합니다.
    
#     rooms = []  # 각 방의 마지막 퇴실 시각을 저장하는 리스트
#     for start, end in book_time:
#         # 현재 예약의 시작 시각과 이전 방 중 가장 빨리 떠난 시각을 비교합니다.
#         # 만약 현재 예약의 시작 시각이 이전 방보다 빠르다면 새로운 방이 필요합니다.
#         if not rooms or start < min(rooms):
#             rooms.append(end)  # 새로운 방을 추가합니다.
#         else:
#             # 이미 사용 중인 방 중 가장 빨리 떠날 수 있는 방을 찾아 업데이트합니다.
#             for i in range(len(rooms)):
#                 if rooms[i] <= start:
#                     rooms[i] = end
#                     break
#     return len(rooms)


book_time = [["00:10", "00:20"], ["00:30", "00:40"]]	
print(solution(book_time))