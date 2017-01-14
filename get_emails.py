#! /usr/bin/python2.7
def get_emails():

    #Reading emails from a file
    file = '/Users/Crivi002/Desktop/OneDrive/CodeSchool/python_web_mailer/python_weather_mailer/emails.txt'
    emails = {}
    email_file = open(file,'r')

    for line in email_file:
        (email, name) = line.split(',')
        emails[email] = name.strip()


    return emails
