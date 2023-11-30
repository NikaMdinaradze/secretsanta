import random
import smtplib
import ssl
from email.message import EmailMessage

email_sender = ''#enter your email
email_password = '' #enter your email password (16 digits)


def get_people():
    people = []
    name = 1
    print("ENTER GMAILS")
    while name:
        name = input("->")
        if name in people:
            print("gmail is already in list")
            continue
        people.append(name)
    people.pop()
    return people


def check_self_senders(list1, list2):
    zipped = zip(list1, list2)
    for person1, person2 in zipped:
        if person1 == person2:
            return True
    return False


def pair_people(people):
    senders = [*people]
    random.shuffle(people)
    while check_self_senders(senders, people):
        random.shuffle(people)

    return zip(senders, people)


def send_mail(sender, receiver):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = sender
    em['Subject'] = "Secret Santa"
    em.set_content(f"You are secret santa of {receiver}")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, sender, em.as_string())


people = get_people()
paired = pair_people(people)

for sender, receiver in paired:
    send_mail(sender, receiver)
