from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_username, user_email
from django.utils.crypto import get_random_string
import re

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        
        # Generate username from email if available
        email = user_email(user)
        if email:
            # Clean email to create username
            username = re.sub(r'[^\w.@+-]', '', email.split('@')[0])
            username = username[:30]  # Truncate to max_length
        else:
            # Fallback to random string if no email
            username = get_random_string(12)
        
        # Ensure username is unique
        original_username = username
        suffix = 1
        while self._username_exists(username):
            username = f"{original_username}_{suffix}"
            suffix += 1
        
        user_username(user, username)
        return user

    def _username_exists(self, username):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        return User.objects.filter(username=username).exists()
