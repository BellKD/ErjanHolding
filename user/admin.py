from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from user.models import MyUser

class MyUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'username')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    model = MyUser
    list_display = ('email', 'username', 'role', 'is_admin')
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
