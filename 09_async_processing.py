#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
09_async_processing.py - Tkinter异步处理演示

演示内容：
- after()模拟定时任务的局限
- 多线程与队列 (queue.Queue) 架构
- 防止GUI冻结的正确线程处理
- 使用threading模块整合后台任务
"""

import tkinter as tk
from tkinter import ttk
import time
import threading
import queue
import random

# 创建主窗口
root = tk.Tk()
root.title("跨线程的智慧 - 异步处理")
root.geometry("700x600+100+100")
root.configure(bg="#f5f5f5")

# 创建一个Notebook(选项卡控件)来展示不同的异步处理方式
nb = ttk.Notebook(root)
nb.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# ===== 1. after()方法演示 =====
after_frame = ttk.Frame(nb, padding=10)
nb.add(after_frame, text="after()方法")

# 创建说明标签
after_info = tk.Label(
    after_frame,
    text="after()方法可以在指定的毫秒数后执行一个函数\n可以用来创建简单的定时任务，但不适合耗时操作",
    justify=tk.LEFT,
    pady=10
)
after_info.pack(anchor=tk.W)

# 创建一个进度条
after_progress = ttk.Progressbar(after_frame, orient=tk.HORIZONTAL, length=300, mode='determinate')
after_progress.pack(pady=20)

# 创建状态标签
after_status = tk.Label(after_frame, text="就绪", pady=10)
after_status.pack()

# 创建一个计数器显示
after_counter = tk.Label(after_frame, text="0", font=("Arial", 24), pady=10)
after_counter.pack()

# 使用after()方法实现计数器
def start_counter():
    count = 0
    after_progress['value'] = 0
    after_status.config(text="计数中...")
    
    def update_counter():
        nonlocal count
        count += 1
        after_counter.config(text=str(count))
        after_progress['value'] = count
        
        if count < 100:
            # 每100毫秒更新一次
            counter_id = root.after(100, update_counter)
            # 保存ID以便取消
            after_counter.counter_id = counter_id
        else:
            after_status.config(text="完成！")
            start_button.config(state=tk.NORMAL)
            stop_button.config(state=tk.DISABLED)
    
    # 开始计数
    update_counter()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

# 停止计数器
def stop_counter():
    if hasattr(after_counter, 'counter_id'):
        root.after_cancel(after_counter.counter_id)
        after_status.config(text="已停止")
        start_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)

# 创建控制按钮
after_control_frame = tk.Frame(after_frame)
after_control_frame.pack(pady=10)

start_button = tk.Button(after_control_frame, text="开始", command=start_counter)
start_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(after_control_frame, text="停止", command=stop_counter, state=tk.DISABLED)
stop_button.pack(side=tk.LEFT, padx=5)

# 演示after()方法的局限性
def simulate_blocking_operation():
    after_status.config(text="执行耗时操作...")
    start_time = time.time()
    
    # 模拟耗时操作（这会阻塞GUI）
    time.sleep(3)
    
    elapsed = time.time() - start_time
    after_status.config(text=f"耗时操作完成，用时: {elapsed:.2f}秒")
    after_counter.config(text="注意：GUI在操作期间被冻结")

block_button = tk.Button(after_frame, text="执行阻塞操作（会冻结GUI）", command=simulate_blocking_operation)
block_button.pack(pady=10)

# ===== 2. 多线程演示 =====
thread_frame = ttk.Frame(nb, padding=10)
nb.add(thread_frame, text="多线程")

# 创建说明标签
thread_info = tk.Label(
    thread_frame,
    text="使用threading模块可以创建后台线程执行耗时操作\n避免阻塞GUI主线程，保持界面响应",
    justify=tk.LEFT,
    pady=10
)
thread_info.pack(anchor=tk.W)

# 创建一个进度条
thread_progress = ttk.Progressbar(thread_frame, orient=tk.HORIZONTAL, length=300, mode='determinate')
thread_progress.pack(pady=20)

# 创建状态标签
thread_status = tk.Label(thread_frame, text="就绪", pady=10)
thread_status.pack()

# 创建一个文本区域显示结果
thread_result = tk.Text(thread_frame, width=50, height=10, wrap=tk.WORD)
thread_result.pack(pady=10)

# 模拟耗时计算的函数
def heavy_calculation(progress_callback=None, result_callback=None):
    # 模拟一个耗时的计算过程
    result = 0
    for i in range(100):
        # 执行一些计算
        result += i * random.random()
        
        # 模拟计算耗时
        time.sleep(0.1)
        
        # 更新进度
        if progress_callback:
            progress_callback(i + 1)
    
    # 返回结果
    if result_callback:
        result_callback(f"计算结果: {result:.2f}")

# 在线程中执行耗时操作
def start_thread_calculation():
    thread_progress['value'] = 0
    thread_status.config(text="计算中...")
    thread_result.delete(1.0, tk.END)
    thread_start_button.config(state=tk.DISABLED)
    
    def update_progress(value):
        thread_progress['value'] = value
    
    def update_result(result):
        thread_result.insert(tk.END, result + "\n")
        thread_status.config(text="计算完成！")
        thread_start_button.config(state=tk.NORMAL)
    
    # 创建并启动线程
    calculation_thread = threading.Thread(
        target=heavy_calculation,
        args=(update_progress, update_result)
    )
    calculation_thread.daemon = True  # 设置为守护线程，随主线程退出
    calculation_thread.start()
    
    # 注意：由于线程安全问题，我们不能直接在线程中更新GUI
    # 而是通过回调函数，让主线程来更新GUI
    thread_result.insert(tk.END, "计算已在后台线程启动...\n")
    thread_result.insert(tk.END, "注意：GUI仍然可以响应，尝试调整窗口大小或点击其他选项卡\n")

# 创建控制按钮
thread_control_frame = tk.Frame(thread_frame)
thread_control_frame.pack(pady=10)

thread_start_button = tk.Button(thread_control_frame, text="开始耗时计算", command=start_thread_calculation)
thread_start_button.pack()

# ===== 3. 队列演示 =====
queue_frame = ttk.Frame(nb, padding=10)
nb.add(queue_frame, text="队列")

# 创建说明标签
queue_info = tk.Label(
    queue_frame,
    text="使用queue.Queue可以安全地在线程间传递数据\n结合after()方法可以定期检查队列，更新GUI",
    justify=tk.LEFT,
    pady=10
)
queue_info.pack(anchor=tk.W)

# 创建一个进度条
queue_progress = ttk.Progressbar(queue_frame, orient=tk.HORIZONTAL, length=300, mode='determinate')
queue_progress.pack(pady=20)

# 创建状态标签
queue_status = tk.Label(queue_frame, text="就绪", pady=10)
queue_status.pack()

# 创建一个文本区域显示结果
queue_result = tk.Text(queue_frame, width=50, height=10, wrap=tk.WORD)
queue_result.pack(pady=10)

# 创建一个队列用于线程间通信
result_queue = queue.Queue()

# 模拟数据处理的函数
def process_data():
    # 模拟处理一批数据
    for i in range(100):
        # 执行一些处理
        data = {
            'progress': i + 1,
            'value': i * random.random()
        }
        
        # 将结果放入队列
        result_queue.put(data)
        
        # 模拟处理耗时
        time.sleep(0.1)
    
    # 处理完成标记
    result_queue.put(None)

# 启动数据处理
def start_queue_processing():
    queue_progress['value'] = 0
    queue_status.config(text="处理中...")
    queue_result.delete(1.0, tk.END)
    queue_start_button.config(state=tk.DISABLED)
    
    # 清空队列（以防之前的处理未完成）
    while not result_queue.empty():
        result_queue.get()
    
    # 创建并启动线程
    processing_thread = threading.Thread(target=process_data)
    processing_thread.daemon = True
    processing_thread.start()
    
    # 开始检查队列
    check_queue()

# 检查队列并更新GUI
def check_queue():
    try:
        # 非阻塞方式获取队列数据
        data = result_queue.get_nowait()
        
        if data is None:
            # 处理完成
            queue_status.config(text="处理完成！")
            queue_start_button.config(state=tk.NORMAL)
        else:
            # 更新进度和结果
            queue_progress['value'] = data['progress']
            queue_result.insert(tk.END, f"处理项 {data['progress']}: {data['value']:.4f}\n")
            queue_result.see(tk.END)  # 滚动到最后
            
            # 继续检查队列
            root.after(10, check_queue)
    
    except queue.Empty:
        # 队列为空，等待一段时间后再检查
        root.after(100, check_queue)

# 创建控制按钮
queue_control_frame = tk.Frame(queue_frame)
queue_control_frame.pack(pady=10)

queue_start_button = tk.Button(queue_control_frame, text="开始数据处理", command=start_queue_processing)
queue_start_button.pack()

# ===== 4. 综合应用 =====
advanced_frame = ttk.Frame(nb, padding=10)
nb.add(advanced_frame, text="综合应用")

# 创建说明标签
advanced_info = tk.Label(
    advanced_frame,
    text="综合应用多线程、队列和定时器，实现复杂的后台任务\n同时保持GUI的响应性",
    justify=tk.LEFT,
    pady=10
)
advanced_info.pack(anchor=tk.W)

# 创建一个模拟的数据监控界面
monitor_frame = tk.LabelFrame(advanced_frame, text="系统监控", padx=10, pady=10)
monitor_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 创建几个监控指标
cpu_frame = tk.Frame(monitor_frame)
cpu_frame.pack(fill=tk.X, pady=5)

tk.Label(cpu_frame, text="CPU使用率:", width=15, anchor=tk.W).pack(side=tk.LEFT)
cpu_progress = ttk.Progressbar(cpu_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
cpu_progress.pack(side=tk.LEFT, padx=5)
cpu_value = tk.Label(cpu_frame, text="0%", width=10)
cpu_value.pack(side=tk.LEFT)

mem_frame = tk.Frame(monitor_frame)
mem_frame.pack(fill=tk.X, pady=5)

tk.Label(mem_frame, text="内存使用率:", width=15, anchor=tk.W).pack(side=tk.LEFT)
mem_progress = ttk.Progressbar(mem_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
mem_progress.pack(side=tk.LEFT, padx=5)
mem_value = tk.Label(mem_frame, text="0%", width=10)
mem_value.pack(side=tk.LEFT)

disk_frame = tk.Frame(monitor_frame)
disk_frame.pack(fill=tk.X, pady=5)

tk.Label(disk_frame, text="磁盘I/O:", width=15, anchor=tk.W).pack(side=tk.LEFT)
disk_progress = ttk.Progressbar(disk_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
disk_progress.pack(side=tk.LEFT, padx=5)
disk_value = tk.Label(disk_frame, text="0 MB/s", width=10)
disk_value.pack(side=tk.LEFT)

net_frame = tk.Frame(monitor_frame)
net_frame.pack(fill=tk.X, pady=5)

tk.Label(net_frame, text="网络流量:", width=15, anchor=tk.W).pack(side=tk.LEFT)
net_progress = ttk.Progressbar(net_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
net_progress.pack(side=tk.LEFT, padx=5)
net_value = tk.Label(net_frame, text="0 KB/s", width=10)
net_value.pack(side=tk.LEFT)

# 创建日志区域
log_frame = tk.LabelFrame(advanced_frame, text="系统日志", padx=10, pady=10)
log_frame.pack(fill=tk.BOTH, expand=True, pady=10)

log_text = tk.Text(log_frame, width=50, height=5, wrap=tk.WORD)
log_text.pack(fill=tk.BOTH, expand=True)

# 创建日志滚动条
log_scrollbar = tk.Scrollbar(log_text)
log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log_text.config(yscrollcommand=log_scrollbar.set)
log_scrollbar.config(command=log_text.yview)

# 创建控制按钮
advanced_control_frame = tk.Frame(advanced_frame)
advanced_control_frame.pack(pady=10)

# 创建一个队列用于监控数据
monitor_queue = queue.Queue()

# 监控数据生成器
def generate_monitor_data():
    # 模拟系统监控数据
    while monitoring_active:
        # 生成随机监控数据
        cpu = random.randint(10, 90)
        mem = random.randint(20, 80)
        disk = random.randint(0, 100) / 10  # 0-10 MB/s
        net = random.randint(0, 1000)  # 0-1000 KB/s
        
        # 创建日志消息
        log_msg = f"[{time.strftime('%H:%M:%S')}] "
        
        # 随机添加一些系统事件
        events = [
            "系统正常运行中",
            f"CPU使用率峰值: {cpu}%",
            f"内存使用增加到: {mem}%",
            f"磁盘写入速度: {disk:.1f} MB/s",
            f"网络下载速度: {net} KB/s",
            "后台服务已启动",
            "数据同步完成",
            "缓存已清理"
        ]
        
        log_msg += random.choice(events)
        
        # 将数据放入队列
        monitor_data = {
            'cpu': cpu,
            'mem': mem,
            'disk': disk,
            'net': net,
            'log': log_msg
        }
        
        monitor_queue.put(monitor_data)
        
        # 模拟数据采集间隔
        time.sleep(1)

# 更新监控界面
def update_monitor():
    if not monitoring_active:
        return
    
    try:
        # 获取监控数据
        while not monitor_queue.empty():
            data = monitor_queue.get_nowait()
            
            # 更新进度条和标签
            cpu_progress['value'] = data['cpu']
            cpu_value.config(text=f"{data['cpu']}%")
            
            mem_progress['value'] = data['mem']
            mem_value.config(text=f"{data['mem']}%")
            
            disk_progress['value'] = data['disk'] * 10  # 转换为0-100
            disk_value.config(text=f"{data['disk']:.1f} MB/s")
            
            net_progress['value'] = data['net'] / 10  # 转换为0-100
            net_value.config(text=f"{data['net']} KB/s")
            
            # 添加日志
            log_text.insert(tk.END, data['log'] + "\n")
            log_text.see(tk.END)  # 滚动到最后
    
    except queue.Empty:
        pass
    
    # 继续更新
    root.after(100, update_monitor)

# 监控状态标志
monitoring_active = False

# 开始监控
def start_monitoring():
    global monitoring_active
    if not monitoring_active:
        monitoring_active = True
        
        # 清空日志
        log_text.delete(1.0, tk.END)
        log_text.insert(tk.END, "[系统] 监控已启动...\n")
        
        # 启动数据生成线程
        monitor_thread = threading.Thread(target=generate_monitor_data)
        monitor_thread.daemon = True
        monitor_thread.start()
        
        # 开始更新界面
        update_monitor()
        
        # 更新按钮状态
        start_monitor_button.config(state=tk.DISABLED)
        stop_monitor_button.config(state=tk.NORMAL)

# 停止监控
def stop_monitoring():
    global monitoring_active
    if monitoring_active:
        monitoring_active = False
        
        # 清空队列
        while not monitor_queue.empty():
            monitor_queue.get()
        
        # 添加日志
        log_text.insert(tk.END, "[系统] 监控已停止\n")
        log_text.see(tk.END)
        
        # 更新按钮状态
        start_monitor_button.config(state=tk.NORMAL)
        stop_monitor_button.config(state=tk.DISABLED)

# 创建控制按钮
start_monitor_button = tk.Button(advanced_control_frame, text="开始监控", command=start_monitoring)
start_monitor_button.pack(side=tk.LEFT, padx=5)

stop_monitor_button = tk.Button(advanced_control_frame, text="停止监控", command=stop_monitoring, state=tk.DISABLED)
stop_monitor_button.pack(side=tk.LEFT, padx=5)

# 清空日志按钮
clear_log_button = tk.Button(
    advanced_control_frame, 
    text="清空日志", 
    command=lambda: log_text.delete(1.0, tk.END)
)
clear_log_button.pack(side=tk.LEFT, padx=5)

# 添加警告说明
tk.Label(
    advanced_frame,
    text="注意：在实际应用中，应该使用专门的库来获取真实的系统监控数据",
    fg="red"
).pack(pady=5)

# 启动主事件循环
root.mainloop()