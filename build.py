templates = open('templates/top.html').read()
about_me = open('content/blog2.txt').read()
contact = open('content/contact2.txt').read()
content = open('content/blog1.txt').read()
templates = open('templates/bottom.html').read()
html_site = templates + about_me + contact + content + templates
print(html_site)



