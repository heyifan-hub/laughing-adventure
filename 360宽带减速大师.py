import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import time

def restart_explorer():
    # 杀死资源管理器进程
    subprocess.run(['taskkill', '/f', '/im', 'explorer.exe'], check=False)
    # 重新启动资源管理器
    subprocess.Popen('explorer.exe')

def update_progressbar():
    # 设置进度条的长度为0到100
    progressbar['value'] = 0
    max_value = 100
    step = max_value // 10  # 假设我们重启资源管理器10次

    for i in range(0, max_value, step):
        restart_explorer()  # 重启资源管理器
        time.sleep(1)  # 等待1秒，模拟耗时操作
        progressbar['value'] += step
        root.update_idletasks()  # 更新界面

    # 进度条完成后显示消息框
    messagebox.showinfo("成功", "宽带减速成功")

# 创建主窗口
root = tk.Tk()
root.title("360宽带减速大师")
root.geometry("840x600")

# 创建按钮，点击后执行update_progressbar函数
button = tk.Button(root, text="点击减速宽带", command=update_progressbar, font=("Helvetica", 20))
button.pack(expand=True)

# 将按钮放置在窗口中间
button.place(relx=0.5, rely=0.3, anchor='center')

# 创建进度条
progressbar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progressbar.pack(pady=20)
# 将进度条放置在窗口中间
progressbar.place(relx=0.5, rely=0.7, anchor='center')

# 启动主循环
root.mainloop()
