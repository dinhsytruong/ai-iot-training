import tkinter as tk
import math


# 1. TẠO CỬA SỔ GIAO DIỆN

window = tk.Tk()
window.title("Máy Tính Khoa Học")
window.configure(bg="#222222") # Màu nền tối (Dark mode)
window.resizable(False, False) # Không cho kéo dãn cửa sổ

# Đây là một biến "toàn cục" (global variable) dùng để lưu phép tính.
# Ví dụ: "3+5*2"
bieu_thuc = ""

# 2. TẠO MÀN HÌNH HIỂN THỊ

# Dùng tk.Entry (ô nhập chữ) làm màn hình. 
# justify="right" nghĩa là chữ canh lề phải giống máy tính thật.
man_hinh = tk.Entry(window, font=('Arial', 24, 'bold'), bg="#dddddd", fg="black", justify="right")
# grid: Đặt màn hình ở hàng 0, cột 0, chiếm 5 cột.
man_hinh.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=20, pady=10)



# 3. CÁC HÀM XỬ LÝ TOÁN HỌC ĐƠN GIẢN

def nhap_ky_tu(ky_tu):
    """Được gọi khi bấm các số (0-9) hoặc dấu (+, -, *, /)."""
    global bieu_thuc
    bieu_thuc = bieu_thuc + str(ky_tu) # Nối thêm chữ/số vào biểu thức
    
    # Xóa màn hình cũ và in biểu thức mới lên
    man_hinh.delete(0, tk.END)
    man_hinh.insert(tk.END, bieu_thuc)

def xoa_tat_ca():
    """Nút AC - Xóa sạch tất cả."""
    global bieu_thuc
    bieu_thuc = ""
    man_hinh.delete(0, tk.END)

def xoa_mot_ky_tu():
    """Nút DEL - Xóa chữ số cuối cùng."""
    global bieu_thuc
    bieu_thuc = bieu_thuc[:-1] # Cắt bỏ ký tự cuối cùng của chuỗi
    man_hinh.delete(0, tk.END)
    man_hinh.insert(tk.END, bieu_thuc)

def tinh_ket_qua():
    """Nút = (Bằng). Tính toán và in kết quả."""
    global bieu_thuc
    try:
        # Máy tính hiểu dấu ** là lũy thừa, chứ không hiểu ký hiệu ^ hay xʸ
        bieu_thuc_python = bieu_thuc.replace('^', '**')
        # Thay thế ký hiệu π và e bằng số thập phân thật để tính
        bieu_thuc_python = bieu_thuc_python.replace('π', str(math.pi))
        bieu_thuc_python = bieu_thuc_python.replace('e', str(math.e))
        
        # eval() là hàm tự động tính chuỗi phép tính.
        # Ví dụ: eval("3+5") sẽ ra 8.
        ket_qua = str(eval(bieu_thuc_python))
        
        man_hinh.delete(0, tk.END)
        man_hinh.insert(tk.END, ket_qua)
        bieu_thuc = ket_qua # Lưu kết quả để có thể cộng trừ tiếp
    except:
        man_hinh.delete(0, tk.END)
        man_hinh.insert(tk.END, "Lỗi cú pháp!")
        bieu_thuc = ""

def tinh_ham_khoa_hoc(ten_ham):
    """Xử lý sin, cos, tan, log, ln, căn bậc 2."""
    global bieu_thuc
    try:
        so = float(bieu_thuc) # Lấy số đang có trên màn hình chuyển thành số thập phân
        
        # Dùng thư viện math để tính
        if ten_ham == "sin":    ket_qua = math.sin(math.radians(so))
        elif ten_ham == "cos":  ket_qua = math.cos(math.radians(so))
        elif ten_ham == "tan":  ket_qua = math.tan(math.radians(so))
        elif ten_ham == "log":  ket_qua = math.log10(so)
        elif ten_ham == "ln":   ket_qua = math.log(so)
        elif ten_ham == "sqrt": ket_qua = math.sqrt(so)
        elif ten_ham == "x2":   ket_qua = so * so
        elif ten_ham == "%":    ket_qua = so / 100
        
        ket_qua = str(round(ket_qua, 8)) 
        
        man_hinh.delete(0, tk.END)
        man_hinh.insert(tk.END, ket_qua)
        bieu_thuc = ket_qua
    except:
        man_hinh.delete(0, tk.END)
        man_hinh.insert(tk.END, "Lỗi!")
        bieu_thuc = ""


# 4. TẠO CÁC NÚT BẤM BẰNG VÒNG LẶP CHO NGẮN
# Lên danh sách các nút theo từng hàng
danh_sach_nut = [
    ['sin', 'cos', 'tan', 'log'],
    ['ln', 'π', 'e', '%'],
    ['x²', '√x', 'DEL', 'AC'],
    ['(', ')', '^', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '00', '.', '=']
]

hang_hien_tai = 1

for hang in danh_sach_nut:
    cot_hien_tai = 0
    for chu_tren_nut in hang:
        
        # --- Đặt màu sắc ---
        mau_nen = "#4a4a4a" # Màu xám đen (Mặc định cho số và dấu chấm)
        mau_chu = "white"
        
        if chu_tren_nut in ['AC', 'DEL']:
            mau_nen = "#e74c3c" # Màu đỏ
        elif chu_tren_nut == '=':
            mau_nen = "#27ae60" # Màu xanh lá
        elif chu_tren_nut in ['+', '-', '*', '/', '^']:
            mau_nen = "#e67e22" # Màu cam
        elif chu_tren_nut in ['sin', 'cos', 'tan', 'log', 'ln', 'π', 'e', '√x', '%', 'x²', '(', ')']:
            mau_nen = "#2980b9" # Màu xanh dương

        # --- Tạo nút ---
        # width được nới rộng một chút cho phù hợp với 4 cột
        nut = tk.Button(window, text=chu_tren_nut, font=('Arial', 14, 'bold'),
                        bg=mau_nen, fg=mau_chu, width=6, height=2)
        
        # --- Gắn chức năng cho nút ---
        # Ghi chú: "lambda" chỉ là một hàm ngắn không tên, dùng để "gói" tham số truyền vào hàm khác.
        if chu_tren_nut == '=':
            nut.config(command=tinh_ket_qua)
        elif chu_tren_nut == 'AC':
            nut.config(command=xoa_tat_ca)
        elif chu_tren_nut == 'DEL':
            nut.config(command=xoa_mot_ky_tu)
        elif chu_tren_nut == '√x':
            nut.config(command=lambda: tinh_ham_khoa_hoc('sqrt'))
        elif chu_tren_nut == 'x²':
            nut.config(command=lambda: tinh_ham_khoa_hoc('x2'))
        elif chu_tren_nut == '%':
            nut.config(command=lambda: tinh_ham_khoa_hoc('%'))
        elif chu_tren_nut in ['sin', 'cos', 'tan', 'log', 'ln']:
            nut.config(command=lambda ham=chu_tren_nut: tinh_ham_khoa_hoc(ham))
        else:
            # Dành cho số và phép tính cơ bản
            nut.config(command=lambda ky_tu=chu_tren_nut: nhap_ky_tu(ky_tu))

        # Đặt nút vào dạng lưới (grid)
        nut.grid(row=hang_hien_tai, column=cot_hien_tai, padx=2, pady=2)
        
        cot_hien_tai += 1
    
    hang_hien_tai += 1



# 5. CHẠY CHƯƠNG TRÌNH

window.mainloop() # Bật vòng lặp để giữ cửa sổ luôn mở
