from django.shortcuts import render, redirect
from onpage.reqhandler import reqhandler
from .reqhandler import reqhandler
from . import dictsimplifier
from . import dictfilter
import json


def home(request):
    content = {
        "title": "Home",
    }
    return render(request, "onpage/search.html", {'content': content})


def result(request):
    if request.method == "POST":
        form = request.POST
        url = form.get("url")   # Url from home page

        # with open("C:\\Users\\nazib\\python\\SEOApp\\onpage\\onpage.json", "r") as onpagefile:
        #     returnedDict = json.load(onpagefile)

        returnedDict = reqhandler({"url": url})
        simplifiedDict = dictsimplifier.simplify(returnedDict)
        filteredDict = dictfilter.filterRequired(simplifiedDict)
        print(len(filteredDict))

        # content = {
        #     "title": "Result",
        #     "items": filteredDict
        # }
        return render(request, "onpage/result.html", {'dict': filteredDict})
    return redirect("/onpage")
