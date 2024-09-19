from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  #

# Создает асинхронный движок для подключения к базе данных.
engine = create_async_engine(
    "sqlite+aiosqlite:///task.db"  # (название бд + драйвер) и название бд  task.db
)
# создаем открытие транзакций для работы с базой данных
new_session = async_sessionmaker(engine, expire_on_commit=False)  # Создает асинхронные сессии для работы с базой данных


# expire_on_commit=False что сессии не будут автоматически закрываться после коммита


# Определение базовой модели
class Model(DeclarativeBase):
    pass


# Определение модели таблицы tasks
class TaskOrm(Model):
    __tablename__ = 'tasks'  # Указывает имя таблицы в базе данных
    id: Mapped[int] = mapped_column(primary_key=True)  # Определяет столбец
    name: Mapped[str]  # Определяет столбец
    descriptions: Mapped[str | None]  # Определяет столбец


# Создание таблиц в базе данных
async def create_tables():
    async with engine.begin() as conn:  # Открывает асинхронное соединение с базой данных
        await conn.run_sync(Model.metadata.create_all)  # Выполняет синхронную функцию create_all
        # в асинхронном контексте, чтобы создать все таблицы, определенные в наших моделях

# Удаление таблиц
async def delete_tables():
    async with engine.begin() as conn:  # Открывает асинхронное соединение с базой данных
        await conn.run_sync(Model.metadata.drop_all)