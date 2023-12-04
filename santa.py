import aiosmtplib
import random
import ssl
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("EMAIL_PASSWORD")


class Santa:
    @staticmethod
    def _check_self_senders(list1, list2):
        zipped = zip(list1, list2)
        for person1, person2 in zipped:
            if person1 == person2:
                return True
        return False

    @classmethod
    def pair_people(cls, people):
        senders = [*people]
        random.shuffle(people)
        while cls._check_self_senders(senders, people):
            random.shuffle(people)

        return zip(senders, people)

    @staticmethod
    async def send_mail(sender, receiver, gift_date):
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = sender
        em['Subject'] = "Secret Santa"
        em.set_content(f"You are the secret Santa of {receiver}. You should send gift until {gift_date}")

        await aiosmtplib.send(em, hostname="smtp.gmail.com",
                              port=587,
                              username=email_sender,
                              password=email_password)



