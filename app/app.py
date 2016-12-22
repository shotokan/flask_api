import pybreaker
from app.bots.bot_listener import BotListener

bot_breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=30, listeners=[BotListener()])
