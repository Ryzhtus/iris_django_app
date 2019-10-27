from django import forms


class IrisForm(forms.Form):
    sepal_length = forms.FloatField(label='Sepal Length', widget=forms.NumberInput(attrs={'type': 'range', 'value': 5.4,
                                                                                          'step': 0.1, 'min': 4.3,
                                                                                          'max': 7.9, 'class': 'form-control'}))
    sepal_width = forms.FloatField(label='Sepal Width', widget=forms.NumberInput(attrs={'type': 'range', 'value': 3.7,
                                                                                        'step': 0.1, 'min': 2.0,
                                                                                        'max': 4.4, 'class': 'form-control'}))
    petal_length = forms.FloatField(label='Petal Length', widget=forms.NumberInput(attrs={'type': 'range', 'value': 1.5,
                                                                                          'step': 0.1, 'min': 1.0,
                                                                                          'max': 6.9, 'class': 'form-control'}))
    petal_width = forms.FloatField(label='Petal Width', widget=forms.NumberInput(attrs={'type': 'range', 'value': 0.2,
                                                                                        'step': 0.1, 'min': 0.1,
                                                                                        'max': 2.5, 'class': 'form-control'}))