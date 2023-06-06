from django import forms

class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=256)
    # description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField()
    model = forms.CharField(max_length=50)

    def save(self, commit):
        pass


class ReviewCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())
