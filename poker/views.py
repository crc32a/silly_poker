from django.http import HttpResponse
from django.shortcuts import render
import django.conf
import silly_poker.utils
import pdb
from poker.forms import UserForm

printf = silly_poker.utils.printf

class PokerView(object):
    def gview(self, request, *args, **kw):
        if "view" in kw:
            func = getattr(self, kw["view"])
            self.request = request
            self.session = request.session
            self.ctx = None
            self.get_default_ctx()
            self.form_named = self.get_formname()
            return func()

    def play_poker_view(self):
        self.ctx["login_form"] = UserForm()
        if "logged_in_as" in self.session:
            self.ctx["login_form"].fields["name"].disabled=True
            self.ctx["login_form"].fields["project"].disabled=True
        if self.form_named == "UserForm":
            self.ctx["login_form"] = UserForm(self.request.POST)
            if self.ctx["login_form"].is_valid():
                self.session["logged_in_as"] = self.ctx["login_form"].cleaned_data["name"]
                self.ctx["login_form"].fields["name"].disabled=True
                self.ctx["login_form"].fields["project"].disabled=True
                self.ctx["logged_in_as"] = self.session["logged_in_as"]
        return self.render_my_response("poker/play.html")

    def render_my_response(self, template_file):
        return render(self.request, template_file, self.ctx)

    def get_default_ctx(self):
        if self.ctx is None:
            self.ctx = {}
        if self.get_formname() == "logout":
            self.session.flush()
        if "logged_in_as" in self.request.session:
            self.ctx["logged_in_as"] = self.session["logged_in_as"]
        self.ctx["cards_nrows"] = django.conf.settings.CARDS_NROWS
        self.ctx["cards"] = []
        for i in django.conf.settings.CARDS:
            card = {}
            card["num"] = i
            self.ctx["cards"].append(card)
            

    def get_formname(self):
        request = self.request
        form_name = None
        if request.method == "POST":
          if "form_name" in request.POST:
            form_name = request.POST["form_name"]
          elif "logout" in request.POST:
            form_name = "logout"
        return form_name
    