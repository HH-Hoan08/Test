from processor import DataProcessor
from admin_processor import AdminProcessor

def main():
    path = "User_Data.xlsx"
    print("---LOGIN---") 
    try:
        while True:
            name_user = input("Nhập tên người dùng: ").strip().upper()
            if name_user == "ADMIN":
                while True:
                    passwd = input("Nhập mật khẩu: ")
                    admin_console = AdminProcessor(path, passwd)
                    if admin_console.is_ADMIN() != True:
                        print("Sai pass")
                        continue
                    else:
                        @admin_console.security_shield
                        def truy_cap_admin(name_user, **kwargs):
                            admin_console.service(name_user)
                        truy_cap_admin(name_user, info = None)
                    break
            else:
                user_console = DataProcessor(path)
                if name_user not in user_console.list_cus():
                    continue
                @user_console.security_shield
                def truy_cap(name_user, info):
                    user_console.service(name_user)
                truy_cap(name_user, info=None)
            break
    except ValueError as e:
            print(e)
main()  