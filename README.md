WG-Gesucht-Updater-Bot
=====================

## Installation

First, you need to clone the repository. You need Google Chrome for the script to work, so make sure you have it
installed.

Second, you need to download [ChromeDriver](http://chromedriver.chromium.org/downloads), if you haven't already. Do make
sure you get the right version for your version of Chrome, e.g., Chrome version 92.

You can use `brew` to install it on macOS: `brew install chromedriver`.

Third, you'll need selenium so python can automate chrome via ChromeDriver. For this you simply
type `pip3 install selenium` into a command prompt and hit enter.

The last thing you'll need to do is rename the `config-sample.ini` file to `config.ini` and change the fields
accordingly.

## Config

### [account]

Just replace `username` and `password` with your login information.

### [setup]

Here you change the value of `interval` to how often you want your listings to be updated. This value is measured in
seconds, so, e.g., if you want them to be updated every hour change this to `interval = 3600`

### [chromedriver]

Change the `path` to where you stored the `chromedriver` (macOS) respectively `chromedriver.exe` (Windows) executable on your computer. This is defaulted
to `/opt/homebrew/bin/chromedriver`. Keep in mind that if you move the executable afterwards, you'll have to
adjust the path again.

### [listings]

Here you can add as many listings as you like. Naming does not affect the code. Simply copy and paste your listing url
to a variable, e.g., `url1 = https://www.wg-gesucht.de/angebot-bearbeiten.html?action=update_offer&offer_id=12345678`. Remove the lines you don't need of course.
You have to extract the numeric `offer_id` from the URL of your advert.

## Usage

Simply execute the `wg-gesucht-bot.py` file. You'll see a python terminal that shows some information, e.g., when it last
updated your listings. You cannot move that file out of the folder, but you can always create a shortcut to your desktop
or anywhere you like.