import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

main_token = '8068696abcf156f04d438685bc17d21867eed97411ca90bf38512ab8d57e76b56afb3ae29b0887ebbb481'

vk_session = vk_api.VkApi(token = main_token)
longpoll = VkLongPoll(vk_session)

#-------------------ФУНКЦИИ--------------------#

#Главный метод отправки сообщений
def sender(id, text):
	vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})

print('Бот запущен')

#-------------------ЦИКЛ--------------------#
for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.from_chat:
				msg = event.text.lower()
				msgl = event.text
				id = event.chat_id

				if msg in ['чтение']:
					kpad58 = open('baza.txt','r')
					klad57 = kpad58.read()
					sender(id, f'' + klad57)
					kpad58.close()

				if msg in ['цикл заметок']:
					for event in longpoll.listen():
						if event.type == VkEventType.MESSAGE_NEW:
							if event.to_me:
								if event.from_chat:
									user = event.user_id
									msg = event.text.lower()
									msgl = event.text
									kpad58 = open('baza.txt','r')
									klad57 = kpad58.read()
									kpad58.close()
									kpad8 = open('baza.txt','w')
									klad7 = kpad8.write(klad57 + '\n' + msgl) 
									kpad8.close()

									if msg in ['стоп']:
										break
