import pandas as pd
#  import folium

ctx = '../data/'

pop_data = pd.read_excel(ctx+'population_in_Seoul.xls'
                         , encoding='UTF-8'
                         , header=2
                         , usecols='B,D,G,J,N')
cctv_data = pd.read_csv(ctx+'CCTV_in_Seoul.csv')

cctv_data_schema = cctv_data.columns
pop_data_schema = pop_data.columns

"""
cctv_data_schema
['구별', '소계', '2013년도 이전', '2014년', '2015년', '2016년']

pop_data_schema
['구별', '인구수', '한국인', '외국인', '고령자']
"""

cctv_data.rename(columns={cctv_data.columns[0]: '구별'}, inplace=True)
# inplace=True 실제 변수의 내용을 바꿔라


pop_data.rename(columns={pop_data.columns[0]:'구별'
                         , pop_data.columns[1]:'인구수'
                         , pop_data.columns[2]:'한국인'
                         , pop_data.columns[3]:'외국인'
                         , pop_data.columns[4]:'고령자'}
                , inplace=True)
print(pop_data.columns)