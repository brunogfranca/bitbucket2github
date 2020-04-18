import logging
from github import Github


logger = logging.getLogger('bitbucket2github')


class GitHubClient:
    BASE_URL = 'https://api.github.com'

    def __init__(self, username, password, owner):
        self.github = Github(username, password)
        self.user = self.github.get_user()
        self.owner = owner

    def import_repo(self, repo_data, source_username, source_password):
        logger.info(f'Creating {repo_data["name"]} repository')
        repo = self.user.create_repo(
            repo_data['name'],
            private=repo_data['is_private']
        )
        logging.info(f'Migrating {repo_data["name"]} from Bitbucket')
        repo.create_source_import(
            vcs='git',
            vcs_url=repo_data['url'],
            vcs_username=source_username,
            vcs_password=source_password
        )
