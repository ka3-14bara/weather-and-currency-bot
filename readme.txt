Бот выдает курсы валют, криптовалют и прогноз погоды в наб. челнах.

Для получения курса используются запросы(библиотека "requests") к серверу гугл при помощи заранее подготовленных
ссылок на необходимые страницы, затем происходит парсинг по полученному HTML коду страницы, имена необходимых блоков, 
поиск которых происходит при парсинге,  найдены заранее вручную. Парсинг происходит при помощи инструмента "BeautifulSoup".

