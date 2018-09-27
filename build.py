templates = open('templates/top.html').read()
about_me = open('content/blog2.txt').read()
contact = open('content/contact2.txt').read()
content = open('content/blog1.txt').read()
templates = open('templates/bottom.html').read()
html_site = templates + about_me + contact + content + templates
print(html_site)


# 2.1 phase 1
def main():
    top = open("templates/top.html").read()
    about_me = open("content/blog2.txt").read()
    contact = open("content/contact2.txt").read()
    content = open("content/blog1.txt").read()
    templates = open("templates/bottom.html").read()
     
#to invoke
if main =="__main__":
    main()
    
# 2.2 phase 2 

pages = [
    {
        "filename": "content/blog2.txt",
        "output": "content/blog2.txt",
        "title": "About Me",
     },
    {
        "filename": "content/contact2.txt",
        "output": "content/contact2.txt",
        "title": "Contact Me",
     },
     {
        "filename": "content/blog1.txt",
        "output": "content/blog1.txt",
        "title": "Blog",
     },
]

# 2.3 phase 3

start = open("project.1/templates/top.html").read()
end = open("project.1/templates/bottom.html").read()
full = start + end
open("base.html", "w+").write(full)

# 2.4 phase 4

def apply_template(content):
    return results

def main():
    content = open("project.1/base.html")
    resulting_html_for_base = apply_template(content)
    
# 2.5 phase 5

def apply_template(value, title):
    template = open("project.1/base.html").read()
    index_html = template.replace("{{content}}", value)
    title_replace = index_html.replace("{{my_blog}}", title)
    return (index_html)
   
def main():
    for value in pages:
        content = open(value["filename"]).read()
        title = value["title"]
        resulting_html_for_index = apply_template(content, title)
        open(value["output"], "w+").write(resulting_html_for_index)
    
    if __name__ == "__main__":
        main()
    
