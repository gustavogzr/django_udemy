from django import forms
from django.core.mail.message import EmailMessage

class ContactForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100,required=True)
    email = forms.EmailField(label='E-mail', max_length=100, required=True)
    assunto = forms.CharField(label='Assunto', max_length=120, required=True)
    mensagem = forms.CharField(label='Mensagem',widget=forms.Textarea, required=True)

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
        mail = EmailMessage(
            subject='E-mail enviado pelo Projeto Django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br',],
            headers={'Reply-To': email},
        )
        mail.send()
        