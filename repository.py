# позволяет работать с бд как с колекцией объектов
from sqlalchemy import select
from database import new_session, TaskOrm
from shemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:  # открываем новую сессию
            task_dict = data.model_dump()  # берем данные из data и превращаем в словарь

            task = TaskOrm(
                **task_dict)  # Создаем новую задачу и передаем данные из task_dict(типа словарь) Типа передаем TaskOrm - это таблица(name, descriptions)
            session.add(task)  # добавляем новую задачу в сессию.
            await session.flush()  # отправить все изменения в базу данных
            await session.commit()  # мы подтверждаем все изменения в базе данных
            return task.id  # возвращаем идентификатор (id) новой задачи

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)  # делаем селект запрос к сессии к таблице (через алхеми)
            result = await session.execute(query)  # обратись к бд через сессию и исполни нам этот запрос
            task_models = result.scalars().all()
            task_schemas = [STask.from_orm(task_model) for task_model in task_models]  # объект алхеми который должен вернуться
            return task_schemas
