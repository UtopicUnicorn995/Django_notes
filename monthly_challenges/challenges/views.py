from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

# Create your views here.

# STATIC VIEWS

# def january(request):
#     return HttpResponse("This works!")
# # Django has no Idea when this function is called or should be called

# def february(request):
#     return HttpResponse('Walk for at least 20 minutes everyday!')

# def march(request):
#     return HttpResponse('Walk for at least 20 minutes everyday!')

# def april(request):
#     return HttpResponse('Walk for at least 20 minutes everyday!')

# def may(request):
#     return HttpResponse('Walk for at least 20 minutes everyday!')

# def june(request):
#     return HttpResponse('Walk for at least 20 minutes everyday!')

# def july(request):
#     return HttpResponse('Walk for at least 20 minutes everyday!')

# def august(request):
#     return HttpResponse('Walk for at least 20 minutes everyday!')

# def september(request):
#     return HttpResponse('Walk for at least 20 minutes everyday!')

# def october(request):
#     return HttpResponse('Walk for at least 20 minutes everyday!')

# def november(request):
#     return HttpResponse('Walk for at least 20 minutes everyday!')

# def december(request):
#     return HttpResponse('Walk for at least 20 minutes everyday!')


monthly_challenges = {
    "january": "Eat no meat for 20 days",
    "february": "Walk for at least 20 minutes everyday!",
    "march": "Fuck 2 times per day for 20 days",
    "april": "Sleep 8 hours per day",
    "may": "I dont know",
    "june": "Eat no meat for 20 days",
    "july": "Walk for at least 20 minutes everyday!",
    "august": "Fuck 2 times per day for 20 days",
    "september": "Sleep 8 hours per day",
    "october": "I dont know",
    "november": "No nut november",
    "december": None, #"I dont know december",
}

# DYNAMIC VIEWS

# def monthly_challenges(request, month):
#     challenge_text = None
#     if month == "january":
#         challenge_text = "Eat no meat for 20 days"
#     elif month == "february":
#         challenge_text = "Walk for at least 20 minutes everyday!"
#     elif month == "march":
#         challenge_text = "Fuck 2 times per day for 20 days"
#     else:
#         return HttpResponseNotFound("This month is not supported!")
#     return HttpResponse(challenge_text)


def index(request):
    months = list(monthly_challenges.keys())
    # list_items = ""
    # for month in list(monthly_challenges.keys()):
    #     index_path = reverse("month-challenge")
    #     list_items += f"<li><a href='{index_path}{month}'>{month.capitalize()}</a></li>"
        
        
    # response_data = f"<ul>{list_items}</ul>"
    
    # response_data = f"""
    # <ul>{list_items}</ul>
    # """
    
    # return HttpResponse(response_data)

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    print(months)
    if month < 1 or month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]

    # /challenge/january -> check the name argument of the function
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string("challenges/challenge.html")
        # Above is a long cut version
        
        # with_html = f"<h1>{challenge_text}</h1>"
        # return HttpResponse(response_data)
        print(request)
        print('fucker')
        return render( request ,"challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("<h1>This is not a valid Date</h1>")
