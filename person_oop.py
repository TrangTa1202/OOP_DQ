class Nguoi:
        def __init__(self, Ma, Ten, NgaySinh, SDT):
                self.Ma = Ma
                self.Ten = Ten
                self.NgaySinh = NgaySinh
                self.SDT = SDT
        
        def SuaSoDT(self):
                sdtMoi = int(input())
class SinhVien(Nguoi):
        def __init__(self, Ma, Ten, NgaySinh, SDT, DiemTL):
                super().__init__( Ma, Ten, NgaySinh, SDT)
                
                self.DiemTL = DiemTL
        
        def TongDiemTL(self, DiemTLMoi):
                self.DiemTL = self.DiemTL + DiemTLMoi

class GiangVien(Nguoi):
        def __init__(self, Ma, Ten, NgaySinh, SDT, Luong):
                super().__init__( Ma, Ten, NgaySinh, SDT)
                
                self.Luong = Luong
                
        def TangLuong(self, TangLuong):
                self.Luong = self.Luong + TangLuong

SV1 = SinhVien('001', 'Nguyễn Duy Quang', '30-05-2002', '0328679742', 3)
GV1 = GiangVien('001', 'Quang','200000', '0905037138', 5000000)
SV1.TongDiemTL(float(input('Nhập điểm tích lũy mới: ')))
GV1.TangLuong(float(input('Nhập điểm tích lũy mới: ')))

print(SV1.DiemTL)
print(GV1.Luong)


