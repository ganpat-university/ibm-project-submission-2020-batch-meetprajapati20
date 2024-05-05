import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


# Brevo SMTP Mailer
SMTP_SERVER = "smtp-relay.brevo.com"
PORT = 587
BREVO_USERNAME = "meetprajapati20@gnu.ac.in"
BREVO_SECURITY_KEY = "wdaMrWH1tjUDEYNB"

def send_mail(from_email, to_email, subject, message, attachment=None, filename=None):
	# Setup the MIME
	msg = MIMEMultipart()
	msg['From'] = from_email
	msg['To'] = ', '.join(to_email)
	msg['Subject'] = subject
	# Attach message to the email
	msg.attach(MIMEText(message, 'plain'))
	if attachment:
		if filename is None:
			return False, "Filename is required for attachment"
		attachment = MIMEApplication(attachment, _subtype="pdf")
		attachment.add_header('Content-Disposition', 'attachment', filename=filename)
		msg.attach(attachment)
	try:
		# Create SMTP session
		with smtplib.SMTP(SMTP_SERVER, PORT) as server:
			# Start TLS for security
			server.starttls()
			# Login
			server.login(BREVO_USERNAME, BREVO_SECURITY_KEY)
			# Send email
			server.sendmail(BREVO_USERNAME, to_email, msg.as_string())
			print("Email sent successfully!")
			# Quit the session
			server.quit()
			return True,"Email sent successfully!"
	except Exception as e:
		print("Error in sending email:", e)
		return False, e