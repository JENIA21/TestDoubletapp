from fastapi import APIRouter

from controllers import pet_controller


def get_apps_router():
    router = APIRouter()
    router.include_router(pet_controller.router)
    return router
