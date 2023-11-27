import time
from datetime import datetime, timedelta

def focus_timer(duration_minutes):
    end_time = datetime.now() + timedelta(minutes=duration_minutes)

    print(f"专注时钟启动，将持续 {duration_minutes} 分钟.")

    while datetime.now() < end_time:
        time_left = end_time - datetime.now()
        print(f"剩余时间: {time_left.seconds // 60} 分钟 {time_left.seconds % 60} 秒", end='\r')
        time.sleep(1)

    print("\n专注时钟结束！")

# 设置专注时长为25分钟（可以根据需要调整）
focus_timer(25)
