# NOT TO BE USED, ONLY FOR EDUCATIONAL PURPOSES!
from UrlCheck import UrlCheck

# no need for http://
print(UrlCheck('www.urlgoesinhere.com')) # True = avaliable, False = not avaliable

if UrlCheck('www.urlgoesinhere.com'): 
    print('This domain name is avaliable')
# if www.urlgoesinhere.com is avaliable, print: "This domain name is avaliable"