from django.contrib import admin
from .models import hiitbook, hittclasses, PtClasses, SpinClasses

# Register your models here.


admin.site.register(hiitbook)
admin.site.register(hittclasses)
admin.site.register(PtClasses)
admin.site.register(SpinClasses)