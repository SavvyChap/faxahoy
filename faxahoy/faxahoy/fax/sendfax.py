from twilio.rest import Client

account_sid = "AC83e3c0d39086dfbc88a3be57c9d53639"
auth_token = "1c71b2ee9b00f1d7855aa6bc164c2c06"

client = Client(account_sid, auth_token)

fax = client.fax.v1.faxes.create(
    from_="+17132367768",
    to="+13104992491",
    media_url="https://www.twilio.com/docs/documents/25/justthefaxmaam.pdf")

print(fax.sid)
