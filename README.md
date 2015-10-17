# Rosterizer: a Braindump roster generator.

Making the braindump roster by hand sucks. I did it once. Now no one has to do it!

## Usage

1. Clone repo.
2. Rename example-config.py to config.py and update it:
 * Add the Chronicle bot user's API key.
 * Add the real project name. (Make sure the bot has wiki edit permissions on the project.)
3. Add a CSV to the bot's directory where each line is of the form "Full Name,username,ImageFile.jpg" (see test_zombies.csv for an example).
4. `./rosterizer.py`

## Caveats

The Redmine API doesn't yet support file uploading, so you still have to upload images by hand. For now.
