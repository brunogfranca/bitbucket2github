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
@click.option('--github-username', help='Your Github Username', required=True)
@click.option('--github-password', help='Your Github Password', required=True)
@click.option(
    '--github-owner',
    help='The owner of the new repository',
    required=True
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
@click.option('-v', '--verbose', count=True)
def migrate(
    github_username, github_password, github_owner,
    bitbucket_username, bitbucket_password, bitbucket_organization,
    verbose
):
    setup_logger(verbose)
    b2g = Bitbucket2GitHub(
        github_username, github_password, github_owner,
        bitbucket_username, bitbucket_password, bitbucket_organization
    )
    b2g.migrate()


if __name__ == '__main__':
    migrate()
