from django.shortcuts import render, redirect
from django.contrib import messages
from . client import RestClient


def domain_finder(link):
    import string
    dot_splitter = link.split('.')
    seperator_first = 0
    if '//' in dot_splitter[0]:
        seperator_first = dot_splitter[0].find('//')+2
    seperator_end = ''
    for i in dot_splitter[2]:
        if i in string.punctuation:
            seperator_end = i
            break
    if seperator_end:
        end_ = dot_splitter[2].split(seperator_end)[0]
    else:
        end_ = dot_splitter[2]

    domain = [dot_splitter[0][seperator_first:], dot_splitter[1], end_]
    domain = '.'.join(domain)
    return domain


def search(request):
    # try:
    if request.method == "POST":
        client = RestClient()
        post_data = {}
        keyword = request.POST.get("keyword")
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
            # while count < 10:
            #     if "title" not in items0[i] or "organic" not in items0[i].values():
            #         i = i+1
            #         continue
            #     else:
            #         items.append(items0[i])
            #         i = i+1
            #         count = count+1

            for i in range(0, 50):
                if count < 10:
                    if items0[i]['type'] == 'organic' or items0[i]['type'] == 'video':
                        if items0[i]['type'] == 'video':
                            for it in range(0, len(items0[i]['items'])):
                                idict = {
                                    'type': 'video', 'rank_group': it+1, 'rank_absolute': str(items0[i]['rank_absolute'])+'-'+str(it+1), 'domain': domain_finder(items0[i]['items'][it]['url']), 'title': items0[i]['items'][it]['title'], 'description': 'This video is published by '+items0[i]['items'][it]['source'], 'url': items0[i]['items'][it]['url']}
                                items.append(idict)
                                # print("\n\n", items0[i]['items'][it]['title'])
                        else:
                            items.append(items0[i])
                        count = count+1
                    else:
                        continue

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
            return redirect("result0")
        else:
            messages.error(
                request, f"{response['status_code']} {response['status_message']}")
            return redirect("/serp")
    else:
        return render(request, "serp-call.html")
    # except:
    #     return redirect("/serp")


def result(request):
    try:
        return render(request, "serp-fetched.html", {'items': items})
    except:
        return redirect("/serp")
