import smtplib

s = smtp.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('akglimitd@gmail.com', 'akglimited')
message = 'Subject: {}\n\n{}'.format('Hello', 'Hello Universe')
s.sendmail('akglimited@gmail.com', 'yoyoavadh@gmail.com', message)
s.quit()
