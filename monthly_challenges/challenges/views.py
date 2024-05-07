from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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
    "october": "I dont know"
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


def monthly_challenge(request, month):
    try:
        # challenge_text = monthly_challenges[month]
        return HttpResponse(monthly_challenges[month])
    except:
        return HttpResponseNotFound("This month is not supported")