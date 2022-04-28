from django.shortcuts import render, redirect
from django.contrib import messages
from . client import RestClient
# from . trafdict0 import dict00

# Create your views here.


def search(request):
    # try:
    if request.method == "POST":
        client = RestClient()
        post_data = {}
        website = request.POST.get("website")
        post_data[len(post_data)] = dict(
            target=website
        )
        response = client.post(
            "/v3/traffic_analytics/similarweb/live", post_data)

        if response["status_code"] == 20000:
            dict0 = response["tasks"][0]["result"][0]
            global items, itlist, top_categories, traffic_countries, other_visited_sites, top_topics, similar_sites, source_lite, top_keywords, top_referring, top_socials
            itlist = []
            top_categories = []
            traffic_countries = []
            other_visited_sites = []
            top_topics = []
            similar_sites = []
            source_lite = []
            top_keywords = []
            top_referring = []
            top_socials = []
            items = {}
            items["company_name"] = dict0["company_name"]
            items["site_url"] = dict0["site_url"]
            items["global_rank"] = dict0["global_rank"]["rank"]
            items["country_rank"] = dict0["country_rank"]["rank"]
            items["country_rank_country"] = dict0["country_rank"]["country"]
            items["category_rank"] = dict0["category_rank"]["rank"]
            items["category_rank_category"] = dict0["category_rank"]["category"]
            items["headquater"] = dict0["headquarters"]["country"]
            items["revenue"] = '$' + str(float(dict0["revenue"]["revenue_min"]/1000000)) + \
                'M-$'+str(float(dict0["revenue"]
                                ["revenue_max"]/1000000))+'M'
            items["audience_visits"] = str(
                float(dict0["audience"]["visits"]/1000))+'K'
            items["audience_time_on_site_avg"] = dict0["audience"]["time_on_site_avg"]
            items["audience_page_views_avg"] = dict0["audience"]["page_views_avg"]
            items["audience_bounce_rate"] = dict0["audience"]["bounce_rate"]
            other_visited_sites = dict0["audience"]["other_visited_websites"]
            top_topics = dict0["audience"]["top_topics"]
            items["traffic_value"] = dict0["traffic"]["value"]
            traffic_countries = dict0["traffic"]["countries"]
            top_keywords = dict0["traffic"]["sources"]["search_organic"]["top_keywords"]
            top_referring = dict0["traffic"]["sources"]["referring"]["top_referring"]
            top_socials = dict0["traffic"]["sources"]["social"]["top_socials"]
            source_lite = [
                {
                    "direct_value": dict0["traffic"]["sources"]["direct"]["value"],
                    "direct_percent": str(dict0["traffic"]["sources"]["direct"]["percent"])+'%'
                },
                {
                    "orgsearch_value": dict0["traffic"]["sources"]["search_organic"]["value"],
                    "orgsearch_percent": str(dict0["traffic"]["sources"]["search_organic"]["percent"])+'%'
                },
                {
                    "searchad_value": dict0["traffic"]["sources"]["search_ad"]["value"],
                    "searchad_percent": str(dict0["traffic"]["sources"]["search_ad"]["percent"])+'%'
                },
                {
                    "referrals_value": dict0["traffic"]["sources"]["referring"]["value"],
                    "referrals_percent": str(dict0["traffic"]["sources"]["referring"]["percent"])+'%'
                },
                {
                    "social_value": dict0["traffic"]["sources"]["social"]["value"],
                    "social_percent": str(dict0["traffic"]["sources"]["social"]["percent"])+'%'
                },
                {
                    "displayad_value": dict0["traffic"]["sources"]["display_ad"]["value"],
                    "displayad_percent": str(dict0["traffic"]["sources"]["display_ad"]["percent"])+'%'
                },
                {
                    "mail_value": dict0["traffic"]["sources"]["mail"]["value"],
                    "mail_percent": str(dict0["traffic"]["sources"]["mail"]["percent"])+'%'
                }
            ]
            similar_sites = dict0["sites"]["similar_sites"]

            # items["traffic_value"] = dict0["traffic"]["countries"]
            # items["similar_sites"] = dict0["sites"]["similar_sites"]
            for i in range(0, len(dict0["audience"]["top_categories"])):
                temp = {"title": dict0["audience"]
                        ["top_categories"][i]['title']}
                top_categories.append(temp)
            return redirect("result1")

        else:
            messages.error(
                request, f"{response['status_code']} {response['status_message']}")
            return redirect("/traffic")

    else:
        return render(request, "trafficAPI-call.html")

    # except:
    #     return redirect("/traffic")


def result(request):
    try:
        context = {
            "items": items,
            "top_categories": top_categories,
            "traffic_countries": traffic_countries,
            "other_visited_sites": other_visited_sites,
            "top_topics": top_topics,
            "similar_sites": similar_sites,
            "source_lite": source_lite,
            "top_keywords": top_keywords,
            "top_referring": top_referring,
            "top_socials": top_socials
        }
        return render(request, "trafficAPI-fetched.html", context)
    except:
        return redirect("/traffic")
