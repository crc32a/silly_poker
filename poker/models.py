from django.db.models import Model, CharField, BooleanField, FloatField, \
PositiveIntegerField, ForeignKey, TextField, PROTECT, SET_NULL, CASCADE, \
OneToOneField

class Project(Model):
    name = CharField(max_length=80, null=False)
    topic = TextField(max_length=1024)

class User(Model):
    name = CharField(max_length=32)
    project = ForeignKey(Project, null=True, on_delete=SET_NULL)
    vote = PositiveIntegerField()

class ProjectOwner(Model):
    project = OneToOneField(Project, on_delete=CASCADE)
    user = OneToOneField(User, on_delete=CASCADE)
    #project = ForeignKey(Project, on_delete=CASCADE, unique=True, null=False)
    #user = ForeignKey(User, on_delete=CASCADE, unique=True, null=False)

