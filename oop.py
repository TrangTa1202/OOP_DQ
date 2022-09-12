# Bài 1:
class SinhVien:
      def __init__(self, Masv, TenSv, NgaySinh,Sdt ,Lop, DiemTichLuy): 
            self.Masv = Masv
            self.TenSv = TenSv
            self.NgaySinh = NgaySinh
            self.Sdt = Sdt
            self.Lop = Lop
            self.DiemTichLuy = DiemTichLuy
      def inThongTinSV(self):
            print("Thông tin sinh viên {}: ".format(self.TenSv))
            print('Masv: {} TenSv: {} NgaySinh: {} SoDienThoai: {} Lop: {} DiemTichLuy: {}'.format(self.Masv, self.TenSv, self.NgaySinh, self.Sdt , self.Lop, self.DiemTichLuy))
      def XepLoai(self):
            if self.DiemTichLuy >= 3.5:
                  print('Xuất sắc')
            elif 3.2<=self.DiemTichLuy < 3.5:
                  print('Giỏi')
            elif 2.5<=self.DiemTichLuy < 3.2:
                  print('Khá')
            elif 2<=self.DiemTichLuy < 2.5:
                  print('Trung bình')
            else:
                  print('Kém')

      def SuaThongTinSV(self):
            self.Sdt = input('Số điện thoại mới: ')
            print('Cập nhật thành công')

# Bài 2

Sv1 = SinhVien('201112345',  'Nguyễn Tiến Thành',  '12/10/2002','' ,'45K14', 3.4)
Sv2 = SinhVien('201112346',  'Phùng Lê Na', '05/06/2001','','45K14' ,1.9)
Sv3 = SinhVien('201112347',  'Trần Văn Hùng', '07/11/2002','','45K21.1', 2.3)

# 1.Sử dụng phương thức XepLoai để kiểm tra xếp loại học lực của sinh viên Nguyễn Tiến Thành
print('\nxếp loại của sinh viên {}'.format(Sv1.TenSv))
Sv1.XepLoai()

# 2. Sử dụng phương thức SuaThongTinSV để đổi số điện thoại của Phùng Lê Na thành 091234567
print( '\nCập nhật số điện thoại của sinh viên Phùng Lê Na')
Sv2.SuaThongTinSV()

#  3. In thông tin của 3 sinh viên ra màn hình
print('\nIn thông tin 3 sinh viên')
Sv1.inThongTinSV()
Sv2.inThongTinSV()
Sv3.inThongTinSV()











