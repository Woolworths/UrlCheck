# DO NOT RUN/USE THIS TOOL AS WEB SCRAPING IS ILLEGAL. ONLY FOR EDUCATION PURPOSES
# SEE TESTS.PY FOR USAGE

from urllib.request import urlopen, Request, quote
from urllib.error import URLError
import itertools, random

headers_useragents = []
headers_referers = []

headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')

headers_referers.append('http://www.google.com/?q=')
headers_referers.append('http://www.usatoday.com/search/results?q=')
headers_referers.append('http://engadget.search.aol.com/search?q=')
headers_referers.append('https://duckduckgo.com/?q=')
headers_referers.append('http://www.bing.com/search?q=')
headers_referers.append('http://www.aolsearch.com/search?&query=')
headers_referers.append('http://blekko.com/#?q=')
headers_referers.append('https://www.yandex.com/yandsearch?text=')
headers_referers.append('http://www.checkdomain.com')   

def write_to_file(string, value):
    file = open('./urls.xml', 'a')
    both = str(string) + ', ' + str(value) + '\n'
    file.write(both)
    file.close()
    
def UrlCheck(url):
    url = quote(url) 
    finalurl = 'http://www.checkdomain.com/cgi-bin/checkdomain.pl?domain=%s' % (url)
    # user agent stuff
    req = Request(finalurl)
    req.add_header('User-Agent:', random.choice(headers_useragents))
    req.add_header('Referer:', random.choice(headers_referers))
    req.add_header('Keep-Alive:', str(random.choice(range(1, 6))))
    req.add_header('Connection:', 'close')
    
    try:
        parse = urlopen(req)
        html = parse.read()
        html = str(html)
        
    except URLError as e:
        raise(e)
    
    try:
        if 'has already been registered' in html:
            return False
        elif 'still available' in html:
            return True
    except Exception as e:
        raise(e)

def Combination():
    for s in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=4):
        
        combination = ''.join(s)
        final = combination + '.com'
        
        if UrlCheck(final):
            write_to_file(final, True)
            print(final, True)
        else:
            print(final, False)

def usage():
    print('SEE TESTS.PY FOR USAGE')

if __name__ == '__main__':
    usage()