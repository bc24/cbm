while True:
    email = input("Bitte E-Mail Adresse eingeben: ")

    if email.count("@") != 1:
        print("Fehlerhafte E-Mail-Adresse [0xc12344]")
        continue
       
    else:
        email_parts = email.split("@")

        if email_parts[1].count(".") <= 0:
            print("Fehlerhafte E-Mail-Adresse [0xc12345]")
            continue
            
        elif len( email_parts[0] ) <= 0:
            print("Fehlerhafte E-Mail-Adresse [0xc12346]")
            continue

        

        print(f"E-Mail-Adresse: {email}")
        break