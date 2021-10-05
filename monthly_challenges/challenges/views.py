from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


# def january(request):
#    return HttpResponse("January!")


# def february(request):
#    return HttpResponse("Febraury!")

""" def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "january"
    elif month == "february":
        challenge_text = "february"
    elif month == "march":
        challenge_text = "march"
    else:
        return HttpResponseNotFound("Not supported")
    return HttpResponse(challenge_text) """


monthly_challenges = {
    "january": "January challenge",
    "february": "February chalenge",
    "march": "March challenge",
    "april": None,
    "may": None,
    "june": None,
    "july": None,
    "august": None,
    "sepetember": None,
    "october": None,
    "november": None,
    "december": None,
}


def index_by_template(request):
    months = list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months": months
    })


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_months = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_months}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenges_by_dict(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Month Not Supported</h1>")


""" def monthly_challenges_by_number(request, month):
    return HttpResponse(month) """


def monthly_challenges_redirect_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Month Not Supported")
    redirect_month = months[month-1]
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    # /challenges/ + redirect_month
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges_by_template(request, month):
    try:
        challenge_text = monthly_challenges[month]
        #response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("<h1>Month Not Supported</h1>")
