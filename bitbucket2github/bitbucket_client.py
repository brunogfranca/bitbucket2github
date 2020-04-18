import logging
import requests


logger = logging.getLogger('bitbucket2github')


class BitbucketClient:
    BASE_URL = 'https://api.bitbucket.org/2.0/'

    def __init__(self, username, password, organization=None):
        self.username = username
        self.password = password
        self.organization = organization
        self.repos = []

    def get_repositories(self, api_url=None):
        if not api_url:
            api_url = f'{self.BASE_URL}repositories'
            if self.organization:
                api_url = f'{api_url}/{self.organization}'
        logger.info(f'Querying {api_url}')
        result = requests.get(api_url, auth=(self.username, self.password))
        data = result.json()
        self.repos += data['values']
        if 'next' in data:
            return self.get_repositories(data['next'])
        else:
            return self.repos
