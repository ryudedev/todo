from middleware.create_api import create_api
from middleware.tags import Tags

v1_router = create_api(prefix="/1", tags=[Tags.V1], api_routes=[])
