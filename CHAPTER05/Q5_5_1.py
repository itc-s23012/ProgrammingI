a = {x for x in 'abcabcabc' if x not in 'ab'}
print(a)
# ④
bigcity_of_japan = {'Sapporo', 'Sendai', 'Tokyo', 'Nagoya', 'Osaka', 'Fukuoka'}
print(bigcity_of_japan)

a = {'Sapporo', 'Sendai',  'Tokyo', 'Nagoya', 'Osaka', 'Fukuoka', 'Osaka'}
print(a)

set_a = set('ABCDEF')
print(set_a)

set_a.add('G')
print(set_a)

set_a.add('A')
print(set_a)
