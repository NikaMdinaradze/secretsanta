import random
import smtplib
import ssl
from email.message import EmailMessage

email_sender = ''#enter your email
email_password = '' #enter your email password (16 digits)

mimgebebi = []
mchuqnelebi = []


saxeli = "saxeli"
while saxeli != "":
    saxeli = input("chaswerei saxeli: ")
    mimgebebi.append(saxeli)
    mchuqnelebi.append(saxeli)

mimgebebi.pop()
mchuqnelebi.pop()



for mchuqneli in mchuqnelebi:
    random_mimgebi = random.choice(mimgebebi)
    while random_mimgebi == mchuqneli:
        random_mimgebi = random.choice(mimgebebi)
    mimgebebi.remove(random_mimgebi)
    print(mchuqneli)
    print(random_mimgebi)
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = mchuqneli
    em['Subject'] = "sekret santai"
    em.set_content(random_mimgebi)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, mchuqneli, em.as_string())


    
    


