import dowhy
from dowhy import CausalModel
import pandas as pd

# 데이터 로드
data = pd.read_csv('data.csv')

# 인과 모델 정의
model = CausalModel(
    data=data,
    treatment='A2M',  # 예시로 특정 유전자를 원인으로 설정
    outcome='SUBCLASS',
    graph="dag { A2M -> SUBCLASS; }"
)

# 인과 모델 식별
identified_estimand = model.identify_effect()

# 인과 효과 추정
estimate = model.estimate_effect(identified_estimand,
                                 method_name="backdoor.propensity_score_matching")

# 결과 해석
print(estimate)
model.view_model()

# 반사실적 추론
refute_results = model.refute_estimate(identified_estimand, estimate, method_name="placebo_treatment_refuter")
print(refute_results)
