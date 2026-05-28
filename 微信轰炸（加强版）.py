import time
from pynput import mouse, keyboard

m_keyboard = keyboard.Controller()

while True:
    try:
        qty = int(input("轰炸次数："))
        break
    except ValueError:
        print("输入无效，请输入一个整数。")

content = input("轰炸内容：")

while True:
    try:
        time_Span = int(input("开始轰炸时间（s）："))
        break
    except ValueError:
        print("输入无效，请输入一个整数。")

while True:
    try:
        frequency = float(input("轰炸频率（0.1-0.5）："))
        if 0.1 <= frequency <= 0.5:
            break
        else:
            print("输入无效，请输入一个在 0.1 - 0.5 范围内的数字。")
    except ValueError:
        print("输入无效，请输入一个有效的数字。")

print("选择轰炸区域", time_Span, "秒后开始轰炸")

try:
    time.sleep(time_Span)

    for i in range(qty):
        m_keyboard.type(content)
        m_keyboard.press(keyboard.Key.enter)
        m_keyboard.release(keyboard.Key.enter)
        time.sleep(frequency)
except Exception as e:
    print(f"发生错误：{e}")