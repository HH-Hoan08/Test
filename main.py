from processor import DataProcessor
path = r"User_Data.xlsx"
processor = DataProcessor(path)

@processor.security_shield
def truy_cap(name_user, info = None):
    processor.service(name_user)

print("Đăng nhập")
name = input("Nhập tên: ")
truy_cap(name)