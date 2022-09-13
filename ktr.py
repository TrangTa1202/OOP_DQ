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
      def NhapThemHang(self):
            MaHang = input()
            SoLuongNhapThem = int(input())
            GiaNhapMoi = int(input())
            self.SoLuong = self.SoLuong + SoLuongNhapThem
            self.GiaNhap = GiaNhapMoi
            self.GiaBan = self.GiaNhap + self.GiaNhap * (20 / 100)

# Bài 3

HH1 = HangHoa('M01',  'Mì tôm Hảo hảo',  100, 3000, int(), 0)
HH2 = HangHoa('D01',  'Dầu ăn Tường An (1 lít)', 100 , 3000 , int(), 0)

#  Bài 4
HH1.NhapThemHang()
print( 'Số lượng mới {}'.format( HH1.SoLuong))
print('Giá nhập mới {}'.format(HH1.GiaNhap))
print('Giá bán {} '.format(HH1.GiaBan))
 