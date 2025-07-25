from django.shortcuts import render
from django.views import View
from allauth.socialaccount.models import SocialAccount


class MainView(View):
    template_name = "main_login.html"

    def get(self, request):
        context = {}
        if request.user.is_authenticated:
            account = SocialAccount.objects.get(user=request.user)
            context = {"account": account}
        return render(request, self.template_name, context)
