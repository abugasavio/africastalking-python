import os
from africastalking.africastalking import AfricasTalking, AfricasTalkingException

username = os.environ['AFRICASTALKING_USERNAME']
apikey = os.environ['AFRICASTALKING_APIKEY']

# Specify an array of dicts to hold the recipients and the amount to send
recipients = [{'phoneNumber': '+254727843600', 'amount': 'KES 10'}]
# Create a new  gateway class
africastalking = AfricasTalking(username, apikey)

try:
    responses = africastalking.send_airtime(recipients)
    for response in responses:
        print response
except AfricasTalkingException as e:
    print 'Encountered an error while sending airtime: %s' % str(e)