# Rosterizer: a Braindump roster generator.

Making the braindump roster by hand sucks. I did it once. Now no one has to do it!

## Usage

1. Clone repo.
2. `pip install --user -r requirements.txt` (or virtualenv or whatever).
3. Rename `example-secrets.yaml` to `secrets.yaml` and update it:
 * Add the Chronicle bot user's API key.
 * Add the real project name. (Make sure the bot has wiki edit permissions on the project.)
4. Rename `example-config.yaml` to `config.yaml` and update it.
5. Add a CSV to the bot's directory where each line is of the form "Full Name,username" (see test_zombies.csv for an example).
6. `./rosterizer.py`

## Caveats

The Redmine API doesn't yet support file uploading, so you still have to upload images by hand. For now.
