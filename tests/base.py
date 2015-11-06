# tests/base.py


from flask.ext.testing import TestCase

from project import app, db
from project.models import User


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        adminUser = User(
            email="ad@min.com",
            password="admin_user",
            admin=True
        )
        db.session.add(adminUser)
        teacherUser = User(
            email="teacher@teacher.com",
            password="teacher",
            teacher=True,
            student=False
        )
        db.session.add(teacherUser)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
