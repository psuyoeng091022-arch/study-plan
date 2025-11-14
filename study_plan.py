plans = [] # 모든 공부 계획 저장

def add_plan():
    subject = input("과목 이름: ")
    goal = input("오늘 목표: ")
    time = int(input("예상 공부 시간(분): "))
    plans.append({
        "subject": subject,
        "goal": goal,
        "time": time,
        "done": False 
    })
    print("저장 완료!\n")

def view_plans():
    if not plans:
        print("아직 저장된 계획이 없어요.\n")
        return
    
    print("\n 오늘의 공부 계획:")
    for i, p in enumerate(plans, 1):
        status = "완료" if p["done"] else "미완료"
        print(f"{i}. [{p['subject']}] {p['goal']} / {p['time']}분 / 상태: {status}")
    print()

def mark_done():
    if not plans:
        print("체크할 계획이 없어요.\n")
        return
    
    view_plans()
    num = int(input("완료 체크할 번호: ")) - 1
    
    if 0 <= num < len(plans):
        plans[num]["done"] = True
        print("🎉 완료 처리되었습니다!\n")
    else:
        print("번호를 잘못 입력했어요.\n")

def total_time():
    total = sum(p["time"] for p in plans)
    print(f"\n 오늘 총 공부 예정 시간: {total}분\n")

def main():
    print("===== Study Planner =====")
    while True:
        print("1. 공부 계획 추가")
        print("2. 저장된 계획 보기")
        print("3. 완료 체크하기")
        print("4. 공부 시간 총합 보기")
        print("5. 종료")
        choice = input("메뉴 선택: ")

        if choice == "1":
            add_plan()
        elif choice == "2":
            view_plans()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            total_time()
        elif choice == "5":
            print("플래너 종료!")
            break
        else:
            print("메뉴를 다시 선택해주세요.\n")

main()