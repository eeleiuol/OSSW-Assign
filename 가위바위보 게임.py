import random

def play_game():
    choices = ["가위", "바위", "보"]
    print("가위, 바위, 보 중 하나를 선택하세요!")
    user_choice = input("당신의 선택: ")

    if user_choice not in choices:
        print("잘못된 입력입니다. 가위, 바위, 보 중 하나만 입력하세요.")
        return

    computer_choice = random.choice(choices)
    print(f"상대대의 선택: {computer_choice}")

    if user_choice == computer_choice:
        print("비겼습니다!")
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        print("당신이 이겼습니다!")
    else:
        print("상대가 이겼습니다!")

if __name__ == "__main__":
    play_game()