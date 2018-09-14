from django.contrib.auth import get_user_model
User = get_user_model()


class CustomBackendUser(object):

    @staticmethod
    def authenticate(username=None, password=None):
        try:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_user(user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
        except User.DoesNotExist:
            return None
