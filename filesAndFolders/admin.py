from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from filesAndFolders.models import FileFolder

# Register your models here.

admin.site.register(FileFolder, DraggableMPTTAdmin)
