
import tkinter as tk
import datetime
import threading

# 좌석 예약 정보를 저장하는 딕셔너리
seats = {'Seat 1': False, 'Seat 2': False}

# 좌석 예약 함수
def reserve_seat(seat_name):
    set_time = 10
    add_time = 5
    if seats[seat_name]:
        print(f'{seat_name}은 이미 예약되어 있습니다.')
    else:
        seats[seat_name] = True
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{seat_name}이 {current_time}에 예약되었습니다.')
        reserve_buttons[seat_name].grid_forget()
        return_buttons[seat_name].grid(row=list(seats.keys()).index(seat_name), column=1)

        # 예약 종료를 위한 타이머 시작
        def end_reservation():
            seats[seat_name] = False
            return_buttons[seat_name].grid_forget()
            reserve_buttons[seat_name].grid(row=list(seats.keys()).index(seat_name), column=0)
            print(f'{seat_name}의 예약이 자동으로 취소되었습니다.')
        
        # 타이머 생성
        timer = threading.Timer(set_time, end_reservation)
        timer.start()

        # 예약 연장 함수
        def extend_reservation():
            nonlocal timer
            if seats[seat_name]:
                timer.cancel()
                timer = threading.Timer(set_time + add_time, end_reservation)
                timer.start()
                print(f'{seat_name}의 예약이 5초 연장되었습니다.')
            else:
                print(f'{seat_name}은 예약되어 있지 않아 연장할 수 없습니다.')

        # 예약 연장 버튼 생성
        extend_button = tk.Button(window, text=f'{seat_name} 연장', command=extend_reservation)
        extend_button.grid(row=list(seats.keys()).index(seat_name), column=2, padx=10, pady=10)

# 좌석 반납 함수
def return_seat(seat_name):
    if not seats[seat_name]:
        print(f'{seat_name}은 이미 반납되었습니다.')
    else:
        seats[seat_name] = False
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{seat_name}이 {current_time}에 반납되었습니다.')
        return_buttons[seat_name].grid_forget()
        reserve_buttons[seat_name].grid(row=list(seats.keys()).index(seat_name), column=0)

# Tkinter 윈도우 생성
window = tk.Tk()

# 좌석 예약 및 반납 버튼 생성 및 배치
reserve_buttons = {}
return_buttons = {}
for i, seat_name in enumerate(seats.keys()):
    reserve_button = tk.Button(window, text=f'{seat_name} 예약', command=lambda name=seat_name: reserve_seat(name))
    reserve_button.grid(row=i, column=0, padx=10, pady=10)
    reserve_buttons[seat_name] = reserve_button
    return_button = tk.Button(window, text=f'{seat_name} 반납', command=lambda name=seat_name: return_seat(name))
    return_buttons[seat_name] = return_button

# 윈도우 실행
window.mainloop()

