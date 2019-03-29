#!/usr/bin/env python3.7

"""103_Send_Emails.py.

One Hundred and Third Program of the Corey Schafer Python Series.

"""

# THIS WILL HAVE TO BE DONE IN TERMINAL, (not persistant.)
# $ EMAIL_ADDRESS='highslater@gmail.com'
# $ EMAIL_PASSWORD='xxxxxxxxxx'

# $ set | grep EMAIL
# EMAIL_ADDRESS=highslater@gmail.com
# EMAIL_PASSWORD='xxxxxxxxxx'

# $ export EMAIL_ADDRESS=highslater@gmail.com
# $ export EMAIL_PASSWORD=''
# $ printenv | grep 'EMAIL'
# EMAIL_ADDRESS=highslater@gmail.com
# EMAIL_PASSWORD=xxxxxxxxxx

import os
import smtplib
import imghdr  # noqa
import base64
from email.message import EmailMessage
from datetime import datetime as dt  # noqa

email_address = os.environ.get('EMAIL_ADDRESS')
email_password = os.environ.get('EMAIL_PASSWORD')
content = "This is a plain text Email, followed by HTML."
alternative = ("""
<!DOCTYPE html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
            <p>This is a plain text Email, followed by HTML.</p>
    </body>
</html>
""")


class Email():
    """Docstring for Email class."""

    def __init__(self, subject, sender,  # encryption level 16-32-64
                 recipient, content, alternative, subtype):
        """Docstring for __init__."""
        self.subject = subject
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.alternative = alternative
        self.subtype = subtype
        self.encrypted = False

    def __repr__(self):
        """Docstring."""
        return "{}, {}, {}, {}, {}, {}, {}".format(
            self.subject, self.sender,
            self.recipient, self.content,
            self.alternative, self.subtype,
            self.encrypted)

    def __str__(self):
        """Docstring."""
        # sc = [lambda: self.content,
        #       lambda: self.content.decode('utf-8')
        #       ][self.encrypted]
        sc = self.content.decode('utf-8') if self.encrypted else self.content
        return ("\nEncrypted:{}\nSubject: {}\nFrom: {}\nTo: {}\nBody: {}\n"
                "Alternative Body:\n {}\nSubtype:{}").format(
            self.encrypted, self.subject, self.sender, self.recipient, sc,
            self.alternative, self.subtype)

    def add_attachment(self):
        """Docstring."""
        pass

    def create_message(self):
        """Docstring."""
        msg = EmailMessage()
        msg['subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = self.recipient
        msg.set_content(self.content)

        if self.alternative:
            msg.add_alternative(self.alternative, subtype=self.subtype)
        self.message = msg

        if self.encrypted:
            self.message_encrypt()

    def send_message(self):
        """Docstring."""
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(self.message)

        print("Sending Email from: {}, to: {}".format(
            self.sender, self.recipient))


class EncryptedEmail(Email):
    """Docstring for EncryptedEmail."""

    def __init__(self, subject, sender, recipient, content, alternative,
                 subtype):
        """Docstring for __init__."""
        super().__init__(subject, sender, recipient, content, alternative,
                         subtype)
        self.encrypted = True
        self.encryption_level = 64

    def html_strip(self):
        """Do not encrypt html."""
        self.alternative = None
        pass

    def message_encrypt(self):
        """b64encode."""
        self.html_strip()
        self.content = base64.b64encode(
            bytes(self.content, 'utf-8'))

    def message_decrypt(self):
        """b64decode."""
        self.content = (base64.b64decode((self.content)))


email1 = EncryptedEmail('html', email_address, 'highslater@hotmail.com',
                        content, alternative, 'html')
email1.create_message()
print((email1))

email2 = Email('html', email_address, 'highslater@hotmail.com',
               content, alternative, 'html')
email2.create_message()
print((email2))
