
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from werkzeug.utils import secure_filename



def email(subject, body, receiver, cc=None, file=None, listbool=False):

    print("LISTBOOL: " + str(listbool))
    port = 465  # For SSL
    password = "REIDpres2021"

    sender="badgerclubtennis@gmail.com"
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender

    if listbool == False:
        message["To"] = receiver
    else:
        message["To"] = ", ".join(receiver)
        
    message["Subject"] = subject
    
    if cc is not None:
        print(cc)
        message["Cc"] = cc
    #message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    if file.filename != "":
        print(file)
    # Open PDF file in binary mode
    
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(file.read())

            # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

            #Add header as key/value pair to attachment part
        part.add_header("Content-Disposition",f"attachment; filename= {secure_filename(file.filename)}",)

    # Add attachment to message and convert message to string
        message.attach(part)

    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, text)
        return True