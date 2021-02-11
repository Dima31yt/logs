import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

main_token = '63ef3cec673e19ba9c4fb90199abff41b8286e23754e945f9ea401aceb7bea07db29c3a3b9a2ad2657c18'

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
									sender(id, f'Готово!')
									kpad8.close()

									if msg in ['стоп']:
										break