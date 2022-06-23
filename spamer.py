import vk_api
import time
import pprint

token_1 = 'vk1.a.'
token_2 = 'vk2.a.'
token_3 = 'vk3.a.'
list_token = (token_1, token_2, token_3)
VERSION = 5.131
spam_text = 'Ищешь свежие и интересные новости о России и событиях в мире? Заходи к нам – https://vk.com/golossovesty'
list_subject = ['экономика', 'общество', 'новости', 'СМИ']
PHOTO = 'photo483705111_457240111'
session = vk_api.VkApi(token=list_token[0])

def get_group_list(subject):
    """метод получения списка групп по ключевому слову"""
    group = session.method("groups.search", {'q': subject, 'count': 10})
    return group['items']

def get_post_group(id):
    """Метод получения записей сообщества"""
    post = session.method("wall.get", {'owner_id': -id, "count": 3})
    return post['items']

def set_comment(session, id, post_id, text, photo):
    """метод оставляющий коментарий под конкретной записью"""
    session.method("wall.createComment", {'owner_id': -id, 'post_id': post_id, 'message': text, 'attachments': photo})
    print('Коментарий в группу https://vk.com/wall-' + str(id) + "_" + str(post_id) + ' отправлен')



