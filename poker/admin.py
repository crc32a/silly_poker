from django.contrib import admin

from .models import User, Project, ProjectOwner

admin.site.register(User)
admin.site.register(ProjectOwner)
admin.site.register(Project)