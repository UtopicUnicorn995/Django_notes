from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.january),
    # # from the path url do something, in this case do the function views.index
    # path("february", views.february),
    # path("march", views.march),
    # path("april", views.april),
    # path("may", views.may),
    # path("june", views.june),
    # path("july", views.july),
    # path("august", views.august),
    # path("september", views.september),
    # path("october", views.october),
    # path("november", views.november),
    # path("december", views.december),
# DYNAMIC URL
    path("", views.index, name="month-challenge"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
    # path("<str:month>", views.monthly_challenges) this means you have a strictly string argument -> int: number
    # "<month>" placeholder which can be used as the identifier/argument of a views.monthly_challenges function
]