from django.shortcuts import render, redirect
from django.contrib import messages
from . client import RestClient


def search(request):
    try:
        if request.method == "POST":
            client = RestClient()
            post_data = {}
            keyword = request.POST.get("keyword")
            print(keyword)
            post_data[len(post_data)] = {
                "language_code": "en",
                "location_code": 2840,
                "keyword": keyword
            }
            response = client.post(
                "/v3/serp/google/organic/live/advanced", post_data)
            if response["status_code"] == 20000:
                global items0, items
                items = []
                items0 = response['tasks'][0]['result'][0]['items']
                i = 0
                count = 0
                while count < 10:
                    if "title" not in items0[i] or "organic" not in items0[i].values():
                        i = i+1
                        continue
                    else:
                        items.append(items0[i])
                        i = i+1
                        count = count+1
                # items = [titems for i in range(0, 10)]
                # print(items)
                # i = 0
                # count = 0
                # while count < 10:
                #     if "title" not in items[i] or "organic" not in items[i].values():
                #         del items[i]
                #         i = i+1
                #     else:
                #         i = i+1
                #     count = count+1
                # for i in range(10, len(items)):
                #     del items[10]
                return redirect("result")
            else:
                messages.error(
                    request, f"{response['status_code']} {response['status_message']}")
                return redirect("/serp")
        else:
            return render(request, "serp-call.html")
    except:
        return redirect("/serp")


def result(request):
    try:
        return render(request, "serp-fetched.html", {'items': items})
    except:
        return redirect("/serp")
