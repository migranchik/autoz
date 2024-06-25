import imaplib, email, re

mail = 'crametohama@hotmail.com'
mail_pass = 'J91wWkjOriGRYiP'

servers = {
    'gmail.com': 'imap.gmail.com',
    'yandex.ru': 'imap.yandex.ru',
    'hotmail.com': 'imap-mail.outlook.com',
}


def get_code(mail, mail_pass):
    domain = mail.split('@')
    verification_code_pattern = re.compile(r'\b\d{6}\b')
    try:
        imap = imaplib.IMAP4_SSL(servers[domain[1]])
        print(imap.login(mail, mail_pass))

        imap.select('inbox')

        # Поиск писем от TikTok
        status, messages = imap.search(None, '(FROM "register@account.tiktok.com")')
        if status == 'OK':
            nums = messages[0].split()
            nums.reverse()
            print(nums)
            for num in nums:
                status, data = imap.fetch(num, '(RFC822)')

                # Если статус не OK, пропускаем дальнейшую обработку
                if status != 'OK':
                    continue

                # Получаем содержимое письма
                email_msg = data[0][1]
                message = email.message_from_bytes(email_msg)

                # Ищем тело письма
                if message.is_multipart():
                    for part in message.walk():
                        # Имеем в виду только текстовые части
                        if part.get_content_type() == 'text/plain':
                            body = part.get_payload(decode=True).decode()
                            # Поиск верификационного кода
                            match = verification_code_pattern.search(body)
                            print(body)
                            if match:
                                code = match.group(0)
                                return code
                                break  # Код найден, дальше не ищем
                else:
                    # Для не multipart сообщений
                    body = message.get_payload(decode=True).decode()
                    match = verification_code_pattern.search(body)
                    if match:
                        code = match.group(0)
                        return code
    except imaplib.IMAP4.error as e:
        print(f"IMAP4 error: {e}")
    finally:
        try:
            imap.close()
        except:
            pass
        imap.logout()



