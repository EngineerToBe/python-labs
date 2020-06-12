#!/usr/bin/python3 -tt

from twilio.rest import Client


account_sid = "ACff2d970d7hndslkjfhlksdjfh5a93e1eef0f595f0c6a813djhfgskaj"
auth_token = "171936af612d983325eklshdklfghjlskdjfhl041c02a493b96"

client = Client(account_sid, auth_token)


call = client.messages.create(
    to="+911357790",
    from_="+12034968764",
    body="Hello"
)


call1 = client.calls.create(
    to="+911234567890",
    from_="+12034968764"
)

call1.Status
