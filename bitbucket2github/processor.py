from .bitbucket_client import BitbucketClient
from .github_client import GitHubClient


class Bitbucket2GitHub:
    def __init__(
        self,
        gh_username, gh_password, gh_owner,
        bb_username, bb_password, bb_organization=None,
    ):
        self._setup_github(gh_username, gh_password, gh_owner)
        self._setup_bitbucket(bb_username, bb_password, bb_organization)

    def _setup_bitbucket(self, username, password, organization):
        self.bitbucket_username = username
        self.bitbucket_password = password
        self.bitbucket = BitbucketClient(
            username=username,
            password=password,
            organization=organization
        )

    def _setup_github(self, username, password, owner):
        self.github = GitHubClient(
            username=username,
            password=password,
            owner=owner
        )

    def migrate(self):
        repos = self.bitbucket.get_repositories()
        for repo in repos:
            repo_data = {
                'name': repo['name'],
                'slug': repo['slug'],
                'is_private': repo['is_private'],
                'url': repo['links']['clone'][0]['href']
            }
            self.github.import_repo(
                repo_data,
                self.bitbucket_username,
                self.bitbucket_password
            )
