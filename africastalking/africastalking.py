import json
import urllib
import urllib2


class AfricasTalkingException(Exception):
    pass


class AfricasTalking(object):
    def __init__(self, username, apikey):
        self.username = username
        self.apikey = apikey
        self.apiurl = 'https://api.africastalking.com/version1/'

    def send_airtime_url(self):
        return self.apiurl + 'airtime/send'

    def send_message_url(self):
        return self.apiurl + 'messaging'

    def account_details_url(self):
        return self.apiurl + 'user'

    def send_africastalking_request(self, url, data=None):
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

    def send_message(self, details):
        if not details.get('to') or not details.get('message'):
            AfricasTalkingException('to or message parameters are required.')
        params = {'username': self.username, 'to': details['to'], 'message': details.get('message'), 'bulkSMSMode': 1}

        if details.get('from'):
            params['from'] = details.get('from')

        if details.get('enqueue'):
            params['enqueue'] = details.get('enqueue')

        if details.get('keyword'):
            params['keyword'] = details.get('keyword')

        if details.get('link_id'):
            params['linkId'] = details.get('link_id')

        if details.get('retry_duration'):
            params['retryDurationInHours'] = details.get('retry_duration')

        response = self.send_africastalking_request(self.send_message_url(), params)
        response_data = json.loads(response.read())
        if response.getcode() == 201:
            return response_data
        raise AfricasTalkingException(response)

    def get_account_details(self):
        url = self.account_details_url + '?' + urllib.urlencode({'username': self.username})
        response = self.send_africastalking_request(url)
        response_data = json.loads(response.read())
        if response.getcode() == 200:
            return response_data['UserData']
        raise AfricasTalkingException(response)
