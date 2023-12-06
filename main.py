import aiosmtplib
import random
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

        # Set the content type to 'text/html'
        em.add_alternative(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Secret Santa Event</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 20px;
                    }}
                    .container {{
                        max-width: 600px;
                        margin: auto;
                        text-align: center;
                    }}
                    .header {{
                        background-color: #f5f5f5;
                        padding: 10px;
                    }}
                    .main-content {{
                        padding: 20px;
                    }}
                    .deadline {{
                        color: #d9534f;
                        font-weight: bold;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>Secret Santa Event</h1>
                    </div>
                    <div class="main-content">
                        <p>Hello {sender}!</p>
                        <p>This year, you are the Secret Santa for:</p>
                        <h2>{receiver}</h2>
                        <p>The deadline to deliver your gift is <span class="deadline">{gift_date}</span>.</p>
                        <p>Remember to keep it a secret and have fun!</p>
                        <p>Best wishes,</p>
                        <p>The Secret Santa Team</p>
                    </div>
                </div>
            </body>
            </html>
        """, subtype='html')

        await aiosmtplib.send(em, hostname="smtp.gmail.com",
                              port=587,
                              username=email_sender,
                              password=email_password)


