from fastapi import HTTPException, APIRouter, Security
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT


from schemas.pet_schema import PetCreate, PetCreateResponse
from services.pet_servise import pet_service
from utils.key_authentication import get_api_key
from utils.pet_utils import crate_pet_id

router = APIRouter()


async def add_id(data):
    data["id"] = crate_pet_id()
    return data


@router.post("/pets")
async def create_pets(
        data: PetCreate,
        api_key: str = Security(get_api_key)
) -> PetCreateResponse:
    try:
        return await pet_service.create(model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))



