import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twdp.settings')

import django
django.setup()
from rango.models import Category, Page


def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
        "url":"http://docs.python.org/2/tutorial/", "views":5},
        {"title":"How to Think like a Computer Scientist",
        "url":"http://www.greenteapress.com/thinkpython/", "views":15},
        {"title":"Learn Python in 10 Minutes",
        "url":"http://www.korokithakis.net/tutorials/python/", "views":35}
        ]
    django_pages = [
        {"title":"Official Django Tutorial",
        "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
        "views":25},
        {"title":"Django Rocks",
        "url":"http://www.djangorocks.com/", "views":50},
        {"title":"How to Tango with Django",
        "url":"http://www.tangowithdjango.com/", "views":51}
        ]
    other_pages = [
        {"title":"Bottle",
        "url":"http://bottlepy.org/docs/dev/", "views":52},
        {"title":"Flask",
        "url":"http://flask.pocoo.org", "views":56}
        ]
    cats = {"Python": {"pages": python_pages, "views": 128, "likes" : 64},
        "Django": {"pages": django_pages, "views": 64, "likes" : 32},
        "Other Frameworks": {"pages": other_pages, "views": 32, "likes" : 16}
        }


    for cat, cat_data in cats.items():
        c = add_cat(cat, cats[cat]["views"], cats[cat]["likes"])
        for p in cat_data["pages"]:
                add_page(c, p["title"], p["url"], p["views"])
        # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))
def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p
def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print("Starting Rango Population script...")
    populate()
