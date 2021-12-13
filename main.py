import pandas as pd
import matplotlib.pyplot as plt

School_meal_data = pd.read_csv("한국농수산식품유통공사_학교급식계약정보_12_31_2020.csv",encoding='cp949')

#한글 출력 오류 수정하는 폰트
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# # 급식계약금액의 최고,최소 5개 계약금액 찾기, 코드오류로 나머지 주석처리 후 실행
# tp = School_meal_data["계약금액"]
# tp1 = School_meal_data["계약명"]
#
# for n in range(10):
#     Mx_tp = tp.idxmax()
#     print(Mx_tp)
#     print(tp1[Mx_tp])
#     print(tp[Mx_tp])
#     del tp[Mx_tp]
# print(tp)
#
# print("======================================================")
#
# for n in range(10):
#     Mx_tp = tp.idxmin()
#     print(Mx_tp)
#     print(tp1[Mx_tp])
#     print(tp[Mx_tp])
#     del tp[Mx_tp]
# print(tp)

#급식계약금액의 최고 계약금액 찾기
max_contract = School_meal_data[["계약명","계약금액"]].max()
print("급식계약금액의 최대값",'\n', max_contract)
print("======================================================")

#급식계약금액의 최소 계약금액 찾기
min_contract = School_meal_data[["계약명","계약금액"]].min()
print("급식계약금액의 최솟값",'\n', min_contract)
print("======================================================")

#급식계약금액의 평균값
average = School_meal_data["계약금액"].mean()
print("평균금액 : ", average)
print("======================================================")

#급식계약의 중간값
medium_value = School_meal_data["계약금액"].median()
print("계약금액의 중간값", medium_value)
print("======================================================")

#지역별 학교의 수
Num_school_region = School_meal_data["구매사시도명"].value_counts()
print(Num_school_region)
print("======================================================")

#지역별 계약금액의 평균
Aver_by_region = School_meal_data.groupby(["구매사시도명"])["계약금액"].mean()
print(Aver_by_region)
print("======================================================")

#지역별 계약금액의 평균의 그래프
School_meal_data.groupby('구매사시도명')['계약금액'].nunique().plot(kind='bar')
plt.show()

#계약금액과 변경계약차수의 관계
ax = plt.gca()
School_meal_data.plot(kind='line',x='구매사시도명',y='계약금액',ax=ax)
School_meal_data.plot(kind='line',x='구매사시도명',y='변경계약차수', color='red', ax=ax)
plt.show()