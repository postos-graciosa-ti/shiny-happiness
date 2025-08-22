from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.hierarchy_structure import HierarchyStructure

hierarchy_structure_seed = [
    {"name": "Tático"},
    {"name": "Operacional"},
    {"name": "Estratégico"},
]


async def seed_hierarchy_structure():
    async with AsyncSession(engine) as session:
        for hierarchy_data in hierarchy_structure_seed:
            result = await session.exec(
                select(HierarchyStructure).where(
                    HierarchyStructure.name == hierarchy_data["name"]
                )
            )

            hierarchy = result.first()

            if not hierarchy:
                new_hierarchy = HierarchyStructure(**hierarchy_data)

                session.add(new_hierarchy)

        await session.commit()
