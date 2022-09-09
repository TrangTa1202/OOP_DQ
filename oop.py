# Bài 1:
class SinhVien:
      def __init__(self, Masv, TenSv, NgaySinh, Lop, DiemTichLuy): 
            self.Masv = Masv
            self.TenSv = TenSv
            self.NgaySinh = NgaySinh
            self.Lop = Lop
            self.DiemTichLuy = DiemTichLuy
      def inThongTinSV(self):
            print("Thông tin sinh viên {}: ".format(self.TenSv))
            print('Masv: {} TenSv: {} NgaySinh: {} Lop: {} DiemTichLuy: {}'.format(self.Masv, self.TenSv, self.NgaySinh, self.Lop, self.DiemTichLuy))
      def XepLoai(self):
            print('Học lực của sinh viên {} là'.format(self.TenSv))
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
            self.sdt = input('Số điện thoại mới: ')
            print('Cập nhật thành công')

# Bài 2

Sv1 = SinhVien('201112345',  'Nguyễn Tiến Thành',  '12/10/2002', '45K14', 3.4)
Sv2 = SinhVien('201112346',  'Phùng Lê Na', '05/06/2001','45K14', 1.9)
Sv3 = SinhVien('201112347',  'Trần Văn Hùng', '07/11/2002','45K21.1', 2.3)

Sv1.XepLoai()
Sv2.SuaThongTinSV()
Sv1.inThongTinSV()
Sv2.inThongTinSV()
Sv3.inThongTinSV()











