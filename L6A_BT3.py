import tkinter as tk
from tkinter import ttk


def submit_data():
    print("Data Submitted!")


def create_data_entry_form():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Data Entry Form")
    root.geometry("500x400")

    # Khung thông tin người dùng
    user_info_frame = ttk.LabelFrame(root, text="User Information")
    user_info_frame.pack(fill="x", padx=20, pady=10)

    # Các trường nhập tên, họ, chức danh, tuổi và quốc tịch
    ttk.Label(user_info_frame, text="First Name").grid(row=0, column=0, padx=5, pady=5)
    ttk.Entry(user_info_frame).grid(row=1, column=0, padx=5, pady=5)

    ttk.Label(user_info_frame, text="Last Name").grid(row=0, column=1, padx=5, pady=5)
    ttk.Entry(user_info_frame).grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(user_info_frame, text="Title").grid(row=0, column=2, padx=5, pady=5)
    ttk.Combobox(user_info_frame, values=["Mr", "Mrs", "Ms"]).grid(row=1, column=2, padx=5, pady=5)

    ttk.Label(user_info_frame, text="Age").grid(row=2, column=0, padx=5, pady=5)
    ttk.Spinbox(user_info_frame, from_=0, to=100).grid(row=3, column=0, padx=5, pady=5)

    ttk.Label(user_info_frame, text="Nationality").grid(row=2, column=1, padx=5, pady=5)
    ttk.Entry(user_info_frame).grid(row=3, column=1, padx=5, pady=5)

    # Khung đăng ký
    registration_frame = ttk.LabelFrame(root, text="Registration Status")
    registration_frame.pack(fill="x", padx=20, pady=10)

    ttk.Checkbutton(registration_frame, text="Currently Registered").grid(row=0, column=0, padx=5, pady=5)

    ttk.Label(registration_frame, text="# Completed Courses").grid(row=0, column=1, padx=5, pady=5)
    ttk.Spinbox(registration_frame, from_=0, to=50).grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(registration_frame, text="# Semesters").grid(row=0, column=2, padx=5, pady=5)
    ttk.Spinbox(registration_frame, from_=0, to=12).grid(row=1, column=2, padx=5, pady=5)

    # Khung Điều khoản và Điều kiện
    terms_frame = ttk.LabelFrame(root, text="Terms & Conditions")
    terms_frame.pack(fill="x", padx=20, pady=10)

    ttk.Checkbutton(terms_frame, text="I accept the terms and conditions.").pack(padx=5, pady=5)

    # Nút Gửi
    submit_button = ttk.Button(root, text="Enter data", command=submit_data)
    submit_button.pack(pady=20)

    root.mainloop()


create_data_entry_form()