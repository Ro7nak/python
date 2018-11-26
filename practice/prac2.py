# PF-Prac-8
def calculate_net_amount(trans_list):
    net_amount = 0
    for i in trans_list:
        if i[:1] == "D":
            net_amount += int(i[2:])
        else:
            net_amount -= int(i[2:])
    return net_amount


trans_list = ["D:300", "D:200", "W:200", "D:200"]
print(calculate_net_amount(trans_list))
