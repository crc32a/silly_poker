from silly_poker import db, app
import flask_session
import silly_poker

flask_session.SqlAlchemySessionInterface(app, db, "sessions", "sess_")

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    topic = db.Column(db.String(4096))
    voters = db.relationship("User", back_populates="project")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    vote = db.Column(db.Integer)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    project = db.relationship("Project", back_populates="voters")

class ProjectOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"),
                           unique=True, nullable=False)
    project = db.relationship("Project")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"),
                        unique=True, nullable=False)
