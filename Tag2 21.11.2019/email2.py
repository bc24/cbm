while True:
    email = input("Bitte E-Mail Adresse eingeben: ")

    if email.count("@") == 1:
        email_parts = email.split("@")
        
        if email_parts[1].count(".") > 0:
            if len( email_parts[0] ) > 0 :
                print(f"E-Mail-Adresse: {email}")
                break
    
    print("Fehlerhafte E-Mail-Adresse [0xc12344]")
    