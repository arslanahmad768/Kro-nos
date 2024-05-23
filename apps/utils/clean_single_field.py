class CleanFieldsModelMixin(object):

    def clean_single_fields(self):
        """Locate and invoke cleaner methods for each individial field."""
        field_names = self.get_model_field_names()
        for field_name in field_names:
            field_cleaner = self._get_field_cleaner(field_name)
            if field_cleaner:
                setattr(self, field_name, field_cleaner())

    def get_model_field_names(self):
        try:
            field_names = [field.name for field in self._meta.get_fields()]
        except AttributeError:
            field_names = self._meta.get_all_field_names()
        return field_names

    def _get_field_cleaner(self, field_name):
        """Return any cleaners for the named field.
        Args:
            field_name (str): name of the field on this model whose cleaners
                to retrieve.
        Return:
            callable or None
        """
        field_cleaner = getattr(self, 'clean_{}'.format(field_name), None)
        if field_cleaner and not callable(field_cleaner):
            field_cleaner = None
        return field_cleaner

    def clean(self):
        """Run field cleaners for this model instance"""
        self.clean_single_fields()
        super(CleanFieldsModelMixin, self).clean()
