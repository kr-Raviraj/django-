from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.contrib.auth import authenticate

class LoginView(App2View):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"})


