from django.contrib.auth.models import User


def create_user(username, email, password, first_name='', last_name=''):
    user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
    user.save()
    return user
