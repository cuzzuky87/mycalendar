from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import User

#class MyUserChageForm(UserChangeForm):
#    class Meta:
#        model = User
#        fields = '__all__'
#
#
#class MyUserCreationForm(UserCreationForm):
#    class Meta:
#        model = User
#        fields = ('email',)
#
#class MyUserAdmin(UserAdmin):
#    fieldsets = (
#        (None, {'fields': ('email', 'password')}),
#        (_('Personal info'), {'fields': ('display_name',)}),
#        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                        'group', 'user_permissions')}),
#        (_('Importtant dates'), {'fields': ('last_login', 'date_modified', 'date_joined')}),
#    )
#    add_fieldsets = (
#        (None, {
#            'classes': ('wide',),
#            'fields': ('email', 'password1', 'password2'),
#        }),
#    )
#    form = MyUserChageForm
#    add_form = MyUserChageForm
#    list_display = ('email', 'display_name', 'is_staff')
#    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#    search_fields = ('email', 'display_name',)
#    ordering = ('email',)

admin.site.register(User)
