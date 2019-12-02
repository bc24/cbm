email=input("Bitte gebe die E-Mail Adresse ein: ")
if email.count("@") !=1:
        print("Fehlerhafte E-Mail Adresse")
        continue

email_parts = email.split("@")

if email_parts[1].count(".") <=0:
        print("Fehlerhafte E-Mail Adresse")
        continue

if len(email_parts[0]) <=0:
        print("Fehlerhafte E-Mail Adresse")
        continue

print(f"E-Mail Adresse: {email} ")
break
