class HangHoa:
      def __init__(self, MaHang, TenHang, SoLuong, GiaNhap , GiaBan, KhuyenMai, ThanhTien, TienKhuyenMai): 
            self.MaHang = MaHang
            self.TenHang = TenHang
            self.SoLuong = SoLuong
            self.GiaNhap = GiaNhap
            self.GiaBan = GiaBan
            self.KhuyenMai = KhuyenMai
      # Bài 2
      def BanHang(self):
            SoLuongBan = int(input())
            # Tính giá bán
            if self.SoLuong >= 100:
                  self.GiaBan = self.GiaNhap * 1.1
            elif  50 <= self.SoLuong < 100:
                  self.GiaBan = self.GiaNhap * 1.15
            elif  self.SoLuong < 50:
                  self.GiaBan = self.GiaNhap * 1.2
            # Tính theo yêu cầu
            self.ThanhTien = SoLuongBan * self.GiaBan 
            self.TienKhuyenMai = self.ThanhTien * self.KhuyenMai 
            self.SoLuong = self.SoLuong - SoLuongBan

#  Khai báo đối tượng
HangHoa1 = HangHoa('M01',  'Mì tôm Hảo hảo',  100, 3000, int(), 0, int(), int())
HangHoa2 = HangHoa('D01',  'Dầu ăn Tường An (1 lít)', 20 , 40000 , int(), 0, int(), int())

#  chạy xem kết quả
HangHoa1.BanHang()
print(HangHoa1.ThanhTien)
print(HangHoa1.SoLuong)
print(HangHoa1.TienKhuyenMai)

 