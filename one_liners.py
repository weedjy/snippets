# given (hh:mm:ss)_1 and (hh:mm:ss)_2. find the difference in seconds
print(sum([(60**((5-i)%3))*int(input())*int((i//3-0.5)*2.0) for i in range(6)]))

import seaborn as sns
ax = sns.regplot(x='input', y='output', data=df, color='green', marker='+')
