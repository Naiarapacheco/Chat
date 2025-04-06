from django.core.exceptions import ValidationError
import re

class StrongPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError("A senha deve ter pelo menos 8 caracteres.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("A senha deve conter pelo menos uma letra maiúscula.")
        if not re.search(r'[a-z]', password):
            raise ValidationError("A senha deve conter pelo menos uma letra minúscula.")
        if not re.search(r'[0-9]', password):
            raise ValidationError("A senha deve conter pelo menos um número.")
        if not re.search(r'[@#$%&()^<>]', password):
            raise ValidationError("A senha deve conter pelo menos um caractere especial.")

    def get_help_text(self):
        return (
            "A senha deve conter pelo menos 8 caracteres, incluindo uma letra maiúscula, "
            "uma minúscula, um número e um caractere especial."
        )
