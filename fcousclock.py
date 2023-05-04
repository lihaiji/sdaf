import time

def focus_timer(minutes):
    seconds = minutes * 60
    while True:
        if seconds == 0:
            print("时间到！")
            break
        print(f"剩余时间：{seconds//60} 分钟 {seconds%60} 秒。")
        time.sleep(1)
        seconds -= 1

focus_timer(25) # 设定专注时长为25分钟
