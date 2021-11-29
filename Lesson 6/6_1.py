

with open('nginx_logs.txt') as f:
    request_list = []
    for line in f:
        remote_addr = line[:line.find(' ')]
        request_type = line[line.find('"')+1:line.find(' /')]
        requested_resource = line[line.find(' /')+1:line.find('" ')]
        request_list.append((remote_addr, request_type, requested_resource))
print(request_list)
