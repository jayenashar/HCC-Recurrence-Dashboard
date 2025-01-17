"""
    Django HCC dashboard views
"""
from django.shortcuts import render

from .app import *  # pylint: disable=unused-wildcard-import,wildcard-import


def index(request):
    """Function to direct to HCC dashboard view

    Args:
        request (HttpRequest): HTTP request to access the view

    Returns:
        HttpResponse: HTTP reponse regarding the access to the view
    """
    return render(request, "hcc/dashboard.html", None)
