import os
import random
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle  # chuyển đổi các cấu trúc đối tượng Python sang một dạng byte
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from math import sqrt
import sklearn.metrics as metric
from sklearn.metrics import accuracy_score

folder = ".\\File" # đường dẫn folder lưu trữ file dữ liệu

data = ['data1.pickle', 'model.sav'] # tên file lưu trữ data

dir = '.\\FruitImages'

# categories = ['Sơ-ri', 'Táo', 'Mơ Châu Âu', 'Bơ', 'Chuối', 'Mâm xôi đen', 'Việt quất xanh', 'Dưa vàng', 'Cherry', 'Dừa', 'Sung Mỹ', 'Nho', 'Bưởi chùm', 'Ổi', 'Kiwi', 'Chanh vàng', 'Chanh xanh', 'Xoài', 'Ô liu', 'Cam', 'Chanh dây', 'Đào', 'Lê', 'Dứa', 'Mận', 'Lựu', 'Mâm xôi ỏ', 'Dâu', 'Cà chua', 'Dưa hấu']
categories = ['Acerola', 'Apple', 'Apricot', 'Avocado', 'Banana', 'BlackBerry', 'Blueberry', 'Cantaloupe', 'Cherry', 'Coconut', 'Fig', 'Grape', 'Grapefruit', 'Guava', 'Kiwifruit', 'Lemon', 'Lime', 'Mango', 'Olive', 'Orange', 'Passionfruit', 'Peache', 'Pear', 'Pineapple', 'Plum', 'Pomegranate', 'Raspberry', 'Strawberry', 'Tomato', 'Watermelon']

# Hàm đường dẫn đến file
def location_data(stt):
    path = os.path.join(folder, data[stt])
    return path

# Hàm tạo dữ liệu training
def create_training_data():
    data = []

    for category in categories:
        path = os.path.join(dir, category)  # nối ừng category vào đường dẫn dir (hay đường dẫn đến thư mục chứa ảnh của từng loa trái cây
        label = categories.index(category)  # nhãn của mỗi loại trái cây (30 loại tương ứng 30 nhãn từ 0->29)
        for img in os.listdir(path):  # duyệt qua tất cả ảnh trong thư mục từ đường dẫn path
            imgpath = os.path.join(path, img)  # nối ảnh vào từng thư mục tương ứng
            fruit_img = cv2.imread(imgpath, 0)  # đọc ảnh xám
            try:
                fruit_img = cv2.resize(fruit_img, (50, 50))
                image = np.array(fruit_img).flatten()

                data.append([image, label])
            except Exception as e:
                pass  # bỏ qua

    pick_in = open('.\\File\\data1.pickle', 'wb')  # mở tệp để ghi
    pickle.dump(data, pick_in)  # lưu data vào pick_in
    pick_in.close()

# Đọc file data1.pickle
def data1_file():
    pick_in = open('.\\File\\data1.pickle', 'rb')  # đọc tệp
    data = pickle.load(pick_in)
    pick_in.close()
    return data


# Trực quan hóa số lượng ảnh
def visualize():
    num_images = []
    for lab in categories:
        files = os.listdir(os.path.join(dir, lab))
        c = len(files)
        num_images.append(c)

    y_pos = np.arange(len(categories))
    plt.barh(y_pos, num_images, align='center')
    plt.yticks(y_pos, categories)
    plt.show()


# hàm tạo dữ liệu test và train
def train_tests_plit():
    random.shuffle(data1_file())
    features = []
    labels = []

    for feature, label in data1_file():
        features.append(feature)
        labels.append(label)

    global X_train, X_test, y_train, y_test

    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.1)  # tách dữ liệu thành test và train 1% test

# Hàm thuật toán phân lớp SVM
def SVM():
    # C: biểu thị mức độ phạt trong lề mềm (soft margin)
    # kernel giúp biến đổi dữ liệu sang chiều (dimension) cao hơn.
    model = SVC(C=1, kernel='poly', gamma=1)  # gamma = 'auto': sử dụng 1/n_features
    model = model.fit(X_train, y_train)  # fit: Điều chỉnh mô hình SVM theo dữ liệu huấn luyện.

    # lưu lại mô hình sau khi huấn luyện
    pick = open('.\\File\\model.sav', 'wb')
    pickle.dump(model, pick)
    pick.close()

# Hàm dự đoán và cho biết độ chính xác
def Result(x):
    train_tests_plit()

    pick = open('.\\File\\model.sav', 'rb')
    model = pickle.load(pick)
    pick.close()

    if (x == 1):
        prediction = model.predict(X_test)  # Thực hiện phân loại trên các mẫu trong X.

        print(metric.classification_report(y_test, prediction))
        # print("rmse", sqrt(metric.mean_squared_error(y_test, prediction)))  # RMSE là độ lệch chuẩn của các phần dư (sai số dự đoán).

        acc_test = accuracy_score(prediction, y_test)
        print('-------------------------------------------------------------')
        print('accuracy_test: ', round(acc_test * 100, 2), '%')
        return categories[prediction[0]]
    else:
        accuracy = model.score(X_test, y_test)  # trả về độ chính xác của thuật toán
        return accuracy

# Hiện thị ảnh ra màn hình
def Display():
    mypet = X_test[0].reshape(50, 50)
    plt.imshow(mypet, cmap='gray')
    plt.show()

# Hàm xóa file mô hình đã tạo
def Delete_Data():
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        os.remove(path)