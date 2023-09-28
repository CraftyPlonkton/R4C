from django import forms

from .models import Robot


class RobotCreateForm(forms.ModelForm):
    serial = forms.CharField(required=False)

    class Meta:
        fields = ['model', 'version', 'created', 'serial']
        model = Robot

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            cleaned_data['version'] = cleaned_data['version'].upper()
            cleaned_data['model'] = cleaned_data['model'].upper()
            serial = f"{cleaned_data['model']}-{cleaned_data['version']}"
            cleaned_data['serial'] = serial
        return cleaned_data
