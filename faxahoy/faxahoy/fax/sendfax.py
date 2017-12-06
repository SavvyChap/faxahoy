from twilio.rest import Client
from datetime import datetime

account_sid = "AC83e3c0d39086dfbc88a3be57c9d53639"
auth_token = "1c71b2ee9b00f1d7855aa6bc164c2c06"

time = datetime.now().strftime("%Y%m%d_%I%M%p")

client = Client(account_sid, auth_token)

fax = client.fax.v1.faxes.create(
    from_="----",
    to="----",
    media_url="https://www.twilio.com/docs/documents/25/justthefaxmaam.pdf")

print(fax.sid + " - " + time)
