# Bitbucket2GitHub

Bitbucket2GitHub is a simple tool to migrate your Bitbucket repositories to GitHub

## Usage

```
$ pip install bitbucket2github
$ bitbucket2github --github-token=TOKEN --github-organization=ORGANIZATION --github-team=TEAM --bitbucket-username=USER --bitbucket-password=SECRET --bitbucket-organization=ORG -v
```

```
$ bitbucket2github --help
Usage: bitbucket2github [OPTIONS]

Options:
  --github-token TEXT            Your Github Personal access token  [required]
  --github-organization TEXT     The Github organization to import the repository to
  --github-team TEXT             The Github team under the organization
  --bitbucket-username TEXT      Your Bitbucket Username  [required]
  --bitbucket-password TEXT      Your Bitbucket Password  [required]
  --bitbucket-organization TEXT  Your Bitbucket Organization
  -v, --verbose
  --help                         Show this message and exit.
```
