from student import Student

ds = []

while True:

    print(f'''
    0. Thoát chương trình
    1. Thêm sinh viên
    2. Cập nhật thông tin sinh viên
    3. Xóa sinh viên
    4. Xem thông tin tất cả sinh viên
    5. Tìm sinh viên
    ''')

    select = input("Mời chọn chức năng: ")

    if str(select).isdigit():   
        select = int(select)
        if select == 0:
            break
        elif select == 1:
            id = input("Nhập ID sinh viên: ")
            name = input("Nhập tên sinh viên: ")
            sv = Student(id, name)
            ds.append(sv)

        elif select == 2:
            id = input("Nhập ID sinh viên cần sửa: ")
            for i in ds:
                if i.get_id() == id:
                    i.set_name(input("Nhập vào tên mới: "))
                    i.show_infor()

        elif select == 3:
            id = input("nhập ID sinh viên cần xóa: ")
            for i in ds:
                if i.get_id() == id:
                    ds.remove(i)
                    print("Xóa sinh viên thành công")

        elif select == 4:
            if len(ds) == 0:
                print("\nHiện không có sinh viên. Vui lòng thêm sinh viên mới vào danh sách!")
            else:
                print(f"\nHiện có {len(ds)} sinh viên")
                for i in ds:
                    i.show_infor()

        elif select == 5:
            id = input("Nhập ID sinh viên cần tìm: ")
            for i in ds:
                if i.get_id() == id:
                    i.show_infor() 

    else:
        print("Bạn phải nhập số. Vui long nhập lại!")