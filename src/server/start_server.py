from fastapi import FastAPI

from server.endpoints.victim import router as router_victim
from server.endpoints.user import router as router_users
from server.endpoints.staff import router as router_staff
from server.endpoints.fakewebsites import router as router_fakewebsite
from server.endpoints.operations import router as router_operation
from server.endpoints.message import router as router_message
from server.endpoints.location import router as router_location
from server.db.DB_manager import base_manager
from server.settings import SCRIPTS_PATH

app = FastAPI()
app.include_router(router_users, prefix='/users_start')
app.include_router(router_victim, prefix='/victim_start')
app.include_router(router_staff, prefix='/staff_start')
app.include_router(router_fakewebsite, prefix='/fakewebsites_start')
app.include_router(router_operation, prefix='/operation_start')
app.include_router(router_message, prefix='/message_start')
app.include_router(router_location, prefix='/location_start')


@app.get('/')
def start_page():
    return 'Page BD'


base_manager.create_base(SCRIPTS_PATH)

