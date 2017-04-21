import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def MotionSendEmail():
    fromaddr = "ABC@gmail.com"
    toaddr = "123@gmail.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Motion detected'
    body = 'Motion was detected by Raspberry Pi. Check attached file'
    msg.attach(MIMEText(body, 'plain'))

    filename='motion.log'
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=%s' % filename)
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, 'USE YOUR EMAIL PASSWORD')
    text = msg.as_string()
    print "send email"
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


# self-test
#MotionSendEmail()


