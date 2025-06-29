def test_simulation_outputs():
    from src.data_ingestion import generate_synthetic_loans
    from src.simulation import simulate_performance
    df = generate_synthetic_loans(100)
    result = simulate_performance(df)
    assert 'defaulted' in result.columns
    assert 'prepaid' in result.columns
    assert result.shape[0] == 100
