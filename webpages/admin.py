from django.contrib import admin
from . models import Contact, Career, Hero, Team, OfficialSocialHandles, Testimonal
from django.utils.html import format_html
from . models import CareerForm
# Register your models here.


class AdminTeam(admin.ModelAdmin):
    def image(self, object):
        return format_html('<img src ="{}" width="40"/>'.format(object.photo.url))
    list_display = ('id', 'name', 'image', 'created_date')
    list_display_links = ('id', 'name')


class AdminContact(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'created_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    list_filter = ('name',)


class AdminCareer(admin.ModelAdmin):
    def image(self, object):
        return format_html('<img src ="{}" width="40"/>'.format(object.photo.url))
    list_display = ('id', 'name', 'image', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class AdminCareerForm(admin.ModelAdmin):
    list_display = ('id', 'first_Name', 'email', 'phone_number', 'position')
    list_display_links = ('id', 'first_Name')


class AdminOfficialSocialHandles(admin.ModelAdmin):
    list_display = ('id', 'fb', 'insta', 'whatsapp')
    list_display_links = ('id', )


class AdminTestimonal(admin.ModelAdmin):
    def image(self, object):
        return format_html('<img src ="{}" width="40"/>'.format(object.photo.url))
    list_display = ('id', 'name', 'image', 'position', 'created_date')
    list_display_links = ('id', 'name', 'image')


admin.site.register(Testimonal, AdminTestimonal)
admin.site.register(OfficialSocialHandles)
admin.site.register(CareerForm, AdminCareerForm)
admin.site.register(Team, AdminTeam)
admin.site.register(Hero)
admin.site.register(Contact, AdminContact)
admin.site.register(Career, AdminCareer)
