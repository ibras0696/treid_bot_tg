from aiogram import Router

from Handlers.user_handler import router as user_router
from Handlers.admin_handlers import router as admin_router

router = Router()


router.include_routers(user_router, admin_router)
