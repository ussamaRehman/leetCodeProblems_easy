gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas_a = 0
last_s = len(gas) - 1
start = None

for gas_s, gas_a in enumerate(gas):
    if gas_s == last_s and not start:
        print('-1')
        break
    if not start and gas_a < cost[gas_s]:
        continue
    if not start and gas_a >= cost[gas_s]:
        start = gas_s
        gas_a += gas_a - cost[gas_s]
    if gas_s == last_s:
        gas_s = 0
    if gas_a == 0 and gas_s != start:
        print('-1')
        break
    if gas_s == start:
        print(f'{gas_s}')
        break