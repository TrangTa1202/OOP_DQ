# Bài 1:
class HangHoa:
      def __init__(self, MaHang, TenHang, SoLuong, GiaNhap , GiaBan, KhuyenMai): 
            self.MaHang = MaHang
            self.TenHang = TenHang
            self.SoLuong = SoLuong
            self.GiaNhap = GiaNhap
            self.GiaBan = GiaBan
            self.KhuyenMai = KhuyenMai
      # Bài 2
      def TinhGiaBan(self):
            if self.SoLuong >= 100:
                  self.GiaBan = self.GiaNhap * 1.1
            elif  50 <= self.SoLuong < 100:
                  self.GiaBan = self.GiaNhap * 1.15
            else:
                  self.GiaBan = self.GiaNhap * 1.2


HH1 = HangHoa('M01',  'Mì tôm Hảo hảo',  100, 3000, int(), 0)
HH2 = HangHoa('D01',  'Dầu ăn Tường An (1 lít)', 20 , 40000 , int(), 0)

HH1.TinhGiaBan()

print('Giá bán {} '.format(HH1.GiaBan)) 
 