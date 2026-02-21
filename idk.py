import pandas as pd

#Danh sách khách hàng
def Thongtinluutru():
    path = r"C:\Users\Lenovo\OneDrive\Documents\Database.xlsx"
    ds = pd.read_excel(path, skiprows= 1)
    return ds

def smart_log(func):
    def Security(*args, **kwargs):
        user = args[0]
        print(f"Đang thực thi lệnh: {func.__name__} với dữ liệu: {user}")
        db = Thongtinluutru()
        if user in db['Tên khách hàng'].values:
            if "Admin" == user:
                print(f"Chào mừng trở lại {user}")
            else:
                print(f"Chào mừng trở lại {user}")
                user_data = db[db["Tên khách hàng"] == user].iloc[0]
                kwargs['info'] = user_data
                func(*args, **kwargs)
        else:
            print("Không có thông tin người dùng")
    return Security

#Truy vấn số dư của khách hàng từ danh sách khách hàng
@smart_log
def truy_van_so_du(user, info = None):
    print(f"Số dư của {user} là {info['Số dư']}$")
    return truy_van_so_du

truy_van_so_du("Hoàng")

#Tính năng chuyển tiền
@smart_log
def chuyen_tien(nguoigui, nguoinhan, sotien):
    print(f"Đã chuyển {sotien}$ từ {nguoigui} sang {nguoinhan}")
    return chuyen_tien

