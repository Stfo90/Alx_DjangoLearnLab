from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"



class CustomUserManager(BaseUserManager):
    """Custom manager for CustomUser"""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("The Email field must be set"))
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email





# Define your Document model with custom permissions
class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        permissions = [
            ("can_view", "Can view documents"),
            ("can_create", "Can create documents"),
            ("can_edit", "Can edit documents"),
            ("can_delete", "Can delete documents"),
        ]

# Create groups and assign permissions
def assign_permissions():
    # Get ContentType for the Document model
    document_content_type = ContentType.objects.get_for_model(Document)

    # Create Groups
    editors_group, _ = Group.objects.get_or_create(name="Editors")
    viewers_group, _ = Group.objects.get_or_create(name="Viewers")
    admins_group, _ = Group.objects.get_or_create(name="Admins")

    # Get Permissions
    can_view = Permission.objects.get(codename="can_view", content_type=document_content_type)
    can_create = Permission.objects.get(codename="can_create", content_type=document_content_type)
    can_edit = Permission.objects.get(codename="can_edit", content_type=document_content_type)
    can_delete = Permission.objects.get(codename="can_delete", content_type=document_content_type)

    # Assign Permissions to Groups
    editors_group.permissions.add(can_create, can_edit)
    viewers_group.permissions.add(can_view)
    admins_group.permissions.add(can_create, can_edit, can_view, can_delete)

    # Call the function to assign the permissions when you run the script
assign_permissins()
