import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("FPS Control Window")
        self.geometry("600x300")
        self.configure(bg="lightblue")  # Tùy chỉnh màu nền

        # Tạo nhãn tiêu đề
        title_label = tk.Label(self, text="FPS Control Panel", font=("Helvetica", 24), bg="lightblue")
        title_label.pack(pady=20)

        # Tạo khung cho đầu vào FPS
        fps_frame = tk.Frame(self, bg="lightblue")
        fps_frame.pack(pady=10)

        fps_label = tk.Label(fps_frame, text="FPS:", font=("Helvetica", 14), bg="lightblue")
        fps_label.pack(side=tk.LEFT, padx=5)

        self.fps_entry = tk.Entry(fps_frame, font=("Helvetica", 14))
        self.fps_entry.pack(side=tk.LEFT, padx=5)

        # Tạo khung cho các nút
        button_frame = tk.Frame(self, bg="lightblue")
        button_frame.pack(pady=10)

        pause_button = tk.Button(button_frame, text="Tạm dừng", font=("Helvetica", 14), command=self.pause)
        pause_button.pack(side=tk.LEFT, padx=5)

        start_button = tk.Button(button_frame, text="Bắt đầu", font=("Helvetica", 14), command=self.start)
        start_button.pack(side=tk.LEFT, padx=5)

        stop_button = tk.Button(button_frame, text="Kết thúc", font=("Helvetica", 14), command=self.stop)
        stop_button.pack(side=tk.LEFT, padx=5)

        # Tạo nhãn trạng thái
        self.status_label = tk.Label(self, text="Trạng thái: Chưa bắt đầu", font=("Helvetica", 14), bg="lightblue")
        self.status_label.pack(pady=10)

    def pause(self):
        self.status_label.config(text="Trạng thái: Tạm dừng")

    def start(self):
        self.status_label.config(text="Trạng thái: Đang ghi")

    def stop(self):
        self.status_label.config(text="Trạng thái: Kết thúc")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
