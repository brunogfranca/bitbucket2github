import logging
from github import Github


logger = logging.getLogger('bitbucket2github')


class GitHubClient:
    BASE_URL = 'https://api.github.com'

    def __init__(self, token, organization, team):
        self.github = Github(token)
        self.user = self.github.get_user()
        self.organization = organization
        self.team = team

    def import_repo(self, repo_data, source_username, source_password):
        if self.organization is None:
            logger.info(f'Creating {repo_data["name"]} repository')
            repo = self.user.create_repo(
                repo_data['name'],
                private=repo_data['is_private']
            )
        else:
            # Do org import
            logger.info(f'Creating {repo_data["name"]} repository in organization {self.organization}')
            org = self.github.get_organization(self.organization)

            team_id = None
            if self.team is not None:
                for team in org.get_teams():
                    if team.name.lower() == self.team.lower():
                        team_id = team.id
                        break

            repo = org.create_repo(
                repo_data['name'],
                private=repo_data['is_private'],
                team_id=team_id
            )

        logging.info(f'Migrating {repo_data["name"]} from Bitbucket')
        repo.create_source_import(
            vcs='git',
            vcs_url=repo_data['url'],
            vcs_username=source_username,
            vcs_password=source_password
        )
