from tkinter import *



root = Tk()
root.title('Book Recorder')
root.geometry('925x500+300+200')
root.configure(bg="black")
root.resizable(False, False)


img = PhotoImage(file='D:\codes/okuduğunuz kitap/kitap.png') 
Label(root, image=img, bg='black').place(x=550, y=50)

def kitap_kaydet():
    try:
        with open("kitaplar.txt", "a") as dosya:
            kitap_adi = kitap_adi_giris.get()
            dosya.write(kitap_adi + "\n")
        print("Kitap başarıyla kaydedildi.")
    except Exception as e:
        print("Hata oluştu:", str(e))

def kitap_listele():
    try:
        with open("kitaplar.txt", "r") as dosya:
            kitaplar = dosya.readlines()
            if not kitaplar:
                print("Henüz kaydedilmiş kitap yok.")
            else:
                listbox.delete(0, END)  # Clear existing listbox items
                for kitap in kitaplar:
                    listbox.insert(END, kitap.strip())
    except Exception as e:
        print("Hata oluştu:", str(e))

def kitap_listesini_temizle():
    try:
        with open("kitaplar.txt", "w") as dosya:
            dosya.write("")
        print("Kitap listesi başarıyla temizlendi.")
        listbox.delete(0, END)
    except Exception as e:
        print("Hata oluştu:", str(e))

def main():
    


    global kitap_adi_giris
    kitap_adi_giris = Entry(root, width=30, bg='white', fg='black', font=('Arial', 12))
    kitap_adi_giris.place(x=550, y=350)

    Button(root, width=39, pady=7, text='Kitap Kaydet', bg='black', fg='white', border=0, command=kitap_kaydet).place(x=550, y=380)
    Button(root, width=39, pady=7, text='Kaydedilen kitapları listele', bg='black', fg='white', border=0, command=kitap_listele).place(x=550, y=410)
    Button(root, width=39, pady=7, text='Çıkış', bg='black', fg='white', border=0, command=root.quit).place(x=550, y=440)
    Button(root, width=39, pady=7, text='Kitap listesini temizle', bg='black', fg='white', border=0, command=kitap_listesini_temizle).place(x=5, y=340)
    Label(root, width=39, pady=7, text='KİTAP LİSTESİ', bg='black', fg='white', border=0).place(x=95, y=20)


    global listbox
    listbox = Listbox(root, bg='white', fg='black', font=('Arial', 12), width=40, height=15)
    listbox.place(x=50, y=50)



if __name__ == "__main__":
    main()
    root.mainloop()
