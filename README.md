## EN
# VK Group Interaction Script

This project is a script for interacting with VKontakte (VK) groups through their API. With this script, you can automate managing your group, such as liking posts and leaving comments.

## Features

- Automatically like posts and leave comments on the latest group posts.
- Utilize GPT for generating comments based on post text.
- Control through a simple command-line interface.

## Usage

### First Run

1. Install Python if you haven't already.
2. Install necessary dependencies using the following commands:
    ```bash
    pip install vk-api
    pip install g4f
    ```
3. Download the `config.py` file from the repository and replace the following data in it:
    ```python
    import g4f
    
    access_token = 'YOUR_ACCESS_TOKEN'
    group_name = 'YOUR_GROUP_ID'
    prompt_1 = 'YOUR_LONG_COMMENT'
    prompt_2 = 'YOUR_SHORT_COMMENT'
    response = 'YOUR_BASIC_COMMENT'
    providers = [g4f.Provider.GPTalk, g4f.Provider.GeekGpt, g4f.Provider.AiAsk, g4f.Provider.Aichat, g4f.Provider.ChatBase, g4f.Provider.ChatForAi, g4f.Provider.ChatgptAi, g4f.Provider.ChatgptX, g4f.Provider.FakeGpt, g4f.Provider.FreeGpt, g4f.Provider.GptForLove, g4f.Provider.GptGo, g4f.Provider.Hashnode, g4f.Provider.MyShell, g4f.Provider.OpenaiChat, g4f.Provider.Theb, g4f.Provider.You, g4f.Provider.Yqcloud]
    ```
    Replace `YOUR_ACCESS_TOKEN` with your access token, `YOUR_GROUP_ID` with your group's id, and specify your prompts and basic comment.

4. Run the `main.py` script from your Python development environment (such as IDLE) or another convenient environment.

## How It Works

- The script uses the VKontakte API to retrieve information about posts and automatically process them.
- Upon detecting a new post, the script likes it and generates a comment based on the post content using the GPT model.
- The results obtained are written to the `records.txt` file for further use or analysis.

## Notes

- Make sure your `access_token` is stored securely and not published in public repositories.
- This script is intended for educational and demonstration purposes only. Use it at your own risk.
- Data about liked posts and written comments are not only displayed in the console but also recorded in the `records.txt` file for further use or analysis.

## Questions and Support

If you have any questions or issues with using the script, please create a new issue in the repository.

# VK Group Interaction Script

## RU
Этот проект представляет собой скрипт для взаимодействия с группами ВКонтакте (VK) через их API. С помощью этого скрипта вы можете автоматизировать процессы управления вашей группой, такие как ставление лайков и оставление комментариев под постами.

## Особенности

- Автоматическое ставление лайков и оставление комментариев под последними постами группы.
- Использование GPT для генерации комментариев на основе текста поста.
- Управление через простой интерфейс командной строки.

## Использование

### Первый запуск

1. Установите Python, если его у вас еще нет.
2. Установите необходимые зависимости с помощью следующих команд:
    ```bash
    pip install vk-api
    pip install g4f
    ```
3. Скачайте файл `config.py` из репозитория и замените в нем следующие данные:
    ```python
    access_token = 'YOUR_ACCESS_TOKEN'
    group_name = 'YOUR_GROUP_ID'
    prompt_1 = 'YOUR_LONG_COMMENT'
    prompt_2 = 'YOUR_SHORT_COMMENT'
    response = 'YOUR_BASIC_COMMENT'
    ```
    Замените `YOUR_ACCESS_TOKEN` на ваш access token, `YOUR_GROUP_ID` на id вашей группы, а также укажите свои варианты промптов и базовый комментарий.

4. Запустите скрипт `main.py` из среды разработки Python (IDLE) или другой удобной среды.

## Как это работает

- Скрипт использует API ВКонтакте для получения информации о постах и их автоматической обработки.
- При обнаружении нового поста скрипт ставит лайк и генерирует комментарий на основе содержания поста с использованием модели GPT.
- Полученные результаты записываются в файл `records.txt` для последующего использования или анализа.

## Заметки

- Обязательно убедитесь, что ваш `access_token` находится в безопасном месте и не публикуйте его в открытых репозиториях.
- Этот скрипт предназначен только для образовательных и демонстрационных целей. Используйте его на свой страх и риск.
- Данные о поставленных лайках и написанных комментариях не только выводятся в консоль, но и записываются в файл `records.txt` для дальнейшего использования или анализа.

## Вопросы и поддержка

Если у вас возникли вопросы или проблемы с использованием скрипта, пожалуйста, создайте новый issue в репозитории.
