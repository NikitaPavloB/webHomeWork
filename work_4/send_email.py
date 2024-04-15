import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


class EmailSender:
    def __init__(self, fromaddr, toaddr, password, reportname):
        self.fromaddr = fromaddr
        self.toaddr = toaddr
        self.password = password
        self.reportname = reportname

    def send_email(self):
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr
        msg['Subject'] = 'Hello from Python'

        with open(self.reportname, 'rb') as f:
            part = MIMEApplication(f.read(), Name=basename(self.reportname))
            part['Content-Disposition'] = f'attachment; filename={basename(self.reportname)}'
            msg.attach(part)

        body = 'Это пробное сообщение'
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.login(self.fromaddr, self.password)
        text = msg.as_string()
        server.sendmail(self.fromaddr, self.toaddr, text)
        server.quit()
