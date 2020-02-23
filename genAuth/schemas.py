from rest_framework.schemas import AutoSchema
from coreapi import Field

class SSOSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        if (method == "GET"):
            return []
        elif method == "POST":
            return [Field('email'),]

class LoginSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        if (method == "GET"):
            return []
        elif method == "POST":
            return [Field('id', description='user id'), Field('code', description='code from sso login')]

class CreateUserSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        if method == "GET":
            return []
        elif method == "POST":
            return [Field('name'), Field('email'),]

class VerifyUserSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        if method == "GET":
            return []
        elif method == "PUT":
            return [Field('id'), Field('token', description='sent via email'), Field('email')]