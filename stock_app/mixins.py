from rest_framework.mixins import CreateModelMixin


# For geting user information via token
class UserMixin(CreateModelMixin):
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
