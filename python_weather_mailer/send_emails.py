import smtplib

def send_emails(emails, forecast):
    # Connect to the SMTP Server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    password = input("What's your password?")
    from_email = 'criviere@gmail.com'
    server.login(from_email, password)

    # Send to entire e-mail list
    for to_email, name in emails.items():
        message = "Subject: Camilo's Daily Weather Update!\n"
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'

        server.sendmail(from_email, to_email, message)

    server.quit()
