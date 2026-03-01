import pandas as pd
from datetime import datetime

class DataProcessor:
    def __init__(self, path):
        self.path = path
        self.df = pd.read_excel(path)
        #self.standardize_data()

    def standardize_data(self):
        self.df["Tên khách hàng"] = self.df["Tên khách hàng"].str.upper()

    def list_cus(self):
        return self.df["Tên khách hàng"].values

    def log_time(self, user, name_act):
        now = datetime.now().strftime("Ngày: %d/%m/%Y, time: %H:%M:%S")
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"{now}: {user}: Hành động {name_act}\n")
        return now
    
    def info_cus(self, name_user):
        info = self.df[self.df["Tên khách hàng"] == name_user].iloc[0]
        return info
    
    def service(self, name_user):
        print("\n--- DANH SÁCH DỊCH VỤ ---")
        print("1. Chuyển tiền")
        choice = input("Chọn dịch vụ: ")
        match(choice):
            case 1 | "Chuyển tiền" | '1':
                self.transfer_money(name_user)

    def transfer_money(self, sender):
        while True:
            receiver = input("Nhập người nhận tiền: ")
            if receiver not in self.list_cus():
                print("Không tồn tại người nhận tiền trong danh sách!")
                continue
            if receiver == sender:
                print("Rửa tiền à!")
                continue

            while True:
                try: 
                    amount = float(input("Số tiền muốn chuyển: "))
                    user_info = self.info_cus(sender)
                    if user_info["Số dư"] < amount:
                        print("Số dư không đủ" + f"Số dư còn lại {user_info["Số dư"]}")
                        self.df.to_excel(self.path, index=False)
                    else:
                        # Trừ tiền người gửi
                        self.df.loc[self.df["Tên khách hàng"] == sender, "Số dư"] -= amount
                        # Cộng tiền người nhận
                        self.df.loc[self.df["Tên khách hàng"] == receiver, "Số dư"] += amount
                        # Lưu lại file
                        self.df.to_excel(self.path, index=False)
                        print("Chuyển tiền thành công")
                        break
                except ValueError:
                    print("Vui lòng nhập số tiền hợp lệ!")
            break
        
    def security_shield(self, func):
        def login_status(*args, **kwargs):
            name_user = args[0].upper()
            now = self.log_time(name_user, func.__name__)
            if name_user == "ADMIN":
                print(f"Đăng nhập với quyền ADMIN \n{now}")
            else:
                if name_user in self.list_cus():
                    kwargs["info"] = self.info_cus(name_user)
                    info = kwargs["info"]
                    print(f"Đăng nhập với {name_user} \n{now}\n{info}")
                else:
                    print("Người dùng không tồn tại")
                    return 0
            return func(name_user, **kwargs)
        return login_status

if __name__ == "__main__":
    path = r"User_Data.xlsx"
    processor = DataProcessor(path)

    @processor.security_shield
    def truy_cap(name_user, info = None):
        processor.service(name_user)