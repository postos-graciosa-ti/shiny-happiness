import os

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import SQLModel


async def get_column_type(column, dialect: str) -> str:
    col_type_str = str(column.type).upper()

    if dialect == "postgresql":
        if "VARCHAR" in col_type_str:
            return "VARCHAR"

        if "TEXT" in col_type_str:
            return "TEXT"

        if "BOOLEAN" in col_type_str:
            return "BOOLEAN"

        if "INTEGER" in col_type_str:
            return "INTEGER"

        if "DATETIME" in col_type_str:
            return "TIMESTAMP"

        if "FLOAT" in col_type_str:
            return "FLOAT"

    return col_type_str


async def watch(engine: AsyncEngine):
    db_dialect = os.environ.get("DIALETICS", "").lower()

    if not db_dialect:
        url = str(engine.url)

        if url.startswith("sqlite"):
            db_dialect = "sqlite"

        else:
            db_dialect = "postgresql"

    assert db_dialect in ("sqlite", "postgresql"), (
        f"Dialeto não suportado: {db_dialect}"
    )

    print(f"Usando o dialeto: {db_dialect}")

    async with engine.begin() as conn:
        for table in SQLModel.metadata.tables.values():
            table_name = table.name

            if db_dialect == "sqlite":
                result = await conn.execute(
                    text(
                        f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
                    )
                )

                table_exists = result.fetchone() is not None

                if not table_exists:
                    continue

                result = await conn.execute(text(f"PRAGMA table_info({table_name})"))

                existing_columns = {col[1] for col in result.fetchall()}

            else:
                result = await conn.execute(
                    text(
                        f"""
                        SELECT to_regclass('{table_name}');
                        """
                    )
                )

                table_exists = result.scalar() is not None

                if not table_exists:
                    continue

                result = await conn.execute(
                    text(
                        f"""
                        SELECT column_name
                        FROM information_schema.columns
                        WHERE table_name = '{table_name}';
                        """
                    )
                )

                existing_columns = {r[0] for r in result.fetchall()}

            for column in table.columns:
                if column.name not in existing_columns:
                    col_type = await get_column_type(column, db_dialect)

                    query = text(
                        f"ALTER TABLE {table_name} ADD COLUMN {column.name} {col_type}"
                    )

                    await conn.execute(query)

                    print(f"✅ Coluna '{column.name}' adicionada em '{table_name}'")
