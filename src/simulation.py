def simulate_performance(loans_df):
    import numpy as np
    import pandas as pd

    np.random.seed(42)
    performance = loans_df.copy()
    #700: acts like a "benchmark" credit score — borrowers around this score will have ~50% default probability before calibration
    #40: controls the steepness of the curve — a smaller number makes the change sharper
    performance['default_prob'] = 1 / (1 + np.exp(-(700 - performance['credit_score']) / 40))
    #0.3: baseline prepayment probability for low credit score borrowers
    #0.0005: linear penalty per credit score point — selected to gradually reduce prepayment probability as score increases
    performance['prepay_prob'] = 0.3 - 0.0005 * performance['credit_score']
    performance['defaulted'] = np.random.binomial(1, performance['default_prob'])
    performance['prepaid'] = np.random.binomial(1, performance['prepay_prob'].clip(0, 1))
    return performance