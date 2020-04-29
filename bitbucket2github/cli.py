import click
import logging
from .processor import Bitbucket2GitHub


def setup_logger(verbose):
    log_level = {
        0: logging.WARNING,
        1: logging.INFO,
        2: logging.DEBUG,
    }.get(verbose, logging.DEBUG)

    logger = logging.getLogger('bitbucket2github')
    logger.setLevel(log_level)

    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)


@click.command()
@click.option('--github-token', help='Your Github Token', required=True)
@click.option(
    '--github-organization',
    help='The organization to import to instead of the user',
)
@click.option(
    '--github-team',
    help='The organization team to give the repository to'
)
@click.option(
    '--bitbucket-username',
    help='Your Bitbucket Username',
    required=True
)
@click.option(
    '--bitbucket-password',
    help='Your Bitbucket Password',
    required=True
)
@click.option('--bitbucket-organization', help='Your Bitbucket Organization')
@click.option(
    '--repos-to-migrate',
    multiple=True,
    help='''
    Repositories you want to migrate. \n
    If not passed, the command will migrate all your repositories. \n
    You can pass this parameter as many times as needed \n
    e.g. --repos-to-migrate=REPO1 --repos-to-migrate=REPO2
    '''
)
@click.option('-v', '--verbose', count=True)
def migrate(
    github_token, github_organization, github_team,
    bitbucket_username, bitbucket_password, bitbucket_organization,
    repos_to_migrate, verbose
):
    setup_logger(verbose)
    b2g = Bitbucket2GitHub(
        github_token, github_organization, github_team,
        bitbucket_username, bitbucket_password, bitbucket_organization,
        repos_to_migrate
    )
    b2g.migrate()


if __name__ == '__main__':
    migrate()
