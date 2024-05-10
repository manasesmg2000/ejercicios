user_1 = str("USER1")
password_user_1 = str("123456789A")
user_2 = str("USER2")
password_user_2 = str("987654321Z")



what_user = str(input("Introduce tu Nombre de Usuario: "))
what_password = str(input("Introduce la contraseña de Usuario: "))

len_pass_input = len(what_password)
len_pass_real= len(password_user_1)



while (what_user == user_1 and what_password == password_user_1 or what_user == user_2 and what_password == password_user_2):
     break


while (not what_user == user_1 and what_password == password_user_1 or not what_user == user_2 and what_password == password_user_2):

    while (not what_user == user_1 or not what_user == user_2 ):
         print("el usuario introduccido no es valido o no existe")
         what_user = str(input("Introduce tu Nombre de Usuario: "))
         what_password = str(input("Introduce la contraseña de Usuario: "))
  
    while (not what_password == password_user_1 or not what_password == password_user_2 ):
                while (len_pass_input == len_pass_real):
                    print("la contraseña es invalida")
                    what_user = str(input("Introduce tu Nombre de Usuario: "))
                    what_password = str(input("Introduce la contraseña de Usuario: "))
               
                while (len_pass_input > len_pass_real):
                        print(f"la contraseña es demasiado larga, debe ser de {len_pass_real} caracteres y es de {len_pass_input} ")
                        what_user = str(input("Introduce tu Nombre de Usuario: "))
                        what_password = str(input("Introduce la contraseña de Usuario: "))
                
                while(len_pass_input < len_pass_real):
                            print(f"la contraseña es demasiado corta, debe ser de {len_pass_real} caracteres y es de {len_pass_input} ")
                            what_user = str(input("Introduce tu Nombre de Usuario: "))
                            what_password = str(input("Introduce la contraseña de Usuario: "))
                else:
                            print("error del sistema")



if(what_user == user_1 and what_password == password_user_1): 
    print(f"Bienbenido al sistema {user_1}")

if (what_user == user_2 and what_password == password_user_2):
    print(f"Bienbenido al sistema {user_2}")











