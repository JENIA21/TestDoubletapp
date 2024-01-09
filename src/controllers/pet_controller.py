from fastapi import HTTPException, APIRouter, Security, UploadFile
from starlette.status import HTTP_400_BAD_REQUEST


from schemas.pet_schema import PetCreate, PetCreateResponse, PhotoCreate, PhotoCreateResponse, PetGetResponse, \
    PetDeleteResponse, PetDelete, Support
from services.file_add_service import file_service
from services.pet_servise import pet_service
from utils.key_authentication import get_api_key


router = APIRouter()


@router.post("/pets")
async def create_pets(
        data: PetCreate,
        api_key: str = Security(get_api_key)
) -> PetCreateResponse:
    try:
        return await pet_service.create(model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("/pets")
async def get_pets(
        limit: int | None = None,
        offset: int | None = None,
        has_photo: bool = False,
        api_key: str = Security(get_api_key)
) -> PetGetResponse:
    try:
        return await pet_service.get_multi(limit=limit,
                                           offset=offset,
                                           has_photo=has_photo)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.delete("/pets")
async def delete_pets(
        data: PetDelete,
        api_key: str = Security(get_api_key)
) -> PetDeleteResponse:
    try:
        return await pet_service.delete(ids=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.post("/pets/{id}/photo")
async def add_photo_for_pet(
        file: UploadFile,
        id: str,
        api_key: str = Security(get_api_key)
) -> PhotoCreateResponse:
    try:
        return await file_service.add_photo(file=await file.read(), id=id, filename=file.filename)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
