with open('nginx_logs.txt') as f:
    request_dict = {}
    for line in f:
        remote_addr = line[:line.find(' ')]
        request_dict.setdefault(remote_addr, 0)
        request_dict[remote_addr] += 1
request_list = sorted(request_dict.items(), key=lambda item: item[1], reverse=True)
spammer = request_list[0][0]
requests_num = request_list[0][1]
print(f'Spammer is {spammer} with {requests_num} requests')
