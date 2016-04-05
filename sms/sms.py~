from twilio.rest import TwilioRestClient
accountSID = 'ACa65f710b22bf1951e02fc8bfba5f2cdd'
authToken = '8a1f73f2d53efa635ed91edbbc33edc1'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+16162582481'
myCellPhone = '+919778428629'
message = twilioCli.messages.create(body='Mr Pankaj this RRD sir,from CET call me immediately', from_=myTwilioNumber, to=myCellPhone)
