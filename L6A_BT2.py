import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AtarBals Modern Antivirus")
        self.geometry("800x500")
        self.configure(background="#f0f0f0")  # Background color for the whole window

        # Sidebar
        sidebar = tk.Frame(self, bg="#333333", width=200)
        sidebar.pack(side="left", fill="y")

        buttons_text = ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help"]
        for text in buttons_text:
            button = tk.Button(sidebar, text=text, bg="#333333", fg="white", relief="flat", anchor="w", width=18)
            button.pack(fill="x", pady=5, padx=10)

        scan_now_button = tk.Button(sidebar, text="Scan Now", bg="#4CAF50", fg="white", relief="flat",
                                    font=("Arial", 12, "bold"), width=18)
        scan_now_button.pack(fill="x", pady=20, padx=10)

        # Main area
        main_area = tk.Frame(self, bg="white")
        main_area.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        title_label = tk.Label(main_area, text="Scan", font=("Arial", 24, "bold"), bg="white")
        title_label.pack(pady=10)

        subtitle_label = tk.Label(main_area, text="Premium will be free forever. You just need to click button.",
                                  font=("Arial", 12), bg="white", fg="#333333")
        subtitle_label.pack(pady=10)

        button_texts = ["Quick Scan", "Web Protection", "Quarantine", "Full Scan", "Simple Update"]
        button_frame = tk.Frame(main_area, bg="white")
        button_frame.pack(pady=20)

        for i, text in enumerate(button_texts):
            button = tk.Button(button_frame, text=text, bg="#FF00FF", fg="black", font=("Arial", 12, "bold"), width=18,
                               height=2)
            button.grid(row=i // 2, column=i % 2, padx=10, pady=10)

        status_label = tk.Label(main_area, text="Get Premium to Enable: {Web Protection}, {Full Scan}, {Simple Update}",
                                font=("Arial", 10), fg="#FF00FF", bg="white")
        status_label.pack(pady=10)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
