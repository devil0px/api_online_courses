from django.contrib import admin

# Register your models here.
from courses.models import Lendet,Lesson,Klasa
# Register your models here.

admin.site.register(Lendet)
admin.site.register(Lesson)
admin.site.register(Klasa)