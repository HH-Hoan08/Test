from processor import DataProcessor

class AdminProcessor(DataProcessor):
    def __init__(self, path, passwd):
        super().__init__(path)
        self.passwd = passwd
    
    def is_ADMIN(self):
        return self.passwd == "Yeuvo"
        
    def delete_user(self, name_user):
        name = input("Nhập tên người muốn xóa nợ: ").upper()
        self.df = self.df[self.df["Tên khách hàng"] != name]
        self.df.to_excel(self.path, index = False)
        
    def add_funds(self, name_user):
        while True:
            name = input("Nhập tên: ").upper()
            if name not in DataProcessor.list_cus(self):
               continue
            info = DataProcessor.info_cus(self, name)
            print(f"Thông tin {info}")
            amount = float(input("Nhập số tiền: "))
            self.df.loc[self.df["Tên khách hàng"] == name, "Số dư"] += amount
            self.df.to_excel("User_data.xlsx", index = False)
            info = self.df[self.df["Tên khách hàng"] == name]
            print(info)
            
    def get_service(self):
        services = super().get_service()
        services["2"] = ("Xóa người dùng", self.delete_user)
        services["3"] = ("Thêm tiền", self.add_funds)
        return services

    def service(self, name_user):
        super().service(name_user)