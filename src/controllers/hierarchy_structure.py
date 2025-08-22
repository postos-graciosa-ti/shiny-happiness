from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.hierarchy_structure import HierarchyStructure


async def handle_get_hierarchy_structure():
    async with AsyncSession(engine) as session:
        query = select(HierarchyStructure)

        result = await session.exec(query)

        hierarchy_structure = result.all()

        return hierarchy_structure
