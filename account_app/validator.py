import re
from django.core.exceptions import ValidationError



class Validator:
    def NationalCode_Validator(value):
        if not re.search(r'^\d{10}$', value):
            raise ValidationError("کد ملی صحیح نیست")
            return False
        check = int(value[9])
        s = sum(int(value[x]) * (10 - x) for x in range(9)) % 11

        if (s < 2 and check == s) or (check + s == 11):
            return True
        else:
            raise ValidationError("کد ملی صحیح نیست")