import operator
from functools import reduce


class SearchBackend(object):

    def get_search_fields(self, resource):
        return getattr(resource, 'search_fields', None)

    def get_fields(self, resource):
        search_fields = self.get_search_fields(resource)
        schema_fields = resource.schema.schema().get('properties')
        if search_fields:
            search_fields = set(search_fields) & set(schema_fields)
        else:
            search_fields = set(schema_fields)
        return search_fields

    def get_search_terms(self, request):
        params = request.query_params.get('search', '')
        return params.replace(',', ' ').split()

    def get_filters(self, resource, schema_in, query):
        model = resource.model
        search_fields = self.get_fields(resource)
        search_terms = self.get_search_terms(resource._request)

        search_q = []
        for field in search_fields:
            for search_term in search_terms:
                q = getattr(getattr(model, field), 'like')(f'%{search_term}%')
                search_q.append(q)

        if search_q:
            query = query.filter(reduce(operator.or_, search_q))
        return query
