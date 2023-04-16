import socket as s
import os

# Bana soru sormak için veya daha fazla türkce kaynak için instagram ve GitHub da takip edebilirsin.
# github.com/canemingozde
# instagram.com/canemingozde


class Server:
    host = "127.0.0.1"
    port = 63541
    server = s.socket(s.AF_INET,s.SOCK_STREAM)
    def __init__(self):
        self.server.bind(( self.host, self.port))
        self.server.listen(1)
        self.client, self.client_adrs =  self.server.accept()
        print(f"******* Bağlanan bilgisayar ip ve port numarası: { self.client_adrs} *******")
        print("__________________________________________________________________________________\n")


    def msj_set(self,msj):
        msj = str(msj)
        self.client.send(msj.encode())


    def msj_get(self):
        gelen_mesaj =  self.client.recv(1024).decode()
        return gelen_mesaj


    def dosya_set(self,dosya):
        self.client.send(dosya)


    def dosya_get(self):
        gelen_dosya = self.client.recv(1024)
        return gelen_dosya



    def dosya(self):
        print("*** UYARI !!! Dosya almak için dosya ismini uzantısı ile giriniz | Dizin gezmek için dizin yazınız. ***")
        # örnek : resim.png 
        print()
        istem2 = input("Hangi işlemi yapmak istiyorsun: ")
        if istem2 == "dizin":
            self.msj_set(istem2)
            self.dizin()
        else:
            self.msj_set(istem2)
            while True:
                gelen_dosya = self.dosya_get()
                with open(istem2,"wb") as file:
                    while gelen_dosya:
                        file.write(gelen_dosya)
                        gelen_dosya = self.dosya_get()
                break
            print("********** Dosya alındı. **********")    

                
                

    def dizin(self):
        print("** Kapatmak için close | Dizin gezmek için dizin yolunu giriniz | Dosya almak için dosya yazınız !!! **")
        print()
        while True:    
            istem = input("Hangi işlemi yapmak istiyorsunuz: ")
            print()
            if istem == "close":
                self.msj_set(istem) 
                break
            elif istem == "dosya":
                self.msj_set(istem)
                self.dosya()
            elif os.path.isdir(istem):
                print()
                self.msj_set(istem)            
                gelen_icerik = self.msj_get()
                print(gelen_icerik)
            else:
                print("Yanlış istem tekrar deneyiniz !!!")    
                print()            

       
       
        
    
if __name__ == "__main__":
    a = Server()
    a.dizin()
       



    




    





