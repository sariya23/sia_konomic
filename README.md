# Test registration form
В данном репозитории лежит код для тестирование формы регистрации по такому URL: https://exchange.konomik.com/authorization/signup

## Используемые технологии
- Python
- Selenium
- Pytest
- Docker
- git hooks

Также используется паттерн Page Object.

## Локальный запуск
### Через Docker
Для начала нужно сбилдить отбраз. Находясь в корне проекта выполнить:
```shell
# docker build . -t <image_name>:<tag>
```
Далее нужно запустить контейнер. Либо так:
```shel
# docker run <image_name>:<tag>
```
В таком случае при запуске контейнера автоматически произойдет запуск тестов. Может работать нестабильно. Некоторые тесты непонятно почему падают, а иногда не создается сессия в Chrome.
Либо можно зайти внутрь контейнера и запустить их вручную:
```shell
# docker run -it --entrypoint bash <image_name>:<tag>
root@3d6063f281a6:/app# pytest -n auto 
```
Также по непонятным причинам может не создаваться сессия в Chrome.

### Без Docker
Для запуска без использования Docker выполнить, находясь в корне проекта (Linux):
```shell
# . venv/bin/activate
# pip install -r requirements/dev_requirements.txt
# pytest -n auto
```
Также обязательно начиличе chromedriver версии 122.x.

## По поводу pageo
На момент написания тестов в pageo нет поддержки работы с shadow DOM, поэтому пришлось писать самому. Issue уже направилю.
