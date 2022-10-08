class Nguoi:
        def __init__(self, Ma, Ten, NgaySinh, SDT):
                self.__Ma = Ma
                self.__Ten = Ten
                self.__NgaySinh = NgaySinh
                self._SDT = SDT
        
        def SuaSoDT(self, sdtMoi):
                self._SDT = sdtMoi
                print('Số điện thoại mới là: {}'.format(self._SDT))

class SinhVien(Nguoi):
        def __init__(self, Ma, Ten, NgaySinh, SDT, DiemTL):
                super().__init__( Ma, Ten, NgaySinh, SDT)
                
                self.DiemTL = DiemTL
        
        def TongDiemTL(self, DiemTLMoi):
                self.DiemTL = self.DiemTL + DiemTLMoi
                print('Điểm tích lũy mới là: {}'.format(self.DiemTL))

class GiangVien(Nguoi):
        def __init__(self, Ma, Ten, NgaySinh, SDT, Luong):
                super().__init__( Ma, Ten, NgaySinh, SDT)
                
                self.Luong = Luong
                
        def TangLuong(self, TangLuong):
                self.Luong = self.Luong + TangLuong
                print('Lương mới là: {}'.format(self.Luong))

# Nguoi1 = Nguoi('001', 'Nguyễn Duy Tan', '30-05-1997', '0346679333')
SV1 = SinhVien('001', 'Nguyễn Duy Quang', '30-05-2002', '0328679742', 3)
GV1 = GiangVien('001', 'Nguyen Duy Hung','20-06-1995', '0905037138', 5000000)


# Nguoi1.SuaSoDT(input('\nNhập số điện thoại mới: '))
SV1.TongDiemTL(float(input('\nNhập điểm được tăng: ')))
GV1.TangLuong(float(input('\nNhập lương được tăng: ')))







