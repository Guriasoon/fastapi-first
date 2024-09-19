from fastapi import FastAPI
from contextlib import asynccontextmanager  # декоратор который позволяет создавать контекстный менеджер
from database import create_tables, delete_tables
from router import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('База готова к работе')
    yield
    print('Перезагрузка приложения')


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)