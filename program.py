import logging.handlers
from tglogging import TelegramLogHandler
from aiogram import Bot, Dispatcher
import asyncio
import logging
from environs import Env
from app import handlers
from app import set_main_menu

env = Env()
env.read_env()


class BotRun:
    async def main(self):
        bot = Bot(token=env("BOT_TOKEN"))
        dp = Dispatcher(storage=handlers.storage)
        dp.include_router(handlers.router)
        dp.startup.register(set_main_menu)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)


if __name__ == "__main__":
    bot_run = BotRun()
    logging.basicConfig(
        level=logging.WARNING,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
        handlers=[
            TelegramLogHandler(
                token=env("BOT_TOKEN"),
                log_chat_id=env('log_chat_id'),
                update_interval=2,
                minimum_lines=1,
                pending_logs=200000,
            ),
            logging.StreamHandler(),
        ],
    )
    try:
        asyncio.run(bot_run.main())
    except:
        print("Завершено")
        KeyboardInterrupt()
