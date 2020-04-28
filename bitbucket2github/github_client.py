import logging
from github import Github
from contextlib import suppress


logger = logging.getLogger('bitbucket2github')


class GitHubClient:
    BASE_URL = 'https://api.github.com'

    def __init__(self, token, organization, team):
        self.github = Github(token)
        self.organization = organization
        self.team = team

    def import_repo(self, repo_data, source_username, source_password):
        repo_name = repo_data["name"]
        if self.organization is None:

            user = self.github.get_user()

            with suppress(Exception):
                repo_check = user.get_repo(repo_name)
                if repo_check is not None:
                    logger.info(f'Repository {repo_name} already exists for user')
                    return

            logger.info(f'Creating {repo_name} repository')
            repo = user.create_repo(
                repo_data['name'],
                private=repo_data['is_private']
            )
        else:
            # Do org import
            org = self.github.get_organization(self.organization)

            with suppress(Exception):
                repo_check = org.get_repo(repo_name)
                if repo_check is not None:
                    logger.info(f'Repository {repo_name} already exists in organization {self.organization}')
                    return

            team_id = None
            if self.team is not None:
                for team in org.get_teams():
                    if team.name.lower() == self.team.lower():
                        team_id = team.id
                        break

            logger.info(f'Creating {repo_name} repository in organization {self.organization}')
            repo = org.create_repo(
                repo_data['name'],
                private=repo_data['is_private'],
                team_id=team_id
            )

        logging.info(f'Migrating {repo_name} from Bitbucket')
        repo.create_source_import(
            vcs='git',
            vcs_url=repo_data['url'],
            vcs_username=source_username,
            vcs_password=source_password
        )
