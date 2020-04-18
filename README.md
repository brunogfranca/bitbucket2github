# Bitbucket2GitHub

Bitbucket2GitHub is a simple tool to migrate your Bitbucket repositories to GitHub

## Usage

```
$ pip install bitbucket2github
$ bitbucket2github --github-username=USER --github-password=SECRET --github-owner=OWNER --bitbucket-username=USER --bitbucket-password=SECRET --bitbucket-organization=ORG -v
```

```
$ bitbucket2github --help
Usage: bitbucket2github [OPTIONS]

Options:
  --github-username TEXT         Your Github Username  [required]
  --github-password TEXT         Your Github Password  [required]
  --github-owner TEXT            The owner of the new repository  [required]
  --bitbucket-username TEXT      Your Bitbucket Username  [required]
  --bitbucket-password TEXT      Your Bitbucket Password  [required]
  --bitbucket-organization TEXT  Your Bitbucket Organization
  -v, --verbose
  --help                         Show this message and exit.
```
