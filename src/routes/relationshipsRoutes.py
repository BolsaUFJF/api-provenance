from fastapi import APIRouter

from src.routes.relationships.wasUsedRoutes import router as was_used_routes
from src.routes.relationships.wasGeneratedBy import router as was_generated_by_routes
from src.routes.relationships.wasAssociatedWith import router as was_associated_with_routes
from src.routes.relationships.wasAttribuitedTo import router as was_attribuited_to_routes
from src.routes.relationships.wasInformedBy import router as was_informed_by_routes
from src.routes.relationships.wasDerivedFrom import router as was_derived_from_routes
from src.routes.relationships.actedOnBehalfOf import router as acted_on_behalf_routes

router = APIRouter(
   prefix = "/relationships",
   tags = ["Relationship Routes"],
   responses = {404: {"description": "Not Found"}},
)

@router.get('/', response_description="Root")
def root():
   return {
      "Relationship": "routes",
      "posts": {
         "was_used": "/relationships/was-used/post",
         "was_generated_by": "/relationships/was-generated-by/post",
         "was_associated_with": "/relationships/was-associated-with/post",
         "was_attribuited_to": "/relationships/was-attribuited-to/post",
         "was_informed_by": "/relationships/was-informed-by/post",
         "was_derived_from": "/relationships/was-derived-from/post",
         "acted_on_behalf": "/relationships/acted-on-behalf/post"
      }
   }

router.include_router(was_used_routes)
router.include_router(was_generated_by_routes)
router.include_router(was_associated_with_routes)
router.include_router(was_attribuited_to_routes)
router.include_router(was_informed_by_routes)
router.include_router(was_derived_from_routes)
router.include_router(acted_on_behalf_routes)