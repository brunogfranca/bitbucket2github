# Bitbucket2GitHub

Bitbucket2GitHub is a simple tool to migrate your Bitbucket repositories to GitHub

## Usage

```
$ pip install bitbucket2github
$ bitbucket2github --github-token=TOKEN --github-organization=ORGANIZATION --github-team=TEAM --bitbucket-username=USER --bitbucket-password=SECRET --bitbucket-organization=ORG -v --repos-to-migrate=REPO_NAME_1 --repos-to-migrate=REPO_NAME_2
```

```
$ bitbucket2github --help
Usage: bitbucket2github [OPTIONS]

Options:
  --github-token TEXT            Your Github Token  [required]
  --github-organization TEXT     The organization to import to instead of the
                                 user

  --github-team TEXT             The organization team to give the repository
                                 to

  --bitbucket-username TEXT      Your Bitbucket Username  [required]
  --bitbucket-password TEXT      Your Bitbucket Password  [required]
  --bitbucket-organization TEXT  Your Bitbucket Organization
  --repos-to-migrate TEXT        Repositories you want to migrate.

                                 If not passed, the command will migrate all
                                 your repositories.

                                 You can pass this parameter as many times as
                                 needed

                                 e.g. --repos-to-migrate=REPO1 --repos-to-
                                 migrate=REPO2

  -v, --verbose
  --help                         Show this message and exit.
```
