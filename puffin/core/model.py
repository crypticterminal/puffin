from ..util import truncate
from flask.ext.security import UserMixin
from enum import Enum


class User(UserMixin):
    
    def __init__(self, login, name, email, password, active, roles):
        self.login = login
        self.name = name
        self.email = email
        self.password = password
        self.active = active
    
    @property
    def id(self):
        return self.user_id

    @property
    def roles(self):
        return []

    @roles.setter
    def roles(self, role):
        pass

class SystemUser:
    
    def __init__(self, login):
        self.login = login

PUFFIN_USER = SystemUser("puffin")


class Application:
    
    def __init__(self, application_id, path, name, logo, description, compose):
        self.application_id = application_id
        self.path = path
        self.name = name
        self.logo = logo
        self.description = description
        self.compose = compose

    @property
    def short_description(self):
        short_description = self.description
        index = self.description.find('\n')
        if index >= 0:
            short_description = short_description[0:index]
        return short_description

    @property
    def logo_url(self):
        return "/static/applications/" + self.application_id + "/" + self.logo


class ApplicationStatus(Enum):
    DELETED = 0
    CREATED = 10
    UPDATING = 20
    ERROR = 90


class Machine:
    
    def __init__(self, base_url, tls_config=None):
        self.base_url = base_url
        if tls_config:
            tls_config.assert_hostname = False
        self.tls_config = tls_config

