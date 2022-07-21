""" The docstrings were only generetad to be in accordance to pylint. Its importance is known
but it is no the focus on this moment and will be refactored in the future"""

# TODO: REFACTOR DOCSTRINGS FROM THE WHOLE PROJECT
from django.shortcuts import render


def login(request):
    """login"""
    return render(request, "account/login.html")


def logout(request):
    """logout"""
    return render(request, "account/logout.html")


def register(request):
    """register"""
    return render(request, "account/register.html")


def dashboard(request):
    """dashboards"""
    return render(request, "account/dashboard.html")
