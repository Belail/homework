#-*-coding:utf-8-*-
#python3.6
#folw_chart : https://www.processon.com/view/link/58c2d3d7e4b0f2e6f8319e18

forbidden_file = open("forbidden_list.txt","a+")
forbidden_file.seek(0)

useradmin = "Belail"
password = "yeshengchengxuyuan"
error_useradmin = []

for i in range(3):
    login_useradmin = input("useradmin:")
    login_password = input("password:")
    if login_useradmin not in forbidden_file.read():
        if login_password == password and login_useradmin == useradmin:
            print("Login successful , Welcome to my territory")
            break
        elif login_password != password and login_useradmin == useradmin:
            print("Password error please re-enter")
            error_useradmin.append(login_useradmin + "\n")
            continue
        elif login_useradmin != useradmin:
            print("User name does not exist , Please re-enter")
            error_useradmin.append(login_useradmin+"\n")
            continue
    else:
        print("User has been disabbled")
        break
else:
    print("Error more than 3 times")
    forbidden_file.writelines(error_useradmin)
