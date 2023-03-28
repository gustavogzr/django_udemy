from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100,required=True)
    email = forms.EmailField(label='E-mail', max_length=100, required=True)
    assunto = forms.CharField(label='Assunto', max_length=120, required=True)
    mensagem = forms.CharField(label='Mensagem',widget=forms.Textarea, required=True)