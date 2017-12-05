from twilio.rest import Client

account_sid = "-----"
auth_token = "-----"

client = Client(account_sid, auth_token)

fax = client.fax.v1.faxes.create(
    from_="----",
    to="----",
    media_url="https://www.twilio.com/docs/documents/25/justthefaxmaam.pdf")

print(fax.sid)
