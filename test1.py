"""ATM系统"""

class ATM:
    """ATM 自动取款机类"""
    
    def __init__(self, initial_balance=5000):
        """初始化ATM账户"""
        self.balance = initial_balance
        self.transaction_history = []
    
    def display_menu(self):
        """显示菜单"""
        print("\n" + "=" * 40)
        print("欢迎使用ATM自动取款机")
        print("=" * 40)
        print("1. 查询余额")
        print("2. 存款")
        print("3. 取款")
        print("4. 交易记录")
        print("5. 退出")
        print("=" * 40)
        choice = input("请选择操作（1-5）：")
        return choice
    
    def check_balance(self):
        """查询余额"""
        print("\n----------查询余额----------")
        print(f"您的账户余额为：{self.balance} 元")
        input("\n按 Enter 键返回菜单...")
    
    def deposit(self):
        """存款"""
        print("\n----------存款----------")
        try:
            amount = float(input("请输入存款金额："))
            if amount <= 0:
                print("❌ 存款金额必须大于0")
                input("\n按 Enter 键返回菜单...")
                return
            self.balance += amount
            self.transaction_history.append(f"存款：+{amount}元")
            print(f"✓ 存款成功！当前余额：{self.balance} 元")
        except ValueError:
            print("❌ 输入错误，请输入有效的金额")
        input("\n按 Enter 键返回菜单...")
    
    def withdraw(self):
        """取款"""
        print("\n----------取款----------")
        try:
            amount = float(input("请输入取款金额："))
            if amount <= 0:
                print("❌ 取款金额必须大于0")
                input("\n按 Enter 键返回菜单...")
                return
            if amount > self.balance:
                print(f"❌ 余额不足！当前余额：{self.balance} 元")
                input("\n按 Enter 键返回菜单...")
                return
            self.balance -= amount
            self.transaction_history.append(f"取款：-{amount}元")
            print(f"✓ 取款成功！当前余额：{self.balance} 元")
        except ValueError:
            print("❌ 输入错误，请输入有效的金额")
        input("\n按 Enter 键返回菜单...")
    
    def show_history(self):
        """显示交易记录"""
        print("\n----------交易记录----------")
        if not self.transaction_history:
            print("暂无交易记录")
        else:
            for i, record in enumerate(self.transaction_history, 1):
                print(f"{i}. {record}")
        input("\n按 Enter 键返回菜单...")
    
    def run(self):
        """运行ATM系统"""
        while True:
            choice = self.display_menu()
            
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.show_history()
            elif choice == "5":
                print("\n感谢使用ATM，再见！")
                break
            else:
                print("❌ 输入有误，请重新选择")

# 主程序
if __name__ == "__main__":
    atm = ATM(initial_balance=5000)
    atm.run()