
class OrderingBackend(object):

    def get_ordering_fields(self, resource):
        return getattr(resource, 'ordering_fields', None)

    def get_fields(self, resource):
        ordering_fields = self.get_ordering_fields(resource)
        schema_fields = resource.schema.schema().get('properties')
        if ordering_fields:
            ordering_fields = set(ordering_fields) & set(schema_fields)
        else:
            ordering_fields = set(schema_fields)
        return ordering_fields

    def get_filters(self, resource, schema_in, query):
        ordering_fields = self.get_fields(resource)

        model = resource.model
        orderings = schema_in.ordering

        if orderings:
            orderings = orderings.split(',')
            order_q = []
            for ordering in orderings:
                field = ordering.strip('-')
                if field not in ordering_fields:
                    continue

                if ordering.startswith('-'):
                    order_type = 'desc'
                else:
                    order_type = 'asc'
                q = getattr(getattr(model, field), order_type)
                order_q.append(q())

            query = query.order_by(*order_q)
        return query
