import os
# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

# Specify your login credentials
username = os.environ['AFRICASTALKING_USERNAME']
apikey = os.environ['AFRICASTALKING_APIKEY']

# Specify an array of dicts to hold the recipients and the amount to send
recipients = [{"phoneNumber" : "+254727843600", 
               "amount"      : "KES 10"}]
# Create a new instance of our awesome gateway class
gateway    = AfricasTalkingGateway(username, apikey)

try:
    # Thats it, hit send and we'll take care of the rest. 
    responses = gateway.sendAirtime(recipients)
    for response in responses:
        print "phoneNumber=%s; amount=%s; status=%s; discount=%s; requestId=%s" % (
                                                                       response['phoneNumber'],
                                                                       response['amount'],
                                                                       response['status'],
                                                                       response['discount'],
                                                                       response['requestId']
                                                                      )

except AfricasTalkingGatewayException as e:
    print 'Encountered an error while sending airtime: %s' % str(e)