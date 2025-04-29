#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
07_menu_dialog.py - Tkinter菜单与对话框演示

演示内容：
- Menu/Menubutton层级菜单构建
- 快捷菜单的弹出实现 (post()方法)
- filedialog文件选择器实践
- messagebox的八种交互弹窗
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

# 创建主窗口
root = tk.Tk()
root.title("专业界面打造 - 菜单与对话框")
root.geometry("700x500+100+100")
root.configure(bg="#f5f5f5")

# 创建状态栏
status_bar = tk.Label(root, text="就绪", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# 创建主框架
main_frame = tk.Frame(root, bg="#f5f5f5")
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# ===== 1. 创建主菜单 =====
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# 文件菜单
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="文件", menu=file_menu)

# 文件菜单项
def new_file():
    status_bar.config(text="创建了新文件")
    text_area.delete(1.0, tk.END)
    root.title("专业界面打造 - 菜单与对话框 - 新文件")

def open_file():
    file_path = filedialog.askopenfilename(
        title="打开文件",
        filetypes=[("文本文件", "*.txt"), ("Python文件", "*.py"), ("所有文件", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
                status_bar.config(text=f"已打开: {file_path}")
                root.title(f"专业界面打造 - 菜单与对话框 - {os.path.basename(file_path)}")
        except Exception as e:
            messagebox.showerror("错误", f"无法打开文件: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(
        title="保存文件",
        defaultextension=".txt",
        filetypes=[("文本文件", "*.txt"), ("Python文件", "*.py"), ("所有文件", "*.*")]
    )
    if file_path:
        try:
            content = text_area.get(1.0, tk.END)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            status_bar.config(text=f"已保存: {file_path}")
            root.title(f"专业界面打造 - 菜单与对话框 - {os.path.basename(file_path)}")
        except Exception as e:
            messagebox.showerror("错误", f"无法保存文件: {e}")

file_menu.add_command(label="新建", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="打开", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="保存", command=save_file, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="退出", command=root.destroy, accelerator="Alt+F4")

# 编辑菜单
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="编辑", menu=edit_menu)

def cut_text():
    text_area.event_generate("<<Cut>>")
    status_bar.config(text="已剪切")

def copy_text():
    text_area.event_generate("<<Copy>>")
    status_bar.config(text="已复制")

def paste_text():
    text_area.event_generate("<<Paste>>")
    status_bar.config(text="已粘贴")

edit_menu.add_command(label="剪切", command=cut_text, accelerator="Ctrl+X")
edit_menu.add_command(label="复制", command=copy_text, accelerator="Ctrl+C")
edit_menu.add_command(label="粘贴", command=paste_text, accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="全选", command=lambda: text_area.tag_add(tk.SEL, "1.0", tk.END), accelerator="Ctrl+A")

# 视图菜单
view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="视图", menu=view_menu)

# 创建字体大小子菜单
font_size_menu = tk.Menu(view_menu, tearoff=0)
view_menu.add_cascade(label="字体大小", menu=font_size_menu)

font_sizes = [8, 10, 12, 14, 16, 18, 20]
font_var = tk.IntVar()
font_var.set(12)  # 默认字体大小

def change_font_size(size):
    text_area.config(font=("TkDefaultFont", size))
    font_var.set(size)
    status_bar.config(text=f"字体大小已更改为 {size}")

for size in font_sizes:
    font_size_menu.add_radiobutton(
        label=str(size),
        variable=font_var,
        value=size,
        command=lambda s=size: change_font_size(s)
    )

# 创建主题子菜单
theme_menu = tk.Menu(view_menu, tearoff=0)
view_menu.add_cascade(label="主题", menu=theme_menu)

themes = {"默认": {"bg": "#ffffff", "fg": "#000000"},
          "暗黑": {"bg": "#2d2d30", "fg": "#ffffff"},
          "蓝色": {"bg": "#e6f3ff", "fg": "#000000"},
          "绿色": {"bg": "#e6ffe6", "fg": "#000000"}}

theme_var = tk.StringVar()
theme_var.set("默认")  # 默认主题

def change_theme(theme_name):
    theme = themes[theme_name]
    text_area.config(bg=theme["bg"], fg=theme["fg"])
    theme_var.set(theme_name)
    status_bar.config(text=f"主题已更改为 {theme_name}")

for theme_name in themes:
    theme_menu.add_radiobutton(
        label=theme_name,
        variable=theme_var,
        value=theme_name,
        command=lambda t=theme_name: change_theme(t)
    )

# 帮助菜单
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="帮助", menu=help_menu)

def show_about():
    messagebox.showinfo(
        "关于",
        "Tkinter菜单与对话框演示\n版本 1.0\n\n这是一个展示Tkinter菜单和对话框功能的示例程序。"
    )

help_menu.add_command(label="关于", command=show_about)

# ===== 2. 创建文本区域 =====
text_frame = tk.Frame(main_frame)
text_frame.pack(fill=tk.BOTH, expand=True)

# 创建滚动条
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 创建文本区域
text_area = tk.Text(
    text_frame,
    font=("TkDefaultFont", 12),
    yscrollcommand=scrollbar.set,
    wrap=tk.WORD,
    undo=True
)
text_area.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=text_area.yview)

# 插入一些示例文本
text_area.insert(tk.END, "这是一个菜单和对话框演示程序。\n\n")
text_area.insert(tk.END, "您可以尝试以下功能：\n")
text_area.insert(tk.END, "1. 使用文件菜单打开和保存文件\n")
text_area.insert(tk.END, "2. 使用编辑菜单剪切、复制和粘贴文本\n")
text_area.insert(tk.END, "3. 使用视图菜单更改字体大小和主题\n")
text_area.insert(tk.END, "4. 右键点击显示上下文菜单\n")
text_area.insert(tk.END, "5. 点击下方的按钮尝试不同类型的对话框\n")

# ===== 3. 创建右键菜单 =====
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="剪切", command=cut_text)
context_menu.add_command(label="复制", command=copy_text)
context_menu.add_command(label="粘贴", command=paste_text)
context_menu.add_separator()
context_menu.add_command(label="全选", command=lambda: text_area.tag_add(tk.SEL, "1.0", tk.END))

# 绑定右键点击事件
def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

text_area.bind("<Button-3>", show_context_menu)

# ===== 4. 创建Menubutton示例 =====
menubutton_frame = tk.LabelFrame(main_frame, text="Menubutton示例", padx=10, pady=10)
menubutton_frame.pack(fill=tk.X, pady=10)

# 创建一个Menubutton
color_menubutton = tk.Menubutton(
    menubutton_frame,
    text="选择颜色",
    relief=tk.RAISED
)
color_menubutton.pack(side=tk.LEFT, padx=10)

# 创建Menubutton的菜单
color_menu = tk.Menu(color_menubutton, tearoff=0)
color_menubutton.config(menu=color_menu)

# 添加菜单项
colors = [("红色", "#ff0000"), ("绿色", "#00ff00"), ("蓝色", "#0000ff"),
          ("黄色", "#ffff00"), ("紫色", "#800080"), ("青色", "#00ffff")]

def change_text_color(color):
    text_area.tag_configure("colored", foreground=color)
    text_area.tag_add("colored", "1.0", tk.END)
    status_bar.config(text=f"文本颜色已更改")

for color_name, color_code in colors:
    color_menu.add_command(
        label=color_name,
        command=lambda c=color_code: change_text_color(c)
    )

# ===== 5. 创建对话框示例 =====
dialog_frame = tk.LabelFrame(main_frame, text="对话框示例", padx=10, pady=10)
dialog_frame.pack(fill=tk.X, pady=10)

# 创建不同类型的对话框按钮
def show_info():
    messagebox.showinfo("信息", "这是一个信息对话框")

def show_warning():
    messagebox.showwarning("警告", "这是一个警告对话框")

def show_error():
    messagebox.showerror("错误", "这是一个错误对话框")

def show_question():
    result = messagebox.askquestion("问题", "这是一个问题对话框，您想继续吗？")
    status_bar.config(text=f"回答: {'是' if result == 'yes' else '否'}")

def show_okcancel():
    result = messagebox.askokcancel("确认", "这是一个确认对话框，您想继续吗？")
    status_bar.config(text=f"回答: {'确定' if result else '取消'}")

def show_yesno():
    result = messagebox.askyesno("是/否", "这是一个是/否对话框，您想继续吗？")
    status_bar.config(text=f"回答: {'是' if result else '否'}")

def show_retrycancel():
    result = messagebox.askretrycancel("重试", "操作失败，您想重试吗？")
    status_bar.config(text=f"回答: {'重试' if result else '取消'}")

def show_yesnocancel():
    result = messagebox.askyesnocancel("是/否/取消", "您想保存更改吗？")
    if result is None:
        status_bar.config(text="回答: 取消")
    else:
        status_bar.config(text=f"回答: {'是' if result else '否'}")

# 创建文件对话框按钮
def show_open_file():
    file_path = filedialog.askopenfilename(
        title="打开文件",
        filetypes=[("文本文件", "*.txt"), ("Python文件", "*.py"), ("所有文件", "*.*")]
    )
    if file_path:
        status_bar.config(text=f"选择的文件: {file_path}")

def show_save_file():
    file_path = filedialog.asksaveasfilename(
        title="保存文件",
        defaultextension=".txt",
        filetypes=[("文本文件", "*.txt"), ("Python文件", "*.py"), ("所有文件", "*.*")]
    )
    if file_path:
        status_bar.config(text=f"保存的文件: {file_path}")

def show_select_dir():
    dir_path = filedialog.askdirectory(title="选择目录")
    if dir_path:
        status_bar.config(text=f"选择的目录: {dir_path}")

# 创建消息框按钮
message_frame = tk.Frame(dialog_frame)
message_frame.pack(fill=tk.X, pady=5)

tk.Label(message_frame, text="消息框:").pack(side=tk.LEFT, padx=5)
tk.Button(message_frame, text="信息", command=show_info, width=8).pack(side=tk.LEFT, padx=2)
tk.Button(message_frame, text="警告", command=show_warning, width=8).pack(side=tk.LEFT, padx=2)
tk.Button(message_frame, text="错误", command=show_error, width=8).pack(side=tk.LEFT, padx=2)

# 创建询问框按钮
ask_frame = tk.Frame(dialog_frame)
ask_frame.pack(fill=tk.X, pady=5)

tk.Label(ask_frame, text="询问框:").pack(side=tk.LEFT, padx=5)
tk.Button(ask_frame, text="问题", command=show_question, width=8).pack(side=tk.LEFT, padx=2)
tk.Button(ask_frame, text="确认", command=show_okcancel, width=8).pack(side=tk.LEFT, padx=2)
tk.Button(ask_frame, text="是/否", command=show_yesno, width=8).pack(side=tk.LEFT, padx=2)
tk.Button(ask_frame, text="重试", command=show_retrycancel, width=8).pack(side=tk.LEFT, padx=2)
tk.Button(ask_frame, text="三选项", command=show_yesnocancel, width=8).pack(side=tk.LEFT, padx=2)

# 创建文件对话框按钮
file_dialog_frame = tk.Frame(dialog_frame)
file_dialog_frame.pack(fill=tk.X, pady=5)

tk.Label(file_dialog_frame, text="文件对话框:").pack(side=tk.LEFT, padx=5)
tk.Button(file_dialog_frame, text="打开文件", command=show_open_file, width=8).pack(side=tk.LEFT, padx=2)
tk.Button(file_dialog_frame, text="保存文件", command=show_save_file, width=8).pack(side=tk.LEFT, padx=2)
tk.Button(file_dialog_frame, text="选择目录", command=show_select_dir, width=8).pack(side=tk.LEFT, padx=2)

# 绑定键盘快捷键
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())

# 启动主事件循环
root.mainloop()