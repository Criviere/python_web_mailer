import get_emails
import send_emails
import weather


def main():
    emails = get_emails.get_emails()

    forecast = weather.get_weather_forecast()

    send_emails.send_emails(emails, forecast)

main()
