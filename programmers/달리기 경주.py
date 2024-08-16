# 달리기 경주
# 추월에 성공한 선수 이름을 기록
# player에 현재 등수가 기록되어 있음.
# 추월에 설공한 문자열 배열 callings가 주어질 때 경기가 끝난 시점의 등수를 담아 리턴 
# callings는 최대 100만으로 O(N^2)이하로 해결해야 함.
# players는 최대 5만으로 여러번 탐색해도 괜찮을 듯.

# 접근 방법
# players를 바꿔가며 사용.
# callings에 등장하면 players에서 찾은 뒤 오른쪽 요소와 자리를 바꿈.
# list.index()의 시간 복잡도는 N. 최대 M * N이 될 수 있음.
# 100만 * 5만은 5억으로 해결하지 못함.
# map에 플레이어별 현재 순서를 담고 위치를 갱신해 O(1)을 통해 현재 위치를 찾을 수 있도록 함

def solution(players, callings):
    # 선수 이름을 키로 하고, 위치를 값으로 하는 딕셔너리 생성
    position = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        # 추월한 선수의 현재 위치
        cur_position = position[call]
        
        # 추월할 선수를 찾기 (현재 위치에서 왼쪽에 있는 선수)
        prev_player = players[cur_position - 1]
        
        # 리스트에서 두 선수의 위치를 교환
        players[cur_position - 1], players[cur_position] = players[cur_position], players[cur_position - 1]
        
        # 딕셔너리에서도 위치를 업데이트
        position[call] -= 1
        position[prev_player] += 1
        
    return players