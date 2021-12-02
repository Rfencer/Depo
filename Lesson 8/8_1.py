import re


def email_parse(email_address):
    RE_NAME = re.compile(r'([\w+\d+]*)(?=@).(?<=@)([\w+\d+]*\.\w+)')
    data = re.findall(RE_NAME, email_address)
    if data:
        username, domain = data[0]
        email_dict = {'username': username, 'domain': domain}
        return email_dict
    else:
        raise ValueError('no email found')


email = 'someone@geekbrains.ru'
print(email_parse(email))
email = 'testtestset'
print(email_parse(email))
email = 'testtestset@sfsaf'
print(email_parse(email))