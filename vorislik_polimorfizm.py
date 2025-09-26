class Shaxs:
    def init(self,ism,familiya,pasport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.pasport=pasport
        self.tyil=tyil
    def get_info(self):
        info=f"Ismi:{self.ism}\nFamiliyasi: {self.familiya}\n"
        info+=f"Pasporti: {self.pasport}\nYili: {self.tyil}"
        return info
    def get_age(self,yil):
        return yil-self.tyil
class Talaba(Shaxs):
    def init(self,ism,familiya,pasport,tyil,idraqam):
        super().init(ism,familiya,pasport,tyil)
        self.idraqam=idraqam
        self.bosqich=1

    def id_raqam(self):
        return self.idraqam

    def bosqich1(self):
        return self.bosqich

talaba=Talaba("Valijon","Aliyev","Ad5241136",2004,"072153")
print(talaba.get_age(2025))
print(talaba.get_info())
print(talaba.id_raqam())
print(talaba.bosqich1())


class Shaxs:
    def init(self,ism,familiya,pasport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.pasport=pasport
        self.tyil=tyil
    def get_info(self):
        info=f"Ismi:{self.ism}\nFamiliyasi: {self.familiya}\n"
        info+=f"Pasporti: {self.pasport}\nYili: {self.tyil}"
        return info
    def get_age(self,yil):
        return yil-self.tyil





class Manzil:
    def init(self,Hudud,mahalla,uy):
        self.hudud=Hudud
        self.mahalla=mahalla
        self.uy=uy
    def manzil_r(self):
        return f"Hudud: {self.hudud}\nMahalla: {self.mahalla}\nUy: {self.uy}"
manzil1=Manzil("xorazm","Ashxabod","Tafakkur 29")




class Talaba(Shaxs):
    def init(self,ism,familiya,pasport,tyil,idraqam,manzil):
        super().init(ism,familiya,pasport,tyil)
        self.idraqam=idraqam
        self.bosqich=1
        self.manzil=manzil

    def id_raqam(self):
        return self.idraqam

    def bosqich1(self):
        return self.bosqich




talaba=Talaba("Valijon","Aliyev","Ad5241136",2004,"072153",manzil1)
print(talaba.manzil.manzil_r())
print(talaba.get_age(2025))
print(talaba.get_info())
print(talaba.id_raqam())
print(talaba.bosqich1())