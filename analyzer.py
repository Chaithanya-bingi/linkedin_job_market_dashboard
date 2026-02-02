def analyze_trends(df):
    trend = df["Job Role"].value_counts()
    return trend
