from django.contrib import admin

# Register your models here.
from .models import Connection, Token, Log, DedupKey, Audit
admin.site.register(Connection)
admin.site.register(Token)  
admin.site.register(Log)
admin.site.register(DedupKey)
admin.site.register(Audit)
