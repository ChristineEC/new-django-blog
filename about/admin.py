from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, CollaborateRequest


# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    **Context**
    Provides a rich text formatting field (a summernote fiels
    in the admin panel for drafting the content of the about page.
    ``content``
        An individual instance of :model:`about.Content`.
    """
    summernote_fields = ('content',)

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    ***Context**
    Displays in the admin panel a list of messages received
    ``message``
        A single message related to :model:
        `CollaborateRequest.message` received through 
        :form: `CollaborateForm`
    ``read``
        Field included in admin panetl so
        superuse has the ability to mark messages
        as read
    """
    list_display = ('message', 'read',)
