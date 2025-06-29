def generate_report(simulation_df):
    summary = simulation_df[['defaulted', 'prepaid']].mean()
    print("--- Simulation Summary ---")
    print(f"Default Rate: {summary['defaulted']:.2%}")
    print(f"Prepayment Rate: {summary['prepaid']:.2%}")
    return summary