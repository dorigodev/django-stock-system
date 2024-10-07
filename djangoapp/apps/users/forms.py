from django import forms
class registerForm(forms.Form):
    store_name = forms.CharField(
        label='Nome da Loja',
        required=True,
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Digite o nome da sua loja'})
    )

    store_email = forms.EmailField(
        label='Email da loja',
        required=True,
        max_length=70,
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Digite o e-mail da sua loja'})
    )

    store_password = forms.CharField(
        label='Senha para acesso do painel da sua loja',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Digite sua senha'})
    )

    store_password_confirmation = forms.CharField(
        label='Digite novamente a senha para acesso do painel',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Digite sua senha novamente'})

    )
    def clean_store_password_confirmation(self):
        password1 = self.cleaned_data['store_password']
        password2 = self.cleaned_data['store_password_confirmation']
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Senhas diferentes uma da outra, verifique novamente')
            else:
                return password2

class loginForm(forms.Form):
    store_email_login = forms.EmailField(
        label='Email da loja',
        required=True,
        max_length=70,
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Digite o e-mail da sua loja'})
        )

    store_password_login = forms.CharField(
        label='Senha para acesso do painel da sua loja',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Digite sua senha'})
        )
