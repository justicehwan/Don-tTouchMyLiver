import random
import time

# 3x3 맵을 리스트로 표현 (0부터 8까지의 인덱스)
def print_board(player_pos, chaser_pos, game_over=False):
    # 9개의 칸을 미리 정의하여 이모티콘 위치만 갱신
    board = ['   ( 0 )  ', '   ( 1 )  ', '   ( 2 )  ', 
             '   ( 3 )  ', '   ( 4 )  ', '   ( 5 )  ', 
             '   ( 6 )  ', '   ( 7 )  ', '   ( 8 )  ']
    
    if game_over:
        board[player_pos] = f'   (💀)   '  # 술래에게 잡혔을 때 거북이 대신 다른 이모티콘
        board[chaser_pos] = f'   (💀)   '
    else:
        board[player_pos] = f'   (🐇)   '  # 플레이어 위치
        board[chaser_pos] = f'   (🐢)   '  # 술래 위치

    # 더 큰 크기의 그래프 출력, 가운데 칸 번호 추가
    print("-- (번호)는 각 칸을 의미하는 번호입니다) --")
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(" - - - - - + - - - - - - + - - - - - ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(" - - - - - + - - - - - - + - - - - - ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def valid_moves(pos):
    """주어진 위치에서 이동할 수 있는 인접한 칸 반환 (대각선도 포함)"""
    moves = {
        0: [1, 3, 4], 1: [0, 2, 3, 4, 5], 2: [1, 4, 5],
        3: [0, 1, 4, 6, 7], 4: [0, 1, 2, 3, 5, 6, 7, 8], 
        5: [1, 2, 4, 7, 8], 6: [3, 4, 7], 7: [3, 4, 5, 6, 8],
        8: [4, 5, 7]
    }
    return moves[pos]

def game():
    while True:  # 게임 반복
        # 초기 설정
        player_pos = random.randint(0, 8)  # 플레이어 초기 위치
        chaser_pos = 4  # 술래는 항상 가운데(4번 칸)에서 시작
        turns = 10  # 10턴 제한
        
        # 플레이어와 술래가 같은 칸에 있을 수 없으므로 다시 배치
        while player_pos == chaser_pos:
            player_pos = random.randint(0, 8)
        
        print("## 게임 시작! 3x3 맵에서 자라를 피해 도망치세요! ##")
        print()
        print("-- 토끼의 위치는 '(🐇)', 자라의 위치는 '(🐢)'로 표시됩니다. --")
        print()
        print_board(player_pos, chaser_pos)
        
        # 게임 시작
        while turns > 0:
            print()
            print(f"남은 턴: {turns}턴 생존 시 승리!")
            print()
            
            # 사용자 입력 받기
            try:
                move = int(input(">> 이동할 칸 번호를 입력하세요 (0-8), 이동하지 않으려면 현재 위치를 입력하세요 << "))
                if move not in range(9):
                    print("잘못된 입력입니다. 0부터 8까지의 숫자를 입력해주세요.")
                    continue
            except ValueError:
                print("숫자를 입력하세요.")
                continue
            
            # 이동하지 않으려면 그대로 두기
            if move == player_pos:
                print(f"이동하지 않고 현재 위치를 유지합니다.")
            # 플레이어가 이동할 수 있는 위치인지 체크
            elif move in valid_moves(player_pos):
                player_pos = move
            else:
                print(f"그 칸으로는 이동할 수 없습니다. 현재 위치는 그대로 유지됩니다.")
                continue
            
            # 술래가 랜덤으로 인접한 칸으로 이동
            chaser_pos = random.choice(valid_moves(chaser_pos))
            
            # 맵 출력
            print_board(player_pos, chaser_pos)
            
            # 게임 종료 체크 (플레이어와 술래가 같은 칸에 있을 때)
            if player_pos == chaser_pos:
                print()
                print("☠️자라에게 잡혀 간을 뺐겼습니다!☠️")
                print_board(player_pos, chaser_pos, game_over=True)
                break
            
            # 턴 감소
            turns -= 1
            
            # 10턴 내에 술래가 잡지 못하면 토끼 승리
            if turns == 0:
                print()
                print("🎉10 턴이 끝났습니다! 토끼가 승리합니다!🎉")
                break
            
            # 잠시 대기 (게임 진행이 너무 빨리 끝나지 않도록)
            time.sleep(1)
        
        # 게임 재시작 여부 확인
        replay = input("게임을 다시 시작하려면 'r'을 입력하세요, 종료하려면 아무 키나 누르세요: ")
        if replay.lower() != 'r':
            break

# 게임 실행
game()
