def simulate_performance(loans_df):
    import numpy as np
    import pandas as pd

    np.random.seed(42)
    performance = loans_df.copy()
    performance['default_prob'] = 1 / (1 + np.exp(-(700 - performance['credit_score']) / 40))
    performance['prepay_prob'] = 0.3 - 0.0005 * performance['credit_score']
    performance['defaulted'] = np.random.binomial(1, performance['default_prob'])
    performance['prepaid'] = np.random.binomial(1, performance['prepay_prob'].clip(0, 1))
    return performance