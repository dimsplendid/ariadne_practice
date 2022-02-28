from ariadne import (
    gql, 
    QueryType,
    make_executable_schema
)
from ariadne.asgi import GraphQL

# Create QueryType instance for Query type defined in our schema
query = QueryType()

type_defs = gql("""
    type Query {
        hello: String!
    }
""")

@query.field('hello')
def resolve_hello(_, info):
    request = info.context['request']
    user_agent = request.headers.get('user-agent', 'guest')
    return f'Hello {user_agent}'

schema = make_executable_schema(type_defs, query)

app = GraphQL(schema, debug=True)