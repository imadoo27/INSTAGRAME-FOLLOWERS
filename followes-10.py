import os
import requests
import time
from bs4 import BeautifulSoup

# مسح الشاشة قبل العرض
os.system("clear" if os.name == "posix" else "cls")

# أكواد ANSI للألوان
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

ascii_art = f"""{GREEN}
+--- IMAD-213 ---+


IIIIIIIIIIMMMMMMMM               MMMMMMMM               AAA               DDDDDDDDDDDDD                          222222222222222      1111111    333333333333333   
I::::::::IM:::::::M             M:::::::M              A:::A              D::::::::::::DDD                      2:::::::::::::::22   1::::::1   3:::::::::::::::33 
I::::::::IM::::::::M           M::::::::M             A:::::A             D:::::::::::::::DD                    2::::::222222:::::2 1:::::::1   3::::::33333::::::3
II::::::IIM:::::::::M         M:::::::::M            A:::::::A            DDD:::::DDDDD:::::D                   2222222     2:::::2 111:::::1   3333333     3:::::3
  I::::I  M::::::::::M       M::::::::::M           A:::::::::A             D:::::D    D:::::D                              2:::::2    1::::1               3:::::3
  I::::I  M:::::::::::M     M:::::::::::M          A:::::A:::::A            D:::::D     D:::::D                             2:::::2    1::::1               3:::::3
  I::::I  M:::::::M::::M   M::::M:::::::M         A:::::A A:::::A           D:::::D     D:::::D                          2222::::2     1::::1       33333333:::::3 
  I::::I  M::::::M M::::M M::::M M::::::M        A:::::A   A:::::A          D:::::D     D:::::D ---------------     22222::::::22      1::::l       3:::::::::::3  
  I::::I  M::::::M  M::::M::::M  M::::::M       A:::::A     A:::::A         D:::::D     D:::::D -:::::::::::::-   22::::::::222        1::::l       33333333:::::3 
  I::::I  M::::::M   M:::::::M   M::::::M      A:::::AAAAAAAAA:::::A        D:::::D     D:::::D ---------------  2:::::22222           1::::l               3:::::3
  I::::I  M::::::M    M:::::M    M::::::M     A:::::::::::::::::::::A       D:::::D     D:::::D                 2:::::2                1::::l               3:::::3
  I::::I  M::::::M     MMMMM     M::::::M    A:::::AAAAAAAAAAAAA:::::A      D:::::D    D:::::D                  2:::::2                1::::l               3:::::3
II::::::IIM::::::M               M::::::M   A:::::A             A:::::A   DDD:::::DDDDD:::::D                   2:::::2       222222111::::::1113333333     3:::::3
I::::::::IM::::::M               M::::::M  A:::::A               A:::::A  D:::::::::::::::DD                    2::::::2222222:::::21::::::::::13::::::33333::::::3
I::::::::IM::::::M               M::::::M A:::::A                 A:::::A D::::::::::::DDD                      2::::::::::::::::::21::::::::::13:::::::::::::::33 
IIIIIIIIIIMMMMMMMM               MMMMMMMMAAAAAAA                   AAAAAAADDDDDDDDDDDDD                         22222222222222222222111111111111 333333333333333   
{RESET}

{RED}----IMAD-213>INSTA-FOLLOWERS----{RESET}
{RED}
1 - followers-login
2 - exit{RESET}
"""

print(ascii_art)

# استقبال الخيار من المستخدم
choice = input(f"{GREEN}Select number: {RESET}")

if choice == "1":
    session = requests.Session()

    # إدخال بيانات المستخدم
    username = input("Enter username: ")
    password = input("Enter password: ")
    target_username = input("Enter target username to send followers: ")

    # قائمة المواقع مباشرة داخل السكربت
    sites = [
        "takipcimx.net",
        "takipcizen.com",
        "takipcibase.com",
        "takip88.com",
        "www.takipciking.net",
        "www.bigtakip.net",
        "www.takipcigen.com",
        "takipcikrali.com",
        "instamoda.org",
        "takipcimx.net"
    ]

    for site in sites:
        print(f"{RED}START NEW FOLLOWERS{RESET}")

        login_url = f"https://{site}/login?"
        headers = {
            "Host": site,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "Referer": f"https://{site}/login"
        }
        login_data = {
            "username": username,
            "password": password,
            "userid": "",
            "antiForgeryToken": "5e65770c2420a986097445ab74b0e24b"
        }

        response = session.post(login_url, headers=headers, data=login_data)

        if response.status_code == 200 and "success" in response.text:
            print(f"{GREEN}تم تسجيل الدخول بنجاح!{RESET}")

            find_user_url = f"https://{site}/tools/send-follower?formType=findUserID"
            followers_data = {"username": target_username}

            followers_response = session.post(find_user_url, headers=headers, data=followers_data)

            if followers_response.status_code == 200:
                soup = BeautifulSoup(followers_response.text, 'html.parser')
                user_id_input = soup.find("input", {"name": "userID"})

                if user_id_input:
                    user_id = user_id_input["value"]
                    print(f"{RED}START{RESET}")

                    send_followers_url = f"https://{site}/tools/send-follower/{user_id}?formType=send"
                    send_followers_data = {"adet": "100", "userID": user_id, "userName": target_username}

                    send_response = session.post(send_followers_url, headers=headers, data=send_followers_data)

                    if send_response.status_code == 200:
                        print(f"{RED}FOLLOWERS SENT SUCCESS{RESET}")

                        for i in range(10, 110, 10):
                            print(f"{GREEN}FOLLOWERS SUCCESS {i}%{RESET}")
                            time.sleep(4)
                    else:
                        print(f"{RED}ERROR!{RESET}")
                else:
                    print(f"{RED}COMPTE PRIVATE{RESET}")
            else:
                print(f"{RED}ERROR!{RESET}")
        else:
            print(f"{RED}COMPTE BANEE{RESET}")

    print("COMPLET SENT FOLLOWERS")

elif choice == "2":
    print("EXIT...")
else:
    print(f"{RED}ERROR!{RESET}")
