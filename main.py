# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

eerste_doelpuntmaker = 'Ruud Gullit'
tweede_doelpuntmaker = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = eerste_doelpuntmaker + ' ' + \
    str(goal_0) + ', ' + tweede_doelpuntmaker + ' ' + str(goal_1)
# print(scorers)

# report_1 = f'{eerste_doelpuntmaker} scored in the {goal_0}nd minute'
# report_2 = f'{tweede_doelpuntmaker} scored in the {goal_1}th minute'

# print(report_1, report_2)

# report = report_1 + ' ' + report_2

report = f'{eerste_doelpuntmaker} scored in the {goal_0}nd minute\n{tweede_doelpuntmaker} scored in the {goal_1}th minute'

# report = eerste_doelpuntmaker + ' scored in the ' + \
str(goal_0) + 'nd minute ' + tweede_doelpuntmaker + \
    ' scored in the ' + str(goal_1) + 'th minute'

#print(report)

player = 'Hans van Breukelen'

first_name = player[player.find("Hans"):player.find("Hans")+4]

last_name = player[player.find("van Breukelen"):]

last_name_len = len(last_name)

initial = first_name[0]

name_short = f'{initial}. {last_name}'

# print(name_short)

chant_ends_with_space = f'{first_name}! '*len(first_name)
chant = chant_ends_with_space.strip()

good_chant = chant[-1] != ' '

# print(good_chant)
