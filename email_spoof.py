import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('Hello freak bitches')

msg['Subject'] = 'BIGLY TOP SECRET DUMBASS'
msg['From'] = 'test@gmail.com'
msg['To'] = 'russelljjadams2@gmail.com'

s = smtplib.SMTP('smtp-relay.sendinblue.com:587')
s.login("danielbcooper@parapsychicmusings.com", "hbg7CftH6Pv2VFpL")
s.send_message(msg)
s.quit()

