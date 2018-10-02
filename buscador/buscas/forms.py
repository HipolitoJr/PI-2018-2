from django import forms

class RegistrarBusca(forms.Form):
    url = forms.CharField(required = True)
    keyword = forms.CharField(required = True)
    profundidade = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(RegistrarBusca, self).is_valid():
            self.adiciona_erro('Por favor, verifique a busca informada')
            valid = False

        return valid


    def adiciona_erro(self, message):
        errors = self._errors.setdefault(
            forms.forms.NON_FIELD_ERRORS,
            forms.utils.ErrorList()
        )
        errors.append(message)