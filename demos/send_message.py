import os
from africastalking import AfricasTalking, AfricasTalkingException

username = os.environ['AFRICASTALKING_USERNAME']
apikey = os.environ['AFRICASTALKING_APIKEY']

africastalking = AfricasTalking(username, apikey)

details = {'to': '+254727843600', 'message': 'hi there!'}


try:
    response = africastalking.send_message(details)
    print response
except AfricasTalkingException as e:
    print 'Encountered an error while sending airtime: %s' % str(e)