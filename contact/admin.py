from django.contrib import admin
from contact.models import Contact, Categoria

# Recebe como argumento uma classe que criei
# Decora uma classe que personaliza como serão mostrados os contatos na /admin

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', )
    ordering = ('id',)
    search_fields = ('first_name', 'id')
    list_per_page = 10 
    list_max_show_all = 20
    list_editable = ('first_name', 'last_name', 'phone',)
    list_display_links = ('id', )
    

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('name',)

# # Outra forma de fazer, só que sem a personalização
# # admin.site.register(Contact)
# # Outra forma de fazer, com a personalização
# # admin.site.register(Contact, ContactAdmin)
