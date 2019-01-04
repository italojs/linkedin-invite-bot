import argparse, time
import random
from linkedin import Linkedin

parser = argparse.ArgumentParser()

parser.add_argument('-e', '--email', help='Your linkedin e-mail', required=True)
parser.add_argument('-p', '--password', help='Your linkedin password', required=True)
parser.add_argument('-k', '--keywords', help='Your search word', required=True)
parser.add_argument('-i', '--initial_page', help='page\'s number where will be started the crawller in search page', default=0)
parser.add_argument('-las', '--last_page', help='Quantity of pages to crawller in search', default=10000)
parser.add_argument('-c', '--chrome_dir', help='path to google chrome bin, example: /bin/google-chrome', default='/bin/google-chrome')
parser.add_argument('-lan', '--language', help='set "pt-br" to portuguese linkedin pages or "en"(default) to english linkedin pages', default='en')
 
args = parser.parse_args()

linkedin = Linkedin()
linkedin.set_chrome_dir(args.chrome_dir)
linkedin.set_language(args.language)

linkedin.login(args.email, args.password)
time.sleep(random.uniform(5,15))

kws = args.keywords.split(',')
for kw in kws:
    try:
        print('-------------------- keyword {} --------------------'.format(kw))
        linkedin.set_keyword(kw)
        for page_number in range(int(args.initial_page),int(args.last_page)+1):
                linkedin.crawller_it_on(page_number)
                time.sleep(random.uniform(5,15))
    except:
        print('Error on {} keyword'.format(kw))
        continue

