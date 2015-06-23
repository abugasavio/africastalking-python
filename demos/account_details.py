import os
from africastalking import AfricasTalking, AfricasTalkingException

username = os.environ['AFRICASTALKING_USERNAME']
apikey = os.environ['AFRICASTALKING_APIKEY']

# Create a new  gateway class
africastalking = AfricasTalking(username, apikey)

try:
    response = africastalking.get_account_details()
    print response
except AfricasTalkingException as e:
    print 'Encountered an error while getting account details: %s' % str(e)