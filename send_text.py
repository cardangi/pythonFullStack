from twilio.rest import TwilioRestClient

account_sid =  "ACf8ee97e818fe9a1de4c68730c2bfdcab"
# Your Account SID from www.twilio.com/console
auth_token  = "751b26064a52d9d118dd10bfb95cc171"
# Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello cucker",
    to="+17818887939",    # Replace with your phone number
    from_="7816074467") # Replace with your Twilio number

print(message.sid)
