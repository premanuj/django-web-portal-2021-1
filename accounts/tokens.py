from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class UserTokenGenerator(PasswordResetTokenGenerator):
    def make_hash_value(self, user, timestamp):
        return six.text_type(user.id)+six.text_type(timestamp)+six.text_type(user.is_active)

activation = UserTokenGenerator()

