#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
06_listbox_treeview.py - Tkinter列表框与树形控件演示

演示内容：
- Listbox的多选与滚动条整合
- Treeview树形表格的数据呈现
- 自定义列标题与数据排序
- 结合ttk.Style美化视图组件
"""

import tkinter as tk
from tkinter import ttk
import random

# 创建主窗口
root = tk.Tk()
root.title("信息展示大师 - 列表框与树")
root.geometry("800x600+100+100")
root.configure(bg="#f5f5f5")

# 创建一个Notebook(选项卡控件)来展示不同的控件
nb = ttk.Notebook(root)
nb.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# ===== 1. Listbox的多选与滚动条整合 =====
listbox_frame = ttk.Frame(nb, padding=10)
nb.add(listbox_frame, text="Listbox列表框")

# 创建说明标签
listbox_info = tk.Label(
    listbox_frame,
    text="Listbox用于显示选项列表，可以配置为单选或多选模式\n结合滚动条可以处理大量数据",
    justify=tk.LEFT,
    pady=10
)
listbox_info.pack(anchor=tk.W)

# 创建一个框架来容纳Listbox和滚动条
list_container = tk.Frame(listbox_frame)
list_container.pack(fill=tk.BOTH, expand=True, pady=10)

# 创建垂直滚动条
scrollbar = tk.Scrollbar(list_container)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 创建水平滚动条
hscrollbar = tk.Scrollbar(list_container, orient=tk.HORIZONTAL)
hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# 创建Listbox并关联滚动条
listbox = tk.Listbox(
    list_container,
    selectmode=tk.MULTIPLE,  # 多选模式
    yscrollcommand=scrollbar.set,
    xscrollcommand=hscrollbar.set,
    width=50,
    height=10
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 配置滚动条
scrollbar.config(command=listbox.yview)
hscrollbar.config(command=listbox.xview)

# 添加一些示例数据
programming_languages = [
    "Python", "Java", "JavaScript", "C++", "C#", "Ruby", "Go", "Swift",
    "Kotlin", "PHP", "Rust", "TypeScript", "Scala", "Perl", "Haskell",
    "Objective-C", "R", "Dart", "Lua", "Groovy", "Elixir", "Clojure"
]

for lang in programming_languages:
    listbox.insert(tk.END, lang)

# 创建控制按钮
control_frame = tk.Frame(listbox_frame)
control_frame.pack(fill=tk.X, pady=10)

# 获取选中项的函数
def get_selection():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(i) for i in selected_indices]
    if selected_items:
        result_label.config(text=f"已选择: {', '.join(selected_items)}")
    else:
        result_label.config(text="未选择任何项")

# 添加项的函数
def add_item():
    new_item = entry.get().strip()
    if new_item:
        listbox.insert(tk.END, new_item)
        entry.delete(0, tk.END)

# 删除选中项的函数
def delete_selected():
    selected_indices = listbox.curselection()
    # 从后向前删除，避免索引变化
    for i in sorted(selected_indices, reverse=True):
        listbox.delete(i)

# 创建输入框和按钮
input_frame = tk.Frame(control_frame)
input_frame.pack(fill=tk.X, pady=5)

tk.Label(input_frame, text="添加新项:").pack(side=tk.LEFT, padx=5)

entry = tk.Entry(input_frame, width=20)
entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
entry.bind("<Return>", lambda e: add_item())

tk.Button(input_frame, text="添加", command=add_item).pack(side=tk.LEFT, padx=5)
tk.Button(control_frame, text="获取选中项", command=get_selection).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(control_frame, text="删除选中项", command=delete_selected).pack(side=tk.LEFT, padx=5, pady=5)

# 创建结果显示标签
result_label = tk.Label(listbox_frame, text="请选择项目", pady=10)
result_label.pack()

# ===== 2. Treeview树形表格的数据呈现 =====
treeview_frame = ttk.Frame(nb, padding=10)
nb.add(treeview_frame, text="Treeview树形表格")

# 创建说明标签
treeview_info = tk.Label(
    treeview_frame,
    text="Treeview可以用来展示层级数据或表格数据\n支持列标题、排序和样式自定义",
    justify=tk.LEFT,
    pady=10
)
treeview_info.pack(anchor=tk.W)

# 创建一个框架来容纳Treeview和滚动条
tree_container = tk.Frame(treeview_frame)
tree_container.pack(fill=tk.BOTH, expand=True, pady=10)

# 创建垂直滚动条
tree_scrollbar = tk.Scrollbar(tree_container)
tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 创建水平滚动条
tree_hscrollbar = tk.Scrollbar(tree_container, orient=tk.HORIZONTAL)
tree_hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# 定义列
columns = ("name", "age", "gender", "occupation", "salary")

# 创建Treeview
tree = ttk.Treeview(
    tree_container,
    columns=columns,
    show="headings",  # 只显示标题行，不显示第一列
    yscrollcommand=tree_scrollbar.set,
    xscrollcommand=tree_hscrollbar.set
)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 配置滚动条
tree_scrollbar.config(command=tree.yview)
tree_hscrollbar.config(command=tree.xview)

# 定义列标题
tree.heading("name", text="姓名")
tree.heading("age", text="年龄")
tree.heading("gender", text="性别")
tree.heading("occupation", text="职业")
tree.heading("salary", text="薪资")

# 定义列宽
tree.column("name", width=100, anchor=tk.W)
tree.column("age", width=50, anchor=tk.CENTER)
tree.column("gender", width=50, anchor=tk.CENTER)
tree.column("occupation", width=150, anchor=tk.W)
tree.column("salary", width=100, anchor=tk.E)

# 添加一些示例数据
sample_data = [
    ("张三", 28, "男", "软件工程师", "¥15,000"),
    ("李四", 35, "男", "产品经理", "¥20,000"),
    ("王五", 42, "男", "技术总监", "¥35,000"),
    ("赵六", 25, "女", "UI设计师", "¥12,000"),
    ("钱七", 31, "女", "市场专员", "¥18,000"),
    ("孙八", 29, "男", "前端开发", "¥16,000"),
    ("周九", 36, "女", "人力资源", "¥14,000"),
    ("吴十", 45, "男", "财务总监", "¥30,000"),
]

# 插入数据
for item in sample_data:
    tree.insert("", tk.END, values=item)

# 创建排序函数
def sort_treeview(col, reverse):
    # 获取所有项
    data = [(tree.set(item, col), item) for item in tree.get_children('')]
    
    # 特殊处理年龄和薪资列
    if col == "age":
        # 按数字排序
        data.sort(key=lambda x: int(x[0]), reverse=reverse)
    elif col == "salary":
        # 去除货币符号和逗号，按数字排序
        data.sort(key=lambda x: int(x[0].replace("¥", "").replace(",", "")), reverse=reverse)
    else:
        # 按字符串排序
        data.sort(reverse=reverse)
    
    # 重新排列项
    for index, (val, item) in enumerate(data):
        tree.move(item, "", index)
    
    # 切换排序方向
    tree.heading(col, command=lambda: sort_treeview(col, not reverse))

# 配置列标题点击事件
for col in columns:
    tree.heading(col, command=lambda c=col: sort_treeview(c, False))

# 创建控制按钮
tree_control_frame = tk.Frame(treeview_frame)
tree_control_frame.pack(fill=tk.X, pady=10)

# 添加新行的函数
def add_row():
    # 生成随机数据
    names = ["张", "李", "王", "赵", "钱", "孙", "周", "吴", "郑", "陈"]
    surnames = ["明", "华", "强", "伟", "芳", "娜", "军", "杰", "艳", "超"]
    occupations = ["工程师", "设计师", "经理", "顾问", "专员", "助理", "总监", "主管"]
    
    name = random.choice(names) + random.choice(surnames)
    age = random.randint(22, 55)
    gender = random.choice(["男", "女"])
    occupation = random.choice(occupations)
    salary = f"¥{random.randint(8, 40):,}000"
    
    # 插入数据
    tree.insert("", tk.END, values=(name, age, gender, occupation, salary))

# 删除选中行的函数
def delete_row():
    selected = tree.selection()
    for item in selected:
        tree.delete(item)

# 获取选中行的函数
def get_row():
    selected = tree.selection()
    if selected:
        values = tree.item(selected[0], "values")
        tree_result_label.config(text=f"已选择: {values}")
    else:
        tree_result_label.config(text="未选择任何行")

tk.Button(tree_control_frame, text="添加随机行", command=add_row).pack(side=tk.LEFT, padx=5)
tk.Button(tree_control_frame, text="删除选中行", command=delete_row).pack(side=tk.LEFT, padx=5)
tk.Button(tree_control_frame, text="获取选中行", command=get_row).pack(side=tk.LEFT, padx=5)

# 创建结果显示标签
tree_result_label = tk.Label(treeview_frame, text="请选择一行数据", pady=10)
tree_result_label.pack()

# ===== 3. 自定义样式 =====
style_frame = ttk.Frame(nb, padding=10)
nb.add(style_frame, text="自定义样式")

# 创建说明标签
style_info = tk.Label(
    style_frame,
    text="ttk.Style可以用来自定义Treeview和其他ttk组件的外观\n以下是一些样式自定义的示例",
    justify=tk.LEFT,
    pady=10
)
style_info.pack(anchor=tk.W)

# 创建样式对象
style = ttk.Style()

# 创建一个框架来容纳样式示例
style_demo_frame = tk.Frame(style_frame)
style_demo_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 创建一个简单的Treeview用于样式演示
style_tree = ttk.Treeview(
    style_demo_frame,
    columns=("col1", "col2"),
    show="headings",
    height=8
)
style_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# 配置列
style_tree.heading("col1", text="项目")
style_tree.heading("col2", text="值")
style_tree.column("col1", width=150, anchor=tk.W)
style_tree.column("col2", width=250, anchor=tk.W)

# 添加一些数据
for i in range(1, 11):
    style_tree.insert("", tk.END, values=(f"项目 {i}", f"值 {i}"))

# 创建样式控制按钮
style_control_frame = tk.Frame(style_frame)
style_control_frame.pack(fill=tk.X, pady=10)

# 定义样式变更函数
def apply_default_style():
    style.configure("Treeview", 
                    background="#ffffff",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#ffffff")
    style.configure("Treeview.Heading",
                    background="#e6e6e6", 
                    foreground="black",
                    relief="flat")
    style.map("Treeview",
              background=[('selected', '#0078d7')])

def apply_dark_style():
    style.configure("Treeview", 
                    background="#2d2d30",
                    foreground="white",
                    rowheight=25,
                    fieldbackground="#2d2d30")
    style.configure("Treeview.Heading",
                    background="#1e1e1e", 
                    foreground="white",
                    relief="flat")
    style.map("Treeview",
              background=[('selected', '#007acc')])

def apply_colorful_style():
    style.configure("Treeview", 
                    background="#f0f0f0",
                    foreground="#333333",
                    rowheight=25,
                    fieldbackground="#f0f0f0")
    style.configure("Treeview.Heading",
                    background="#4CAF50", 
                    foreground="white",
                    relief="flat")
    style.map("Treeview",
              background=[('selected', '#ff9800')])
    
    # 为奇偶行设置不同背景色
    style_tree.tag_configure('oddrow', background='#e6f7ff')
    style_tree.tag_configure('evenrow', background='#ffffff')
    
    # 应用标签
    for i, item in enumerate(style_tree.get_children()):
        if i % 2 == 0:
            style_tree.item(item, tags=('evenrow',))
        else:
            style_tree.item(item, tags=('oddrow',))

# 创建样式按钮
tk.Button(style_control_frame, text="默认样式", command=apply_default_style).pack(side=tk.LEFT, padx=5)
tk.Button(style_control_frame, text="暗黑模式", command=apply_dark_style).pack(side=tk.LEFT, padx=5)
tk.Button(style_control_frame, text="多彩样式", command=apply_colorful_style).pack(side=tk.LEFT, padx=5)

# 应用默认样式
apply_default_style()

# 启动主事件循环
root.mainloop()