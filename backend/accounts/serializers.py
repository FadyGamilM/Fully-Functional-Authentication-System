
from djoser.serializers import UserCreateSerializer

# Since that we have a custom user mode, and here we need to deal 
# with our user model, so this method is how you grap your custom user model 
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
   class Meta(UserCreateSerializer.Meta):
      model=User
      fields=('id', 'email', 'name', 'password')