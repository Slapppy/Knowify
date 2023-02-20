from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from forms import CreateUserForm



def main(request):
    return render(request, 'source/registration.html')


class RegistrationView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, "source/registration.html", {"form": form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            storage = messages.get_messages(request)
            self.clear_messages(storage)
            messages.success(request, "Вы успешно зарегистрировались")
            return redirect("auth")
        else:
            storage = messages.get_messages(request)
            self.clear_messages(storage)
            messages.error(request, "Ошибка регистрации")
        context = {"form": form}
        return render(request, "source/registration.html", context)

    def clear_messages(self, storage):
        for _ in storage:
            pass
        if len(storage._loaded_messages) == 1:
            del storage._loaded_messages[0]
