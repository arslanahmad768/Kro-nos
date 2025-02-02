from drf_yasg.inspectors.base import FieldInspector
from drf_yasg.inspectors.view import SwaggerAutoSchema


def unique_parameters(parameters):
    seen = {}
    return [seen.setdefault(repr(e),e) for e in parameters if repr(e) not in seen]


def add_manual_fields(self, serializer_or_field, schema):
    """
    Override swagger_schema_fields properties instead of overriding the whole schema.
    https://github.com/axnsan12/drf-yasg/issues/291
    """
    meta = getattr(serializer_or_field, 'Meta', None)
    swagger_schema_fields = getattr(meta, 'swagger_schema_fields', {})
    if swagger_schema_fields:
        for attr, val in swagger_schema_fields.items():
            if isinstance(val, dict) and isinstance(getattr(schema, attr, None), dict):
                to_update = dict(list(getattr(schema, attr).items()) + list(val.items()))
                setattr(schema, attr, to_update)
            else:
                setattr(schema, attr, val)

FieldInspector.add_manual_fields = add_manual_fields


class SwaggerAutoSchema(SwaggerAutoSchema):

    def add_manual_parameters(self, parameters):
        try:
            return super().add_manual_parameters(parameters)
        except AssertionError:
            parameters = unique_parameters(parameters)
            return super().add_manual_parameters(parameters)
