@echo off
set DJANGO_SETTINGS_MODULE=chat.settings
daphne chat.asgi:application