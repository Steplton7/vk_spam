import vk_api
import time
import pprint

token_1 = 'vk1.'
token_2 = 'vk1.'
token_3 = 'vk1.'
token_4 = 'vk1.'
list_token = (token_1, token_2)
VERSION = 5.131
spam_text = 'Ищешь свежие и интересные новости о России и событиях в мире? Заходи к нам – https://vk.com/golossovesty'
list_subject = ['наука', 'общество']#'новости', 'СМИ', 'экономика', 'общество', "политика", "правда", "Рифмы"]
PHOTO = 'photo676766983_457239022'
session = vk_api.VkApi(token=token_4)
print(spam_text)


def get_group_list(subject):
    """метод получения списка групп по ключевому слову"""
    group = session.method("groups.search", {'q': subject, 'count': 5})
    return group['items']


def get_post_group(id):
    """Метод получения записей сообщества"""
    post = session.method("wall.get", {'owner_id': -id, "count": 3})
    return post['items']


def set_comment(session, id, post_id, text , photo):
    """метод оставляющий коментарий под конкретной записью"""
    session.method("wall.createComment", {'owner_id': -id, 'post_id': post_id, 'message': text, 'attachments': photo})
    print('Коментарий в группу https://vk.com/wall-' + str(id) + "_" + str(post_id) + ' отправлен')


def main():
    captcha_index = 1
    mylist = list()
    for i in range(len(list_subject)):
        time.sleep(1)
        list_group = get_group_list(list_subject[i])
        for j in range(len(list_group)):
            if list_group[j]['is_closed'] == 0:
                post = get_post_group(list_group[j]['id'])
                time.sleep(5)
                for k in range(len(post)):
                    if post[k]['comments'].get('can_post', 0) == 1:

                        session = vk_api.VkApi(token=list_token[captcha_index % 2])
                        print('https://vk.com/wall-' + str(list_group[j]['id']) + "_" + str(post[k]['id']))
                        time.sleep(10)
                        captcha_index += 1
                        try:
                            set_comment(session,list_group[j]['id'], post[k]['id'], spam_text, PHOTO)
                        except Exception:
                            session = vk_api.VkApi(token=list_token[captcha_index % 2])
                            set_comment(session, list_group[j]['id'], post[k]['id'], spam_text, PHOTO)
                        mylist.append('https://vk.com/wall-' + str(list_group[j]['id']) + "_" + str(post[k]['id']))

    print(mylist)
    return mylist


def delete_comment(owner_id,post_id):
    """Метод удаления всех коментариев под постом"""
    com = session.method("wall.getComments", {"owner_id": -owner_id, "post_id": post_id, "count": 100})['items']
    for i in range(len(com)):
        session.method("wall.deleteComment", {'owner_id': -owner_id, "comment_id": com[i]['id']})
        print('delete')

#if __name__ == "__main__":
#    main()
#142918777 москва онлайн+
#91452083 наука и развитие+
#30179569 убойный юмор+
#15755094 РИА
#26284064 тасс
#170528132 топор+

casho =  {
    15755094: ['4394256, 4395258, 4395245'],#ria
    91452083: ['763517, 1904175, 1904143'],#n r
    142918777: ['633150, 633470, 633453'],#mos
    170528132: ['4472735, 4472512, 4472469'],}#top
print(casho)
#file = open('list_group_id.txt')

with open('list_group_id.txt') as file:
    l = (15755094, 142918777, 170528132)
    cash = dict()
    k = list()
    for i in range(9):
        s = [file.readline()]
        s = [line.rstrip(',\n') for line in s]
        k.append(int(s[0]))
    print(k)
    cash[15755094] = k[0:3]
    cash[142918777] = k[3:6]
    cash[170528132] = k[6:9]
k = 1
while k<2:
    for keys in cash:
        s = get_post_group(keys)
        old_post_list = cash.get(keys)
        new_post_list = list()
        for i in range(len(s)):
            new_post_list.append(s[i]['id'])
        for i in new_post_list:
            if i not in old_post_list:
                time.sleep(5)
                set_comment(session, keys, i, spam_text, PHOTO)
                print('update')
            else:
                print("no up")
            cash[keys] = new_post_list
        #print(new_post_list)
        #print(old_post_list)
    pprint.pprint(cash)
    time.sleep(1)
    k+=1
    print('---------')

with open('list_group_id.txt','w') as file:
    k = list()
    for id_g,id_p in cash.items():
        for i in id_p:
            k.append(i)

    for i in k:
        print(i)
        file.write(str(i) +',\n')





"""
while True:
    for keys in cash:
        s = get_post_group(keys)
        old_post_list = cash.get(keys)
        new_post_list = list()
        for i in range(len(s)):
            new_post_list.append(s[i]['id'])
        for i in new_post_list:
            if i not in old_post_list:
                #set_comment(session, keys, i, spam_text, PHOTO)
                print('update')
            else:
                print("no up")
            cash[keys] = new_post_list
        #print(new_post_list)
        #print(old_post_list)
    print(cash)
    time.sleep(10)
    print('---------')
    break


---------------------------------------
    session = vk_api.VkApi(token=list_token[captcha_index % 2])
    time.sleep(10)
    try:
        set_comment(session, list_group[j]['id'], post[k]['id'], spam_text, PHOTO)
    except vk_api.exceptions.Captcha:
        time.sleep(1)
        captcha_index = captcha_index + 1
        print(captcha_index % 2, 'exept STOP!!!')
        # break
        session = vk_api.VkApi(token=list_token[captcha_index % 2])
        set_comment(session, list_group[j]['id'], post[k]['id'], spam_text, PHOTO)
"""

'''
old = [225711, 225766, 225766]
new = [225710, 225762, 225766]
for i in new:
    if i not in old:
        #set_comment(session, 346191, i, spam_text, PHOTO)
        print('setcom')
    else:
        print('no update')'''