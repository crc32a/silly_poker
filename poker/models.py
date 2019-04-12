from django.db.models import Model, CharField, BooleanField, FloatField, \
PositiveIntegerField, ForeignKey, TextField, PROTECT, SET_NULL, CASCADE, \
OneToOneField

class Project(Model):
    name = CharField(max_length=32, null=False)
    topic = TextField(max_length=1024, null=True)
    show_votes = BooleanField(null=False, default=True)

class User(Model):
    name = CharField(max_length=32)
    project = ForeignKey(Project, null=True, on_delete=SET_NULL)
    vote = PositiveIntegerField()

class ProjectOwner(Model):
    project = OneToOneField(Project, on_delete=CASCADE)
    user = OneToOneField(User, on_delete=CASCADE)

