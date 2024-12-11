
# Telegram Book Bot

Этот бот Telegram позволяет просматривать список книг из Google Drive и получать к ним доступ по ссылке.

## Деплой на Railway

1. Загрузите архив ZIP или подключите репозиторий к Railway.
2. В **Settings > Environment** добавьте переменную окружения:
   ```
   TELEGRAM_API_TOKEN=ваш_токен
   ```
3. Railway автоматически создаст приложение и запустит команду из `Procfile`.
    