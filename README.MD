# Linkedin connector bot

It's a linkedin crawller to connect with everyone in a people search

## Install
```
pip install -r requirements.txt
```

## Install chrome driver
in your terminal
```
cd ~
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

```

## Basic usage
```
python bot.py --email='<your_email>' --password='<your_password>' --keyword='<search_word_query>,<other_search_word_query>..."
```

### How it works?
1º - The crawller will login in your linkedin account;<br>
2º - For each keyword the bot wil execute the crawller job;<br>
3º - Scrool the feed page;<br>
4º - Search a keyword;<br>
5º - Connect with the users;<br>

## Full usage
```
python bot.py --email='<your_email>' --password='<your_password>' --keyword='<search_word_query>,<other_search_word_query>,<other_search_word_query>...' --initial_page=<search_page_to_init_crawller> --last_page=<search_page_to_finish_crawller> --chrome_dir='<your_bin_chrome_directory --language='<language>'
```

### Example
```
python bot.py --email='foo@bar.com' --password='f00_B@r123' --keyword='python developer,devops,machine learning engineer' --initial_page=1 --last_page=20 --chrome_dir='/bin/google-chrome-stable' --language='pt-br'
```

### Parameters
To know more about parameters use `python bot.py -h`:

```
usage: bot.py [-h] -e EMAIL -p PASSWORD -k KEYWORDS [-i INITIAL_PAGE]              [-las LAST_PAGE] [-c CHROME_DIR] [-lan LANGUAGE]

optional arguments:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        Your linkedin e-mail
  -p PASSWORD, --password PASSWORD
                        Your linkedin password
  -k KEYWORDS, --keywords KEYWORDS
                        Your search word
  -i INITIAL_PAGE, --initial_page INITIAL_PAGE
                        page's number where will be started the crawller in
                        search page
  -las LAST_PAGE, --last_page LAST_PAGE
                        Quantity of pages to crawller in search
  -c CHROME_DIR, --chrome_dir CHROME_DIR
                        path to google chrome bin, example: /bin/google-chrome
  -lan LANGUAGE, --language LANGUAGE
                        accept pt-br or en(default)
```

## Warnning
- Do not close your browser
- If you want use your machine while the bot work to you, divide your software windows in your screen (left ou right side is the selenium browser, other side is yours softwares)

### Probabily you will need install geckodriver (linux)

#### ARCH LINUX
```
sudo pacman -S geckodriver
```

#### OTHERS LINUX

Go to the geckodriver releases page. Download the latest version of the driver for your platform, example:
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
export PATH=$PATH:/path-to-extracted-file/geckodriver
```