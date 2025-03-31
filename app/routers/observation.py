from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.observation import Observation
from app.schemas.observation import (
    ObservationCreate,
    ObservationRead,
    ObservationUpdate,
)
from app.services.observation import (
    get_all_observations,
    create_observation,
    update_observation,
    delete_observation,
    get_observation,
)
from app.db.db import get_async_session  # This is your async session dependency
from uuid import UUID

# Assuming you have set up FastAPI Users, import the dependency for getting the current active user:
# from fastapi_users import FastAPIUsers
# from app.models.user import User
# from app.schemas.user import UserCreate, UserUpdate, UserDB
# from app.services.user import get_user_manager


def get_jwt_strategy():
    # Your implementation for JWT strategy here
    pass


# fastapi_users = FastAPIUsers[User, UserCreate, UserUpdate, UserDB](
#     get_user_manager, [get_jwt_strategy()]
# )

# Dependency to ensure the user is authenticated
# current_active_user = fastapi_users.current_user()

router = APIRouter()


@router.get("/observations", response_model=List[ObservationRead])
async def view_observations(
    session: AsyncSession = Depends(get_async_session),
    # user: User = Depends(current_active_user),
):
    observations = await get_all_observations(session)
    return observations


@router.post(
    "/observations",
    # response_model=ObservationRead,
    status_code=status.HTTP_201_CREATED,
)
async def add_observation(
    observation: ObservationCreate,
    session: AsyncSession = Depends(get_async_session),
    # user: User = Depends(current_active_user),
):
    # Optionally, ensure that the user_id is taken from the current user:
    # observation.user_id = user.id
    # new_obs = await create_observation(observation, session)
    await create_observation(observation, session)
    # return new_obs


@router.put("/observations/{observation_id}", response_model=ObservationRead)
async def edit_observation(
    observation_id: UUID,
    observation: ObservationUpdate,
    session: AsyncSession = Depends(get_async_session),
    # user: User = Depends(current_active_user),
):
    updated = await update_observation(observation_id, observation, session)
    if not updated:
        raise HTTPException(status_code=404, detail="Observation not found")
    return updated


@router.delete("/observations/{observation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_observation_endpoint(
    observation_id: UUID,
    session: AsyncSession = Depends(get_async_session),
    # user: User = Depends(current_active_user),
):
    success = await delete_observation(observation_id, session)
    if not success:
        raise HTTPException(status_code=404, detail="Observation not found")
    return None
