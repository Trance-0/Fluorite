
from os.path import abspath, dirname, join

'''配置文件'''


ROOT_DIR = join(dirname(abspath(__file__)),'resources')
ACTION_DISTRIBUTION = [['1', '2', '3'],
					   ['4', '5', '6', '7', '8', '9', '10', '11'],
					   ['12', '13', '14'],
					   ['15', '16', '17'],
					   ['18', '19'],
					   ['20', '21'],
					   ['22'],
					   ['23', '24', '25'],
					   ['26',  '27', '28', '29'],
					   ['30', '31', '32', '33'],
					   ['34', '35', '36', '37'],
					   ['38', '39', '40', '41'],
					   ['42', '43', '44', '45', '46']]
PET_ACTIONS_MAP = {'pet_1': ACTION_DISTRIBUTION}
for i in range(2, 65): PET_ACTIONS_MAP.update({'pet_%s' % i: ACTION_DISTRIBUTION})