import time
import datetime
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    current_time = datetime.datetime.now().strftime("%H:%M")
    Stop_time = input("Zamanı giriniz örnek:- [10:10]:- ")
    a = current_time.replace(":", ".")
    a = float(a)
    b = Stop_time.replace(":", ".")
    b = float(b)
    Focus_Time = b - a
    Focus_Time = round(Focus_Time, 3)
    host_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
    redirect = '127.0.0.1'
    print(current_time)
    time.sleep(2)
    website_list = ["www.facebook.com", "facebook.com"]  # Engellemek istediğiniz web sitelerini girin
    if current_time < Stop_time:
        with open(host_path, "r+") as file:  # r+ yazma+okuma
            content = file.read()
            time.sleep(2)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(f"{redirect} {website}\n")
            print("TAMAMLANDI")
            time.sleep(1)
            print("ODAK MODU AÇILDI !!!!")
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            website_list = ["www.facebook.com", "facebook.com"]  # Engellemek istediğiniz web sitelerini girin
            if current_time >= Stop_time:
                with open(host_path, "r+") as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in website_list):
                            file.write(line)
                    file.truncate()
                print("Web sitelerinin engeli kaldırıldı !!")
                file = open("focus.txt", "a")
                file.write(f",{Focus_Time}")  # Başlamadan önce focus.txt dosyasına 0 yaz
                file.close()
                break
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    is_admin()
