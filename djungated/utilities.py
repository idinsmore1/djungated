import re
from django.conf import settings
import os
from json import load
from difflib import get_close_matches


class SearchText:
    with open(os.path.join(settings.BASE_DIR, 'static/json/ungated_phenotypes.json')) as f:
        phenotypes = load(f)

    def __init__(self, text: str):
        # Change the text to standard formats
        # self.phenotypes = SearchText.phenotypes
        self.text = text.replace(',', '').replace('-', ':').replace('.', '_')
        self.is_variant = self._check_variant(self.text)
        if self.is_variant:
            self.response = self.text
            self.is_phenocode = False
            self.is_phenostring = False
        else:
            self.is_phenocode = self._check_phenocode(self.text)
            if self.is_phenocode:
                self.is_phenostring = False
                if self.text in self.phenotypes.values():
                    self.response = self.text
                else:
                    self.response = self._get_phenocode(self.text)
            else:
                self.is_phenostring = self._check_phenostring(self.text)
                if self.is_phenostring:
                    self.is_phenocode = False
                    self.response = self._get_phenocode(self.text)
                else:
                    self.response = None

    @staticmethod
    def _check_variant(text):
        # Check if text is a variant
        regex = re.compile(r'(\d+):(\d+):[ACTGactg]+:[ACTGactg]+')
        is_variant = bool(re.match(regex, text))
        if is_variant:
            return True
        else:
            return False

    @staticmethod
    def _check_phenocode(text):
        # Check if text is a phenocode
        regex = re.compile(r'\d+_\d+|\d+')
        is_phenocode = bool(regex.match(text))
        if is_phenocode:
            return True
        else:
            return False

    @staticmethod
    def _check_phenostring(text):
        # Check if text is a phenotype string
        regex = re.compile(r'[a-zA-Z]+')
        is_phenostring = bool(regex.match(text))
        if is_phenostring:
            return True
        else:
            return False

    def _get_phenocode(self, text):
        # Get the phenocode for a phenotype string
        if self.is_phenocode:
            phenocode = get_close_matches(text, self.phenotypes.values(), n=1, cutoff=0.1)[0]
            return phenocode.replace('.', '_')
        else:
            phenotype = get_close_matches(text, self.phenotypes.keys(), cutoff=0.1)[0]
            phenocode = SearchText.phenotypes.get(phenotype).replace('.', '_')
            return phenocode
