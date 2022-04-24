from django.shortcuts import render, redirect
from django.contrib import messages
from . import dict
from . client import RestClient
# Create your views here.


def search(request):
    if request.method == "POST":
        client = RestClient()
        post_data = {}
        keyword = request.POST.get("keyword")
        # keyword = input("Enter: ")
        print(keyword)
        post_data[len(post_data)] = {
            "language_code": "en",
            "location_code": 2840,
            "keyword": keyword
        }
        response = client.post(
            "/v3/serp/google/organic/live/advanced", post_data)
        if response["status_code"] == 20000:
            items = response['tasks'][0]['result'][0]['items']
            i = 0
            count = 0
            while count < 10:
                if "title" not in items[i] or ("image" or "video") in items[i]["type"]:
                    del items[i]
                    i = i+1
                else:
                    i = i+1
                count = count+1
            for i in range(10, len(items)):
                del items[10]
            return render(request, "serp-fetched.html", {'items': items})
        else:
            messages.error(
                request, f"{response['status_code']} {response['status_message']}")
            return redirect("serp")

    else:
        return render(request, "serp-call.html")
