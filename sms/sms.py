""" simple python script for sending sms to specified mobile number given   """

from twilio.rest import TwilioRestClient
accountSID = '**************************'
authToken = '***************************'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '**********'
myCellPhone = '*************'
message = twilioCli.messages.create(body='msg', from_=myTwilioNumber, to=myCellPhone)
