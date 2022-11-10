import re

from rest_framework.exceptions import ValidationError


class MixinValidatorUsername:

    def validate_username(self, value):
        if value.lower() == 'me':
            raise ValidationError('Username не должно быть "me"')
        if not re.match(r'^[\w.@+-]+$', value):
            raise ValidationError('Username содержит недопустимые символы')
        return value
