import esatto.patient.validator as val

import pytest


class TestText:

    @pytest.mark.parametrize('text', ['A8', 'ABC234', 'AB2'])
    def test_matches_regex(self, text):
        regex = r'^[A-Z]+\d+$'

        result = val.Validator.matches_regex(regex, text)

        assert result == True

    @pytest.mark.parametrize('text', ['AaBC234', 'AB', '45', 'AB83B', 'A 4', ])
    def test_not_matches_regex(self, text):
        regex = r'^[A-Z]+\d+$'

        result = val.Validator.matches_regex(regex, text)

        assert result == False

    def test_has_only_upper(self):
        text = 'HELLO WORLD'
        result = val.Validator.has_only_upper(text)

        assert result == True

    def test_has_not_only_upper(self):
        text = 'HELLo wORLd'
        result = val.Validator.has_only_upper(text)

        assert result == False