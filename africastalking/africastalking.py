import json
import urllib
import urllib2


class AfricasTalkingException(Exception):
    pass


class AfricasTalking(object):
    def __init__(self, username, apikey):
        self.username = username
        self.apikey = apikey

        self.airtime_url = 'https://api.africastalking.com/version1/airtime'

    def send_airtime_url(self):
        return self.airtime_url + '/send'

    def send_africastalking_request(self, url, data):
        try:
            if data is not None:
                data = urllib.urlencode(data)
                request = urllib2.Request(url, data)
            else:
                request = urllib2.Request(url)

            request.add_header('Accept', 'application/json')
            request.add_header('apikey', self.apikey)

            response = urllib2.urlopen(request)
        except Exception as e:
            raise AfricasTalkingException(str(e))
        else:
            return response

    def send_airtime(self, recipients):
        data = {'username': self.username, 'recipients': json.dumps(recipients)}

        response = self.send_africastalking_request(self.send_airtime_url(), data)
        response_data = json.loads(response.read())
        if response.getcode() == 201:
            if len(response_data['responses']):
                return response_data['responses']
            raise AfricasTalkingException(response_data['errorMessage'])
        raise AfricasTalkingException(response)