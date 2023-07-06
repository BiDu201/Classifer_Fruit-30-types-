import os
from tkinter import *
from tkinter import messagebox, ttk
import Data_Classifer as svm

a = Tk()  # Tạo cửa sổ chính của ứng dụng GUI

a.title("Phân Loại Trái Cây")

a.geometry('600x300') # kích thước cửa sổ


# hàm kiểm tra xem file data1.pickle đã được tạo hay chưa
def check_create_training_data():
    if(not os.path.isfile(svm.location_data(0))): # Nếu thư mục chưa tồn tại file data1.pickle
        try:
            svm.create_training_data()
            messagebox.showinfo('Thông báo', 'Dữ liệu đã được nhập')
        except Exception as e:
            messagebox.showerror('Thông báo', 'Tạo file thất bại!')
    else:
        messagebox.showwarning('Thông báo', 'File đã tồn tại!')

# hàm kiểm tra tách dữ liệu thành train và test
def check_train_tests_plit():
    if(os.path.isfile(svm.location_data(0))): # Nếu file data1.pickle đã được tạo
        try:
            svm.train_tests_plit()
            # show = Label(a, background='yellow', width=20, font=('Time New Roman', 10), text='Tạo dữ liệu thành công')
            # show.place(x=220, y=170)
            messagebox.showinfo('Thông báo', 'Tập dữ liệu train và test đã được tạo')
        except Exception as e:
            messagebox.showerror('Thông báo', 'Tách dữ liệu thất bại!')
    else:
        # error = Label(a, background= 'yellow', width= 20, font=('Time New Roman', 10), text= 'Không có dữ liệu')
        # error.place(x=220, y=170)
        messagebox.showwarning('Thông báo', 'Chưa có dữ liệu ảnh ! Bạn vui lòng nhập dữ liệu')

def SVM():
    if (not os.path.isfile(svm.location_data(1))):
        try:
            svm.SVM()
            messagebox.showinfo('Thông báo', 'Mô hình huấn luyện đã hoàn thành!')
        except Exception as e:
            messagebox.showerror('Thông báo', 'Dữ liệu train chưa được tạo')
    else:
        messagebox.showwarning('Thông báo', 'Mô hình huấn luyện đã tồn tại!')

# Hàm dự đoán và cho biết độ chính xác
def Result():
    if (os.path.isfile(svm.location_data(1))):
        acc = Label(a, background='yellow', width=20, font=('Time New Roman', 10), text=svm.Result(2))  # In độ chính xác
        pred = Label(a, background='yellow', width=20, font=('Time New Roman', 10), text=svm.Result(1)) # prediction[0]: lấy ảnh đầu tiên trả về 1 hoặc 0, categories[0:Cat hoặc 1:Dog]
        acc.place(x=220, y=170)
        pred.place(x=220, y=220)

        svm.Display()
    else:
        messagebox.showerror('Thông báo', 'Dự đoán thất bại')

# Hàm xóa file dữ liệu đã tạo
def delete_file():
    if(os.listdir(svm.folder)): # nếu tồn tại file trong thư mục File
        svm.Delete_Data()
        messagebox.showinfo('Thông báo', 'Mô hình đã được xóa, bây giờ bạn có thể huấn luyện mô hình mới!')
    else:
        messagebox.showwarning('Thông báo', 'Thư mục rỗng!')


# Label tên form
label = Label(a, width= 40, font=('Time New Roman', 20), fg= 'red', text='PHÂN LOẠI TRÁI CÂY', bg='yellow')
label.place(y=1)

# button nhập dữ liệu
btn = Button(a, text = 'Nhập dữ liệu', width= 10, font=('Time New Roman', 10), activebackground='Light Blue', command=check_create_training_data)
btn.place(x = 50, y = 70)

# button tạo dữ liệu train, test
btn1 = Button(a, text = 'Tạo dữ liệu train & test', width= 17, font=('Time New Roman', 10), activebackground='Light Blue', command=check_train_tests_plit)
btn1.place(x = 230, y = 70)

# button huấn luyện
btn2 = Button(a, text = 'Huấn luyện mô hình', width= 17, font=('Time New Roman', 10), activebackground='Light Blue', command=SVM)
btn2.place(x = 230, y = 120)

# button in ra dự đoán và độ chính xác
btn3 = Button(a, text = 'Dự đoán', width= 10, font=('Time New Roman', 10), activebackground='Light Blue', command=Result)
btn3.place(x = 450, y = 70)

# button in ra dự đoán và độ chính xác
btn5 = Button(a, text = 'Trực quan', width= 10, font=('Time New Roman', 10), activebackground='Light Blue', command=svm.visualize)
btn5.place(x = 450, y = 120)

# button Xóa
btn4 = Button(a, text = 'Xóa File', width= 10, font=('Time New Roman', 10), activebackground='Light Blue', command=delete_file)
btn4.place(x = 50, y = 120)

a.mainloop()  # Gọi vòng lặp sự kiện chính để các hành động có thể diễn ra trên màn hình máy tính của người dùng