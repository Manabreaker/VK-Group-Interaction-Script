import vk_api
from config import *
import vk_api
import g4f
import time


def gpt(text_from_post, i=0):
    from config import response

    if len(text_from_post.split()) > 5:  # Если текст сообщения > пяти символов используем стандартный промпт
        message = prompt_1 + text_from_post
    else:  # Если текст сообщения < пяти символов используем альтернативный промпт
        message = prompt_2 + text_from_post

    try:
        response = g4f.ChatCompletion.create(model="gpt-3.5-turbo", provider=providers[i],
                                             messages=[{"role": "user", "content": message}])
    except:
        print('\033[31m' + 'Произошла ошибка при использовании ', providers[i], ', пробуем другую модель...\033[39m',
              sep='')
        if i + 1 < len(providers):
            gpt(text_from_post, i + 1)

    time.sleep(5)
    return response


def get_text_from_post(group_id, post_id):
    """ Получение информации о посте """
    response = vk.wall.getById(posts=f"{group_id}_{post_id}")

    """ Извлечение текста поста """
    text_from_post = response[0]['text']

    return text_from_post


def like_comment(group_id, post_id, message):
    records = open('records.txt', 'a')
    records.write(time.ctime()[4:] + ' Лайк на запись id' + str(post_id) + ' поставлен успешно! Оставлен комментарий: '
                  + message + '\n')
    vk.likes.add(owner_id=group_id, item_id=post_id, type='post')
    print(str(time.ctime()[4:]) + ' Лайк на запись id' + str(post_id) + ' поставлен успешно!')

    vk.wall.createComment(owner_id=group_id, post_id=post_id, message=message)
    print(str(time.ctime()[4:]) + ' Под записью id ' + str(post_id) + ' оставлен комментарий: ' + message)


def get_post_id(group_id):
    """ Получение последних двух записей группы """
    response = vk.wall.get(owner_id=group_id, count=2)  # Запрашиваем две последние записи
    """ Проверка, является ли последняя запись закрепленной """
    if 'is_pinned' in response['items'][0]:
        if response['items'][0]['is_pinned'] == 0:
            return response['items'][0]['id']  # Используем предпоследнюю запись
        else:
            return response['items'][1]['id']  # Используем предпредпоследнюю запись
    else:
        return response['items'][0]['id']  # Используем предпоследнюю запись


if __name__ == '__main__':
    """ Вход в аккаунт """
    vk_session = vk_api.VkApi(token=access_token)
    vk = vk_session.get_api()

    last_post_id = int(open('records.txt', 'r').readlines()[-1][38:44])
    """ Получение числового id группы """
    group_id = -1 * vk.groups.getById(group_id=group_name)[0]['id']
    records = open('records.txt')
    for string in records.readlines():
        print(string)
    records.close()
    a_flag = True
    while True:
            """ Вход в аккаунт """
            vk_session = vk_api.VkApi(token=access_token)
            vk = vk_session.get_api()

            if last_post_id != get_post_id(group_id):
                print('Найдена новая запись')
                last_post_id = get_post_id(group_id)  # обновляем id последнего поста
                text_from_post = get_text_from_post(group_id, last_post_id)  # Текст из поста
                like_comment(group_id, last_post_id, gpt(text_from_post))  # Ставим лайк и пишем комментарий
            time.sleep(5)
            if a_flag:
                print('Программа работает корректно')
            a_flag = False
