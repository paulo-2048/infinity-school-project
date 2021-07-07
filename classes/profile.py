class Profile:
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password


class NewProfile(Profile):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)


class ExistentProfile(Profile):
    def __init__(self, email, password):
        super().__init__(email, password)
