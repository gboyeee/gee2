# Gitlab Scanner Example

Example of scanning Git-repository blobs using [Gitlab's API](https://docs.gitlab.com/ee/api/).

This example will reduce contents from
`requirements.txt` files for all read-accessible repositories by the user
associated with the provided token.


## Usage

First, create a [Gitlab Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) for
a user with sufficient access to the repos you want to scan. The script
configuration is provided via environment variables:
```sh
# set environment variables
# (preferably in .rc or .env file to keep token out of shell history)
export GITLAB_URL=...
export GITLAB_TOKEN=...
```

From here, you should be able to run the script:

```sh
# from host machine (with Python 3 installed)
pip install -r requirements.txt
python main.py
# or with docker-compose
docker-compose run python
```

## Testing
To test using a locally hosted gitlab instance, a `docker-compose` configuration
is provided:

```sh
# start gitlab service
docker-compose up -d
# login via browser/push code to create test data
open http://localhost
# run python-container shell with connectivity to the web service
docker-compose run python
```

Note only the `GITLAB_TOKEN` env-var is required here as the url is defaulted in
the docker-compose configuration.
