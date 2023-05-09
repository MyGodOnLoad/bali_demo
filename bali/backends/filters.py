from bali.db.operators import get_filters_expr


class FilterBackend(object):

    def get_filter_fields(self, resource):
        return getattr(resource, 'filter_fields', None)

    def get_fields(self, resource):
        schema_fields = resource.schema.schema().get('properties')
        filter_fields = self.get_filter_fields(resource)
        if filter_fields:
            filter_fields = set(filter_fields) & set(schema_fields)
        else:
            filter_fields = set(schema_fields)
        return filter_fields

    def get_filters(self, resource, schema_in, query):
        filter_fields = self.get_fields(resource)

        target = {k: v for k, v in schema_in.filters.items() if k in filter_fields}

        if target:
            query = query.filter(*get_filters_expr(resource.model, **target))
        return query
