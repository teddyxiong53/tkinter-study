#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
01_hello_gui_world.py - Tkinter窗口基础演示

演示内容：
- 创建第一个窗口 (Tk())
- 窗口属性设置 (标题/尺寸/图标)
- mainloop()机制理解
- 核心对象：Frame容器的运用
"""

import tkinter as tk

# 创建主窗口
root = tk.Tk()

# 设置窗口标题
root.title("Hello GUI World")

# 设置窗口尺寸和位置 (宽度x高度+x坐标+y坐标)
root.geometry("400x300+100+100")

# 设置窗口最小尺寸
root.minsize(300, 200)

# 设置窗口图标 (如果有图标文件的话)
# root.iconbitmap('icon.ico')  # 在Windows上使用

# 创建一个Frame容器
main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
# 使用pack布局管理器将Frame填充到整个窗口
main_frame.pack(fill=tk.BOTH, expand=True)

# 在Frame中添加一个标签
label = tk.Label(
    main_frame,
    text="欢迎使用Tkinter!",
    font=("Arial", 18),
    bg="#f0f0f0"
)
label.pack(pady=50)

# 添加一个子Frame，展示Frame的嵌套使用
sub_frame = tk.Frame(main_frame, bg="#e0e0e0", padx=10, pady=10, bd=1, relief=tk.RAISED)
sub_frame.pack(fill=tk.X)

# 在子Frame中添加说明文本
info_label = tk.Label(
    sub_frame,
    text="这是一个基本的Tkinter窗口示例\n展示了窗口创建和Frame容器的使用",
    bg="#e0e0e0",
    justify=tk.LEFT
)
info_label.pack(pady=10)

# 添加一个按钮用于关闭窗口
close_button = tk.Button(main_frame, text="关闭窗口", command=root.destroy)
close_button.pack(pady=20)

# 显示说明
print("窗口已创建并显示。")
print("mainloop()将开始事件循环，等待用户交互。")
print("关闭窗口或点击'关闭窗口'按钮将终止程序。")

# 启动主事件循环
# mainloop()会阻塞程序执行，直到窗口被关闭
# 它负责处理所有的用户交互事件（如点击、键盘输入等）
root.mainloop()

print("窗口已关闭，程序结束。")  # 这行代码只有在mainloop结束后才会执行