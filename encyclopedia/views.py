from django.shortcuts import render

from . import util
from markdown2 import Markdown
from django import forms

def md2html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry_content(request,title):
    return render(request, "encyclopedia/entry_content.html",{
        "content": md2html(title),
        "title": title
        }),title
def search(request):
    if request.method == "POST":
        entry_search= request.POST['q']
        html_content = md2html(entry_search)
        if html_content is not None:
            return render(request,"encyclopedia/entry_content.html",{
                "title": entry_search,
                "content": html_content
                })
        else:
            entries = util.list_entries()
            recommends = []
            for title in entries:
                if entry_search.lower() in title.lower():
                    recommends.append(title)
            return render(request,"encyclopedia/recommend.html",{
                "recommends": recommends
            })
def create_newpage(request):
    if request.method == "GET":
        return render(request,"encyclopedia/newpage.html")
    else:
        title = request.POST['new_title']
        content = request.POST['new_content']
        titleExists = util.get_entry(title)
        if titleExists is None:
            return render(request,"encyclopedia/error.html",{
                "message": "Missing title/content!"
                })
        elif title.capitalize() in util.list_entries():
            return render(request,"encyclopedia/error.html",{
                "message": "This title already exists!"
                })
        
        else:
            util.save_entry(title,content)
            return render(request,"encyclopedia/entry_content.html",{
                "title": title,
                "content": Markdown().convert(content)
            })
# def edit(request):
#     if request.method == "POST":
#         title = request.POST['entry_title']
#         old_content = util.get_entry(title)
#         return render(request,"encyclopedia/edit.html",{
#             "title":title,
#             "placeholder": old_content
#         })
