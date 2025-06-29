def generate_synthetic_loans(n=1000):
    import pandas as pd
    import numpy as np

    data = pd.DataFrame({
        'loan_id': range(n),
        'credit_score': np.random.normal(680, 50, n).astype(int),
        'loan_amount': np.random.normal(25000, 10000, n).clip(5000, 100000),
        'interest_rate': np.random.uniform(0.03, 0.12, n),
        'term_months': np.random.choice([36, 60], n),
        'income': np.random.normal(75000, 20000, n),
        'employment_length': np.random.randint(0, 20, n)
    })
    return data
