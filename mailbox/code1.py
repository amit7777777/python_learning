import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "amitkumar.tcet9@gmail.com"
password = input("Type your password and press enter: ")
passwordapp="zmskzeeuyvwyhjck";

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    print("emai ", sender_email)
    print(password)
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, passwordapp)

    # TODO: Send email here
    print("connection success")
except Exception as e:
    # Print any error messages to stdout
    print(e)
    print("not successful")
finally:
    server.quit()