def simple():
    top = open("templates/top.html").read()
    about_me = open("content/blog2.html").read()
    contact = open("content/contact2.html").read()
    content = open("content/blog1.html").read()
    templates = open("templates/bottom.html").read()
    
def apply_template(content):
    return results

def project():
    content = open("project.1/base.html")
    resulting_html_for_base = apply_template(content)
    

def apply_template(value, title):
    template = open("project.1/base.html").read()
    index_html = template.replace("{{content}}", value)
    title_replace = index_html.replace("{{my_blog}}", title)
    return (index_html)
   
def pages():
    for value in pages:
        content = open(value["filename"]).read()
        title = value["title"]
        resulting_html_for_index = apply_template(content, title)
        open(value["output"], "w+").write(resulting_html_for_index)    
        
 
pages = []
def html_output():
    for each in all_html_files:
        file_name = os.path.basename(each)
        name_only, extension = os.path.splitext(file_name)
        
      
        pages.append({
            "filename": each,
            "title": name_only,
            "output": "docs/" + name_only + '.html',
            "link": name_only + '.html',
            "output_filepath": 'docs/' + name_only + '.html'
        })
        
def apply_template():
    for page in pages:
        index_html = open(page['filename']).read()
        template_html = open('templates/base.html').read()
        template = Template(template_html)
        page_output = template.render(
            title=page['title'],
            content=index_html,
            pages=pages,
            )
        open(page["output"], "w+").write(page_output)     
        
  
