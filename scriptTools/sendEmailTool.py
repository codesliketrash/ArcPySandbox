import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

# The following variables hold the information of the email sender and the email recipient
gmail_user = arcpy.GetParameterAsText(0)
gmail_pwd = arcpy.GetParameterAsText(1)
recipient = arcpy.GetParameterAsText(2)
subject = arcpy.GetParameterAsText(3)
body = arcpy.GetParameterAsText(4)
attachment = arcpy.GetParameterAsText(5)

def mail(to, subject, text, attach):
	msg = MIMEMultipart()

	msg['From'] = gmail_user
	msg['To'] = to
	msg['Subject'] = subject

	msg.attach(MIMEText(text))

	part = MIMEBase('application', 'octet-stream')
	part.set_payload(open(attach, 'rb').read())
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
	msg.attach(part)

	mailServer = smtplib.SMTP("smtp.gmail.com",587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login(gmail_user, gmail_pwd)
	mailServer.sendmail(gmail_user, to, msg.as_string())
	mailServer.close()

mail(recipient,
	subject,
	body,
	attachment)

print "your email and attachment have successfully been sent."
