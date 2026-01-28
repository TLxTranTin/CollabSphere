from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
class BaiKiemTra:
    def __init__(self, id: str, ten: str, mo_ta: str , mon_hoc : MonHoc):
        self.id = id
        self.ten = ten
        self.mo_ta = mo_ta
        self.mon_hoc = mon_hoc
