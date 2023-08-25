import pandas as pd

def substitute_full_state_name(state, name='Washington'):
    if state[0] == 'W':
        return name
    else:
        return state

def grab_first_letter(state):
    return state[0]

df_one = pd.DataFrame({'k1':['A','A','B','B','C','C'],
                        'col1':[100,200,300,300,400,500],
                        'col2':['NY','CA','WA','WA','AK','NV']})


print('DataFrame')
print(df_one)

#Find unique values in column col2
print('\nUnique values in col2 = ',df_one['col2'].unique())

print('\nRemove duplicate values')
print(df_one.drop_duplicates())

print('\nAdd a new column of data derived from the first letter of each state in col2')
df_one['first letter'] = df_one['col2'].apply(grab_first_letter)
print(df_one)

print('\nIn col2 replace WA with Washington')
df_one['col2'] = df_one['col2'].apply(substitute_full_state_name)
print(df_one)


