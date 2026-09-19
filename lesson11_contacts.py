# 第2周毕业项目：通讯录
FILE_NAME = "contacts.txt"

# === 加载和保存（数据层）===
def load_contacts():
    """从文件加载通讯录，没文件就返回空字典"""
    contacts = {}
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "=" in line:
                    name, phone = line.split("=", 1)
                    contacts[name] = phone
    except FileNotFoundError:
        pass   # 文件不存在也没事，给个空的
    return contacts

def save_contacts(contacts):
    """把字典存到文件"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for name, phone in contacts.items():
            f.write(f"{name}={phone}\n")

# === 5 个功能（功能层）===
def show_all(contacts):
    """看全部"""
    if not contacts:
        print("通讯录是空的，先去添加几个吧")
        return
    print("--- 你的通讯录 ---")
    for i, (name, phone) in enumerate(contacts.items(), 1):
        print(f"  {i}. {name} : {phone}")

def add_contact(contacts):
    """添加联系人"""
    name = input("姓名：")
    if name in contacts:
        print(f"{name} 已存在，电话是 {contacts[name]}")
        if input("要更新吗？(y/n)：").lower() == "y":
            contacts[name] = input("新电话：")
            save_contacts(contacts)
            print("已更新")
        return
    phone = input("电话：")
    contacts[name] = phone
    save_contacts(contacts)
    print(f"已添加：{name}")

def search_contact(contacts):
    """查找"""
    name = input("要查的姓名：")
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print(f"没找到 {name}")

def delete_contact(contacts):
    """删除"""
    name = input("要删的姓名：")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"已删除 {name}")
    else:
        print(f"通讯录里没有 {name}")

# === 主程序 ===
def main():
    contacts = load_contacts()
    print(f"=== 通讯录（已加载 {len(contacts)} 个）===")

    while True:
        print("\n1.看全部  2.添加  3.查找  4.删除  5.退出")
        choice = input("请选择：")

        if choice == "1":
            show_all(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("再见！下次启动数据还在")
            break
        else:
            print("请输入 1-5")

main()
