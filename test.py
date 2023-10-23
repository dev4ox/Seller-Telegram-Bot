from func import *

table_users = ['user_id', 'username', 'first_name', 'last_name', 'phone', 'email', 'reg_date', 'ref_code', 'sub_pub']
table_orders = ['order_id', 'user_id', 'count', 'order_list', 'master', 'discont', 'order_date']
table_payments = ['pay_id', 'user_id', 'count', 'pay_date', 'trans_id']
message = {'content_type': 'text',
       'id': 1,
       'message_id': 1,
       'from_user': {'id': 0,
                     'is_bot': False,
                     'first_name': 'Developer',
                     'username': 'dev4ox',
                     'last_name': 'Fox',
                     'language_code': 'ru',
                     'can_join_groups': None,
                     'can_read_all_group_messages': None,
                     'supports_inline_queries': None,
                     'is_premium': None,
                     'added_to_attachment_menu': None},
       'date': 1697490297,
       'chat': {'id': 0,
                'type': 'private',
                'title': None,
                'username': 'dev4ox',
                'first_name': 'Developer',
                'last_name': 'Fox',
                'is_forum': None,
                'photo': None,
                'bio': None,
                'join_to_send_messages': None,
                'join_by_request': None,
                'has_private_forwards': None,
                'has_restricted_voice_and_video_messages': None,
                'description': None,
                'invite_link': None,
                'pinned_message': None,
                'permissions': None,
                'slow_mode_delay': None,
                'message_auto_delete_time': None,
                'has_protected_content': None,
                'sticker_set_name': None,
                'can_set_sticker_set': None,
                'linked_chat_id': None,
                'location': None,
                'active_usernames': None,
                'emoji_status_custom_emoji_id': None,
                'has_hidden_members': None,
                'has_aggressive_anti_spam_enabled': None,
                'emoji_status_expiration_date': None},
       'sender_chat': None,
       'forward_from': None,
       'forward_from_chat': None,
       'forward_from_message_id': None,
       'forward_signature': None,
       'forward_sender_name': None,
       'forward_date': None,
       'is_automatic_forward': None,
       'reply_to_message': None,
       'via_bot': None, 'edit_date': None,
       'has_protected_content': None,
       'media_group_id': None,
       'author_signature': None,
       'text': '/start',
       # 'entities': [<telebot.types.MessageEntity object at 0x0000018C2861C990>],
       'caption_entities': None,
       'audio': None,
       'document': None,
       'photo': None,
       'sticker': None,
       'video': None,
       'video_note': None,
       'voice': None,
       'caption': None,
       'contact': None,
       'location': None,
       'venue': None,
       'animation': None,
       'dice': None,
       'new_chat_member': None,
       'new_chat_members': None,
       'left_chat_member': None,
       'new_chat_title': None,
       'new_chat_photo': None,
       'delete_chat_photo': None,
       'group_chat_created': None,
       'supergroup_chat_created': None,
       'channel_chat_created': None,
       'migrate_to_chat_id': None,
       'migrate_from_chat_id': None,
       'pinned_message': None,
       'invoice': None,
       'successful_payment': None,
       'connected_website': None,
       'reply_markup': None,
       'message_thread_id': None,
       'is_topic_message': None,
       'forum_topic_created': None,
       'forum_topic_closed': None,
       'forum_topic_reopened': None,
       'has_media_spoiler': None,
       'forum_topic_edited': None,
       'general_forum_topic_hidden': None,
       'general_forum_topic_unhidden': None,
       'write_access_allowed': None,
       'user_shared': None,
       'chat_shared': None,
       'story': None,
       'json': {'message_id': 1,
                'from': {
                    'id': 0,
                    'is_bot': False,
                    'first_name': 'Developer',
                    'last_name': 'Fox',
                    'username': 'dev4ox',
                    'language_code': 'ru'},
                'chat': {
                    'id': 0,
                    'first_name': 'Developer',
                    'last_name': 'Fox',
                    'username': 'dev4ox',
                    'type': 'private'},
                'date': 1697490297,
                'text': '/start',
                'entities': [{'offset': 0,
                              'length': 6,
                              'type': 'bot_command'}]
                }
       }



call = {'id': '5673885123357213651',
        'from_user': {'id': 5616021621,
                      'is_bot': False,
                      'first_name': 'Developer',
                      'username': 'dev4ox',
                      'last_name': 'Fox',
                      'language_code': 'ru',
                      'can_join_groups': None,
                      'can_read_all_group_messages': None,
                      'supports_inline_queries': None,
                      'is_premium': None,
                      'added_to_attachment_menu': None},
        'message': {'content_type': 'text',
                    'id': 203, 'message_id': 203,
                    # 'from_user': <telebot.types.User object at 0x0000022C47D56210>,
'                   date': 1697928424,
                    # 'chat': <telebot.types.Chat object at 0x0000022C47D57F90>,
                    'sender_chat': None,
                    'forward_from': None,
                    'forward_from_chat': None,
                    'forward_from_message_id': None,
                    'forward_signature': None,
                    'forward_sender_name': None,
                    'forward_date': None,
                    'is_automatic_forward': None,
                    'reply_to_message': None,
                    'via_bot': None,
                    'edit_date': 1697929496,
                    'has_protected_content': None,
                    'media_group_id': None,
                    'author_signature': None,
                    'text': 'Для оформления заказа напишите нам',
                    # 'entities': [<telebot.types.MessageEntity object at 0x0000022C47D57390>],
                    'caption_entities': None,
                    'audio': None,
                    'document': None,
                    'photo': None,
                    'sticker': None,
                    'video': None,
                    'video_note': None,
                    'voice': None,
                    'caption': None,
                    'contact': None,
                    'location': None,
                    'venue': None,
                    'animation': None,
                    'dice': None,
                    'new_chat_member': None,
                    'new_chat_members': None,
                    'left_chat_member': None,
                    'new_chat_title': None,
                    'new_chat_photo': None,
                    'delete_chat_photo': None,
                    'group_chat_created': None,
                    'supergroup_chat_created': None,
                    'channel_chat_created': None,
                    'migrate_to_chat_id': None,
                    'migrate_from_chat_id': None,
                    'pinned_message': None,
                    'invoice': None,
                    'successful_payment': None,
                    'connected_website': None,
                    # 'reply_markup': <telebot.types.InlineKeyboardMarkup object at 0x0000022C47D653D0>,
                    'message_thread_id': None,
                    'is_topic_message': None,
                    'forum_topic_created': None,
                    'forum_topic_closed': None,
                    'forum_topic_reopened': None,
                    'has_media_spoiler': None,
                    'forum_topic_edited': None,
                    'general_forum_topic_hidden': None,
                    'general_forum_topic_unhidden': None,
                    'write_access_allowed': None,
                    'user_shared': None,
                    'chat_shared': None,
                    'story': None,
                    'json': {'message_id': 203,
                             'from': {'id': 6525829659,
                                      'is_bot': True,
                                      'first_name': 'Fox Service Bot',
                                      'username': 'foxserviceBot'},
                             'chat': {'id': 5616021621,
                                      'first_name': 'Developer',
                                      'last_name': 'Fox',
                                      'username': 'dev4ox',
                                      'type': 'private'},
                             'date': 1697928424,
                             'edit_date': 1697929496,
                             'text': 'Для оформления заказа напишите нам',
                             'entities': [{'offset': 22, 'length': 12, 'type': 'bold'}],
                             'reply_markup': {'inline_keyboard': [[{'text': '⬅️  Назад',
                                                                    'callback_data': 'main'},
                                                                   {'text': '📋  Каталог',
                                                                    'callback_data': 'catalog'}],
                                                                  [{'text': '📩  Написать нам',
                                                                    'url': 'https://t.me/dev4ox'}]]}}},
        'inline_message_id': None,
        'chat_instance': '5649510892878336445',
        'data': 'catalog',
        'game_short_name': None,
        'json': {'id': '5673885123357213651',
                 'from': {'id': 5616021621,
                          'is_bot': False,
                          'first_name': 'Developer',
                          'last_name': 'Fox',
                          'username': 'dev4ox',
                          'language_code': 'ru'},
                 'message': {'message_id': 203,
                             'from': {'id': 6525829659,
                                      'is_bot': True,
                                      'first_name': 'Fox Service Bot',
                                      'username': 'foxserviceBot'},
                             'chat': {'id': 5616021621,
                                      'first_name': 'Developer',
                                      'last_name': 'Fox',
                                      'username': 'dev4ox',
                                      'type': 'private'},
                             'date': 1697928424,
                             'edit_date': 1697929496,
                             'text': 'Для оформления заказа напишите нам',
                             'entities': [{'offset': 22,
                                           'length': 12,
                                           'type': 'bold'}],
                             'reply_markup': {'inline_keyboard': [[{'text': '⬅️  Назад',
                                                                    'callback_data': 'main'},
                                                                   {'text': '📋  Каталог',
                                                                    'callback_data': 'catalog'}],
                                                                  [{'text': '📩  Написать нам',
                                                                    'url': 'https://t.me/dev4ox'}]]}},
                 'chat_instance': '5649510892878336445',
                 'data': 'catalog'}}

def db_r(user_id: int, parametr: list[int]):
    answer = []
    conn = sqlite3.connect(key.db)
    cursor = conn.cursor()
    try:
        for i in parametr:
            cursor.execute(f"SELECT {KEY_REQUESTS[i][1]} FROM {KEY_REQUESTS[i][0]} WHERE user_id=?", (user_id,))
            result = cursor.fetchone()
            answer.append(result[0])
    except Exception as e:
        print('db_req_users', e)
    finally:
        cursor.close()
        return answer

def db_w(user_id: int, parametr: dict[int, str]):
    answer = []
    conn = sqlite3.connect(key.db)
    cursor = conn.cursor()
    try:
        for i in parametr:
            cursor.execute(f"SELECT {KEY_REQUESTS[i][1]} FROM {KEY_REQUESTS[i][0]} WHERE user_id=?", (user_id,))
            result = cursor.fetchone()
            answer.append(result[0])
    except Exception as e:
        print('db_req_users', e)
    finally:
        cursor.close()
        return answer

db_w(5616021621, {})
print(db_req(5616021621, [20, 26]))