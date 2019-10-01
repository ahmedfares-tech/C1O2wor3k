import os
import io
import errno
import datetime

# default employer login is -> username : default -> password : defaul123
# default admin login is -> username : default -> password : defaul123

_role_login = ""


def _start_checker():
    # *******************************************************************
    # *                                                                 *
    # *                             Direction checkker                  *
    # *                                                                 *
    # *******************************************************************
    try:
        # admin folder and file path
        _admin_check_folder = os.path.isdir("admin/")
        _admin_check_file = os.path.isfile("admin/admin.txt")

        # employer folder and file path
        _employer_check_folder = os.path.isdir("employer/")
        _employer_check_file = os.path.isfile("employer/employer.txt")

        # client folder path
        _client_folder_exists = os.path.isdir("clients/")

        # check if folder is exists if it's True nothing well do
        # else he will create the folder for clients
        if(_client_folder_exists == True):
            print("All Right")
        elif(_client_folder_exists == False):
            os.makedirs("clients/")
            print("client folder created succ")
        else:
            print("contact the adminstrator there is a big issue")

        # check if file or folder is exists if it's True nothing well do
        # else he will create the folder or the file for admins which is not exists
        if(_admin_check_file == True and _admin_check_folder == True):
            print("All Right")
        elif(_admin_check_file == False and _admin_check_folder == True):
            create_admin = open("admin/admin.txt", "w+")
            create_admin.write("default,default123,")
            create_admin.close()
            print("admin file created succ")
        elif(_admin_check_folder == False):
            os.makedirs("admin/")
            create_admin = open("admin/admin.txt", "w+")
            create_admin.write("default,default123,")
            create_admin.close()
            print("admin folder created succ")
        else:
            print("please contact the adminstrator there is a big issue")

        # check if file or folder is exists if it's True nothing well do
        # else he will create the folder or the file for employer which is not exists
        if(_employer_check_file == True and _employer_check_folder == True):
            print("All Right")
        elif(_employer_check_file == False and _employer_check_folder == True):
            create_employer = open("employer/employer.txt", "w+")
            create_employer.write("default,default123,")
            create_employer.close()
            print("employer file created succ")
        elif(_employer_check_folder == False):
            os.makedirs("employer/")
            create_employer = open("employer/employer.txt", "w+")
            create_employer.write("default,default123,")
            create_employer.close()
            print("employer folder created succ")

        else:
            print("please contact the adminstrator there is a big issue")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def _read_admin_file(username, password):
    # *******************************************************************
    # *                                                                 *
    # *                         read admin file for checking            *
    # *                                                                 *
    # *******************************************************************
       # open File admin as Read
    _read_admin_file = open("admin/admin.txt", "r+")

    # Get all Data in txt file
    get_data_admin_file = _read_admin_file.readlines()

    for _admin_users in get_data_admin_file:
        _default_list = _admin_users.strip().split(',')

    # close connection
    _read_admin_file.close()

    _count_index = len(_default_list)

    _admin_dic = {}

    _admin_user_index = 0

    while(_admin_user_index < _count_index - 1):
        _admin_dic.update(
            {_default_list[_admin_user_index]: _default_list[_admin_user_index + 1]})
        _admin_user_index += 2

    _check_passwordFrom_Data = _admin_dic.get(username)

    # Var For while To try while for 3 times
    # Check for Username and password in Users Dictionry
    if(username in _admin_dic and password == _check_passwordFrom_Data):

        # If username and password Right Welcome The user with his name
        return 1

        # check from username is Right or No
    elif(username not in _admin_dic):

        # If Username is wrong Tell Him to check his username first
        return 2

        # Check If username is Right and the password is Wrong
    elif(username in _admin_dic and password != _check_passwordFrom_Data):

        # If Username is Right and password Wrong
        return 3

    else:

        # in Any other Issues case in the programme he should go to contact The IT
        print("Please Contact The Adminstrator For Help")
        return 4


def _read_employer_file(username, password):
    # *******************************************************************
    # *                                                                 *
    # *                         read employer file for checking         *
    # *                                                                 *
    # *******************************************************************
    # open File Employer as Read
    _read_employ_file = open("employer/employer.txt", "r+")

    # Get all Data in txt file
    get_data_employ_file = _read_employ_file.readlines()

    # for loop to put all data in list and every word in index *He know its end of word by split

    for _employ_users in get_data_employ_file:
        _default_list = _employ_users.strip().split(',')

    # close connection
    _read_employ_file.close()

    _count_index = len(_default_list)

    _employer_dic = {}

    _employer_user_index = 0

    while(_employer_user_index < _count_index - 1):
        _employer_dic.update(
            {_default_list[_employer_user_index]: _default_list[_employer_user_index + 1]})
        _employer_user_index += 2

    _check_passwordFrom_Data = _employer_dic.get(username)

    # Var For while To try while for 3 times
    # Check for Username and password in Users Dictionry
    if(username in _employer_dic and password == _check_passwordFrom_Data):

        # If username and password Right Welcome The user with his name
        return 1

        # check from username is Right or No
    elif(username not in _employer_dic):

        # If Username is wrong Tell Him to check his username first
        return 2

        # Check If username is Right and the password is Wrong
    elif(username in _employer_dic and password != _check_passwordFrom_Data):

        # If Username is Right and password Wrong
        return 3
    elif(username in _employer_dic):
        return 4
    else:

        # in Any other Issues case in the programme he should go to contact The IT
        print("Please Contact The Adminstrator For Help")
        return 5


def _admin_creation():
    # *******************************************************************
    # *                                                                 *
    # *                             admin Creation                      *
    # *                                                                 *
    # *******************************************************************
    # admin File Path
    _admin_data_exists = os.path.isfile("admin/admin.txt")

    # If Admin file is not exists
    if (_admin_data_exists == False):

        while(True):

            # enter His Admin username
            _admin_username = input("Enter your admin username: \n")

            if(len(_admin_username) < 1):

                print("please enter admin username")

            else:

                break

        # Variable For While To check from password and confirm password2
        _check_double_password = "Y"

        # While loop to check password and confirm password
        while (_check_double_password == "Y"):

            while(True):

                # admin password
                _admin_password = input("Enter Your admin password: \n")

                if(len(_admin_password) < 1):

                    print("please enter admin password")

                else:

                    break
            # confirm admin password
            _admin_confirm_password = input("Please Confirm Your password: \n")

            # if conditional to check if two passwords are same
            if(_admin_password != _admin_confirm_password):

                # if not same print 'are not matched'
                print("Passwords Are not matched! \n")

            elif(_admin_password == _admin_confirm_password):

                # if same go to while-> else
                _check_double_password = "N"

        else:

            # Create a file in path 'admin/' with name 'admin.txt
            _admin_file = open("admin/admin.txt", "w")

            # close connection
            _admin_file.close()

            # open file to Add username and password
            _admin_file = open("admin/admin.txt", "a+")

            # Write  Username and password in 'admin.txt' file
            _admin_file.writelines(
                _admin_username + "," + _admin_password + ",")

            # close connection
            _admin_file.close()

    elif(_admin_data_exists == True):

        # check from admin if he want to add new admin or no
        _new_admin_check = input(
            "Did you want to add new admin To your system [Y/N]").lower()

        # if y then start get information
        if(_new_admin_check == "y"):

            while(True):

                    # Enter admin Username
                _new_admin_username = input(
                    "Enter your admin username: \n")

                if (len(_new_admin_username) < 1):

                    print("username field is empyte")

                else:

                    get_return = _read_admin_file(_new_admin_username, "")
                    if(get_return == 4 or get_return == 3):
                        print("username is exsits please choose anothe one")
                    elif(get_return == 2):
                        break

            # Again Variable for while loop to check from password
            _check_admin_double_password = "Y"

            # While loop to check password and confirm password
            while (_check_admin_double_password == "Y"):

                while(True):
                    # admin password

                    _new_admin_password = input(
                        "Enter Your admin password: \n")

                    if(len(_new_admin_password) < 1):

                        print("password Field is empyte")
                    else:

                        break
                # confirm admin password
                _new_admin_confirm_password = input(
                    "Please Confirm Your password: \n")

                # if conditional to check if two passwords are same
                if(_new_admin_password != _new_admin_confirm_password):

                    # if not same print 'are not matched
                    print("Passwords Are not matched! \n")

                elif(_new_admin_password == _new_admin_confirm_password):

                    # if same go to while-> else
                    _check_admin_double_password = "N"

            else:

                # if the password and confirm are matched then start to write in the file
                # open file in append mode to start writing in it with out remove it or recreatian for him
                _admin_file = open("admin/admin.txt", "a+")

                # write the new username and password of new admin
                _admin_file.writelines(
                    _new_admin_username + "," + _new_admin_password + ",")

                # close connection
                _admin_file.close()

                # if he won't add new admin and changed his mind he press N or n
        elif(_new_admin_check == "n"):

            # We love our Boss :P
            print("You're Welcome in any time sir\n")

        else:

            # User Want to play or tester want to get app break then we kill him :)
            print("please Enter Correct Choose!\n")


def _add_employer():
    # *******************************************************************
    # *                                                                 *
    # *                             ADD employer                        *
    # *                                                                 *
    # *******************************************************************
        # empployer users file path
    _employ_data_exist = os.path.isfile("employer/" + "employer.txt")

    # if employer file not exists start to create new one and add one employer in it
    if (_employ_data_exist == False):
        _create_file_employer = open("employer/employer.txt", "w+")
        _create_file_employer.close()
        while(True):

                # Enter Employer Username
            _employ_username = input("Enter your employer username: \n")

            if (len(_employ_username) < 1):

                print("username field is empyte")

            else:

                get_return = _read_employer_file(_employ_username, "")
                if(get_return == 4 or get_return == 3):
                    print("username is exsits please choose anothe one")
                elif(get_return == 2):
                    break
        # Variable For While To check from password and confirm password2
        _check_employ_double_password = "Y"

        # While loop to check password and confirm password
        while (_check_employ_double_password == "Y"):

            while(True):

                # employer password
                _employ_password = input("Enter Your employer password: \n")

                if(len(_employ_password) < 1):

                    print("password field is empyte")

                else:

                    break

            # confirm employer password
            _employ_confirm_password = input(
                "Please Confirm Your password: \n")

            # if conditional to check if two passwords are same
            if(_employ_password != _employ_confirm_password):

                    # if not same print 'are not matched'
                print("Passwords Are not matched! \n")

                # if they same
            elif(_employ_password == _employ_confirm_password):
                    # go to while-> else
                _check_employ_double_password = "N"

        else:

            # open file with append 'a+' to Add username and password
            _employ_file = open("employer/" + "employer.txt", "a+")

            # Write  Username and password in 'employer.txt' file
            _employ_file.writelines(
                _employ_username + "," + _employ_password + ",")

            # close connection
            _employ_file.close()

        # if file is exist in folder then
    elif(_employ_data_exist == True):

        # check from admin if he want to add new employer or no
        _new_employ_check = input(
            "Did you want to add new employer To your system [Y/N]")

        # if y then start get information
        if(_new_employ_check == "y" or _new_employ_check == "Y"):

            while(True):

                    # Enter Employer Username
                _new_employ_username = input(
                    "Enter your employer username: \n")

                if (len(_new_employ_username) < 1):

                    print("username field is empyte")

                else:

                    get_return = _read_employer_file(_new_employ_username, "")
                    if(get_return == 4 or get_return == 3):
                        print("username is exsits please choose anothe one\n")
                    elif(get_return == 2):
                        break

            # Again Variable for while loop to check from password
            _check_employ_double_password = "Y"

            # While loop to check password and confirm password
            while (_check_employ_double_password == "Y"):

                while(True):
                    # employer password

                    _new_employ_password = input(
                        "Enter Your employer password: \n")

                    if(len(_new_employ_password) < 1):

                        print("password Field is empyte")
                    else:

                        break
                # confirm employer password
                _new_employ_confirm_password = input(
                    "Please Confirm Your password: \n")

                # if conditional to check if two passwords are same
                if(_new_employ_password != _new_employ_confirm_password):

                    # if not same print 'are not matched
                    print("Passwords Are not matched! \n")

                elif(_new_employ_password == _new_employ_confirm_password):

                    # if same go to while-> else
                    _check_employ_double_password = "N"

            else:

                # if the password and confirm are matched then start to write in the file
                # open file in append mode to start writing in it with out remove it or recreatian for him
                _employ_file = open("employer/" + "employer.txt", "a+")

                # write the new username and password of new employer
                _employ_file.writelines(
                    _new_employ_username + "," + _new_employ_password + ",")

                # close connection
                _employ_file.close()

                # if he won't add new employer and changed his mind he press N or n
        elif(_new_employ_check == "n" or _new_employ_check == "N"):

            # We love our Boss :P
            print("You're Welcome in any time sir\n")

        else:

            # User Want to play or tester want to get app break then we kill him :)
            print("please Enter Correct Choose!\n")


def _login_employer():
    # *******************************************************************
    # *                                                                 *
    # *                       Log in  employer                          *
    # *                                                                 *
    # *******************************************************************
    global _role_login
    attemps = 0
    while(attemps < 4):
        _login_username = input("Enter your username:\n").lower()

        _login_password = input("Enter your password:\n")

        get_return = _read_employer_file(_login_username, _login_password)

        if(get_return == 1):
            print("Username & password Are Coreect Logged in!")
            _role_login = "employer"
            break
        elif(get_return == 2):
            print("username not found!")
            attemps += 1
        elif(get_return == 3):
            print("password is incorrect!")
            attemps += 1
        elif(get_return == 5):
            print("There Is And isuue call the IT")
            attemps += 1


def _login_admin():
    # **********************************************************************
    # *                                                                   *
    # *                       Log in  admin                               *
    # *                                                                   *
    # **********************************************************************
    global _role_login
        # Get Login Username and password
        # .lower() To put all username in Lower Letters
    attemps = 0
    while(attemps < 4):
        _login_username = input("Enter your username:\n").lower()

        _login_password = input("Enter your password:\n")

        get_return = _read_admin_file(_login_username, _login_password)

        if(get_return == 1):
            print("Username & password Are Coreect Logged in!")
            _role_login = "admin"
            break
        elif(get_return == 2):
            print("username not found!")
            attemps += 1
        elif(get_return == 3):
            print("password is incorrect!")
            attemps += 1
        elif(get_return == 4):
            print("There Is And isuue call the IT")
            attemps += 1


def _client_and_products():
    # Variables for Excute function to work and do his work
    _client_product_list = []
    _client_product_list_fixerror = []
    _checkout_print_product = 0
    _get_product_tolist = 0
    _total_product = 0
    _product_details_index = 3
    start_time = datetime.datetime.now()
    end_time = datetime.datetime.now()
    while(True):
        _client_identify = input("please enter client username or phone number as he want!\n")
        if(len(_client_identify)<1):
            print("please enter correct client identify")
        else:
            break
    _client_exists = os.path.isfile("clients/" + _client_identify + ".txt")

    if(_client_exists == False):
        start_h = start_time.hour
        if(start_h > 12):
            start_h = start_h - 12
        else:
            start_h = start_h
        start_m = start_time.minute

        client_login = open("clients/" + _client_identify + ".txt", "w+")

        client_login.write(str(_client_identify) + "," +
                           str(start_h) + "," + str(start_m) + ",")

        client_login.close()
        print("client file created please have a sit! :D")
    elif(_client_exists == True):
        while(True):
            _choose_checkout_add = input(
                "Do you want to check out[c] or add product for user [a]\n").lower()
            if(_choose_checkout_add == "a"):
                while(True):
                    _check_more = input("Want to Add Product [Y/N]\n")
                    if(_check_more == "y"):
                        while(True):
                            _new_product_name = input(
                                "please enter product name or id\n")
                            if(len(_new_product_name)<1):
                                print("please enter product name to continue! \n")
                            else:
                                break
                        

                        while(True):
                            
                            _new_product_price = input("please enter product price\n")
                            if(_new_product_price.isdigit()):
                                break
                            
                            else:
                                print("enter product price (without fractions),or letters")
                        _client_product_list.append(_new_product_name)
                        _client_product_list.append(_new_product_price)
                        _add_product = open(
                            "clients/" + _client_identify + ".txt", "a+")
                        _add_product.writelines(
                            _new_product_name + "," + str(_new_product_price) + ",")
                        _add_product.close()
                    elif(_check_more == "n"):
                        print("Ending of add productus\n")
                        break
                    else:
                        print("please enter coreect choose\n")
            elif(_choose_checkout_add == "c"):
                _check_out_client = open("clients/"+_client_identify+".txt", "r+")
                _data_get_client = _check_out_client.readlines()

                for i in _data_get_client:
                    _store_data_intolist = i.strip().split(",")
                # print("this list after split ','", finall1)

                _get_len = len(_store_data_intolist)
                # in this i want to get product namees and prices only for this i remove last index which is empyte by default
                # and first 3 indexs which i don't want them to get my len which i want of productus only 
                
                _len_for_product = _get_len - 4
                if(_len_for_product<1):
                    print("no product we get")
                else:
                    while(_get_product_tolist < _len_for_product):
                        
                        _client_product_list_fixerror.append(
                            _store_data_intolist[_product_details_index])
                        
                        _client_product_list_fixerror.append(
                            _store_data_intolist[_product_details_index+1])
                        
                        _get_product_tolist += 2
                        _product_details_index += 2
                    
                start_h = float(_store_data_intolist[1])
                
                start_m = float(_store_data_intolist[2])
                
                f_start = (start_h*60)+start_m

                end_h_c = end_time.hour
                
                if(end_h_c > 12):
                    
                    end_h = end_h_c - 12
                    
                else:
                    
                    end_h = end_h_c
                    
                end_m = end_time.minute

                f_end = (end_h*60) + end_m

                totalh = (abs(f_start - f_end))
                
                totalh_price = totalh * 10
                
                # below comment for me only
                # list = [identify,start , name,price,name,price,name,price]
                # first product index (3) -> second product index (3+2)

            #            for i in get_date_start:
            #                print("hello this is i")
                _check_out_client.close()
                client_login = open("clients/" + _client_identify + ".txt", "a+")

                client_login.writelines(str(f_end) + "," + str(totalh) + ",")

                client_login.close()

                print("Checkout recipt:")
                print("Identify (username OR phone):", _client_identify, "\n")
                print("Start Time:", f_start, "\n")
                print("End Time:", f_end, "\n")
                print("Total Time:", totalh, "\n")

                _get_len_list = len(_client_product_list_fixerror)

                while(True):
                    if(_checkout_print_product < _get_len_list):

                        # Print Product Name
                        print(
                            "Product Name", _client_product_list_fixerror[_checkout_print_product], "\n")
                        # print Product Price
                        print("Product Price:",
                              _client_product_list_fixerror[_checkout_print_product+1], "\n")
                        # Get Sum of all productts
                        _total_product = _total_product + float(_client_product_list_fixerror[_checkout_print_product+1])

                        _checkout_print_product += 2
                    else:
                        print("total price product:", _total_product)
                        print("total hours price:", totalh_price)
                        print("Total Paid money:",
                              _total_product + totalh_price)
                        os.remove("clients/"+ _client_identify+".txt")
                        break
                break
    else:
        print("Contact IT For This issue! :(")


print("Check From All Folders and files of Programm....\n")
_start_checker()
while(True):

    _main_start = input("1.create admin\n 2.admin login \n 3. create employer\n 4.login employer\n 5.client create and checkout\n 6.exit\n")
    if(_main_start == "1" and _role_login =="admin"):
        _admin_creation()
    elif(_main_start == "1" and _role_login != "admin"):
        print("This Function is available for admin only")
    elif(_main_start == "2"):
        _login_admin()
    elif(_main_start == "3" and _role_login == "admin"):
        _add_employer()
    elif(_main_start == "3" and _role_login != "admin"):
        print("This Function is available for admin only")
    elif(_main_start == "4"):
        _login_employer()
    elif(_main_start == "5" and (_role_login == "admin" or _role_login == "employer")):
        _client_and_products()
    elif(_main_start == "5" and (_role_login != "admin" or _role_login != "employer")):
        print("You should log in first ")
    elif(_main_start == "6"):
        break
    else:
        print("please enter correct choose")
