# Rosterizer: a Braindump roster generator.

Making the braindump roster by hand sucks. I did it once. Now no one has to do it!

## Usage

1. Clone repo.
2. `pip install --user -r requirements.txt` (or virtualenv or whatever).
3. For rosterizer, add a CSV to the bot's directory where each line is of the form "Full Name,username,ImageFile.jpg" (see `example_zombies.csv` for an example).
4. For chroniclizer, add another CSV where each line is of the form "username,password" (their Redmine credentials). See `example_credentials.csv` for an example. It's okay if this isn't exactly the same people as above for whatever reason. We won't be using these for edits.
5. Rename `example_secrets.yaml` to `secrets.yaml` and update it:
 * Add the Chronicle bot user's API key.
 * Add the real project name. (Make sure the bot has wiki edit permissions on the project.)
6. Rename `example_config.yaml` to `config.yaml` and update it with the CSV filenames and anything else you want to change.
7. `./rosterizer.py` will create all the individual zombie pages with the appropriate template and build a roster page that links to them all. It halts if it can't create the roster, and reports any individual page creation failures.
8. `./chroniclizer.py` simply attempts to log in with each set of credentials provided and make no changes. This triggers Redmine to grab the account information from LDAP, making the users available in the administrative interface to grant permissions to.

## Caveats

The Redmine API doesn't yet support file uploading, so you still have to upload images by hand. For now.
