import mechanize # pip install mechanize
# www.youtube.com/c/pythonlife
# www.youtube.com/c/riadhcoding
br = mechanize.Browser()
br.set_handle_equiv( True )
br.set_handle_gzip( True )
br.set_handle_redirect( True )
br.set_handle_referer( True )
br.set_handle_robots( False )
br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
url = "http://mbasic.facebook.com/login.php"
br.open(url)
br.select_form(nr=0)
br.form['email'] = 'your email'
br.form['pass'] = 'your password'
response = br.submit() # print(response)
# https://mbasic.facebook.com/login/save-device/  for login successfully
if 'save-device' in response.geturl():
    print('login successfully')
# https://mbasic.facebook.com/login/?email=       for Wrong password
else:
    print('wrong Id or Password')



