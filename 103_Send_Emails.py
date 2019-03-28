#!/usr/bin/env python3.7

"""103_Send_Emails.py.

One Hundred and Third Program of the Corey Schafer Python Series.

"""
import logging
import os
import smtplib
import imghdr
from email.message import EmailMessage
from platform import python_version
from sys import hexversion
from datetime import datetime as dt

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

NOW = dt.today()
PRINT_VERSION_INFO = True
PRINT_TIME = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str(hexversion))
logging.basicConfig(filename="LOG_files/LOG_103.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("103_Send_Emails.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None

# THIS WILL HAVE TO BE DONE IN TERMINAL, (not persistant.)
# $ EMAIL_ADDRESS='highslater@gmail.com'
# $ EMAIL_PASSWORD='xxxxxxxxxx'

# $ set | grep EMAIL
# EMAIL_ADDRESS=highslater@gmail.com
# EMAIL_PASSWORD='xxxxxxxxxx'

# $ export EMAIL_ADDRESS
# $ export EMAIL_PASSWORD
# $ printenv | grep 'EMAIL'
# EMAIL_ADDRESS=highslater@gmail.com
# EMAIL_PASSWORD=xxxxxxxxxx


# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     # with smtplib.SMTP('localhost', 1025) as smtp:
#     # python3 -m smtpd -c DebuggingServer -n localhost:1025
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

#     subject = 'Grab dinner tonight?'
#     body = 'How about dinner at six?'

#     msg = f'Subject: {subject}\n\n{body}'

#     smtp.sendmail(EMAIL_ADDRESS, 'highslater@hotmail.com', msg)

# print("Sending Email from: {}, with password of: {}".format(EMAIL_ADDRESS,
#                                                             None))


# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

#     subject = 'Grab dinner tonight?'
#     body = 'How about dinner at six?'

#     msg = f'Subject: {subject}\n\n{body}'

#     smtp.sendmail(EMAIL_ADDRESS, 'highslater@hotmail.com', msg)

# print("Sending Email from: {}, with password of: {}".format(EMAIL_ADDRESS,
#                                                             None))

# msg = EmailMessage()
# msg['subject'] = 'Grab dinner tonight?'
# msg['From'] = EMAIL_ADDRESS
# msg['To'] = 'highslater@hotmail.com'
# msg.set_content('How about dinner at six?')

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(msg)

# print("Sending Email from: {}, with password of: {}".format(EMAIL_ADDRESS,
#                                                             None))

# msg = EmailMessage()
# msg['subject'] = 'Puppys!'
# msg['From'] = EMAIL_ADDRESS
# msg['To'] = 'highslater@hotmail.com'
# msg.set_content('images attatched')

# files = ['./Files/beagle_1.jpg', './Files/beagle_2.jpeg']

# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_type = imghdr.what(f.name)
#         file_name = f.name
#         logger.info(
#             'Image Type: {}, Image Name: {}'.format(file_type, file_name))

#     msg.add_attachment(
#         file_data, maintype='image', subtype=file_type, filename=file_name)

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(msg)

# print("Sending Email from: {}, with password of: {}".format(EMAIL_ADDRESS,
#                                                             None))

# msg = EmailMessage()
# msg['subject'] = 'pdf'
# msg['From'] = EMAIL_ADDRESS
# msg['To'] = 'highslater@hotmail.com'
# msg.set_content('pdf attatched')

# files = ['./Files/lab 5 hub-and-spoke-frame-relay.pdf']

# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_name = f.name
#         logger.info(
#             'File Name: {}'.format(file_name))

#     msg.add_attachment(
#         file_data, maintype='application',
#         subtype='octet-stream', filename=file_name)

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(msg)

# print("Sending Email from: {}, with password of: {}".format(EMAIL_ADDRESS,
#                                                             None))

# contacts = ['highslater@hotmail.com', 'highslater@gmail.com']

# msg = EmailMessage()
# msg['subject'] = 'pdf'
# msg['From'] = EMAIL_ADDRESS
# # msg['To'] = contacts
# msg['To'] = ', '.join(contacts)
# msg.set_content('pdf attatched')

# files = ['./Files/lab 5 hub-and-spoke-frame-relay.pdf']

# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_name = f.name
#         logger.info(
#             'File Name: {}'.format(file_name))

#     msg.add_attachment(
#         file_data, maintype='application',
#         subtype='octet-stream', filename=file_name)

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(msg)

# print("Sending Email from: {}, with password of: {}".format(EMAIL_ADDRESS,
#                                                             None))


msg = EmailMessage()
msg['subject'] = 'HTML'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'highslater@hotmail.com'
msg.set_content('This is a plain text email.')

msg.add_alternative("""

<!DOCTYPE html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
        <h1 style="color:Red;">This is Red!</h1>
        <h1 style="color:Blue;">This is Blue</h1>
        <h1 style="color:Green;">This is Green</h1>
    </body>
</html>
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("Sending Email from: {}, with password of: {}".format(EMAIL_ADDRESS,
                                                            None))
