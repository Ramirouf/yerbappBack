from sqlmodel import select
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.observation import Observation
from app.schemas.observation import ObservationCreate, ObservationUpdate


async def get_all_observations(session: AsyncSession) -> List[Observation]:
    result = await session.execute(select(Observation))
    return result.scalars().all()


async def create_observation(
    observation_data: ObservationCreate, session: AsyncSession
) -> Observation:
    observation = Observation(**observation_data.dict())
    session.add(observation)
    await session.commit()
    await session.refresh(observation)
    return observation


async def get_observation(
    observation_id: int, session: AsyncSession
) -> Optional[Observation]:
    result = await session.execute(
        select(Observation).where(Observation.id == observation_id)
    )
    return result.scalar_one_or_none()


async def update_observation(
    observation_id: int, observation_data: ObservationUpdate, session: AsyncSession
) -> Optional[Observation]:
    observation = await get_observation(observation_id, session)
    if not observation:
        return None
    update_data = observation_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(observation, key, value)
    session.add(observation)
    await session.commit()
    await session.refresh(observation)
    return observation


async def delete_observation(observation_id: int, session: AsyncSession) -> bool:
    observation = await get_observation(observation_id, session)
    if not observation:
        return False
    await session.delete(observation)
    await session.commit()
    return True
