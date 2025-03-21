import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm  

def load_aggregate_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    
    df['date'] = pd.to_datetime(df['date'])
    if "indeed_job_postings_index_NSA" in df.columns:
        df.rename(columns={"indeed_job_postings_index_NSA": "job_postings"}, inplace=True)
    elif "indeed_job_postings_index" in df.columns:
        df.rename(columns={"indeed_job_postings_index": "job_postings"}, inplace=True)

    return df

def sarimax_forecast(df: pd.DataFrame, forecast_months=60):
    df = df.sort_values('date').copy()
    df.set_index('date', inplace=True)
    monthly_df = df['job_postings'].resample('M').mean().to_frame()
    monthly_df.dropna(inplace=True)

    model = sm.tsa.statespace.SARIMAX(
        monthly_df['job_postings'],
        order=(1, 1, 1),             # (p,d,q) 
        seasonal_order=(1, 0, 1, 12),# (P,D,Q,m) with m=12 for monthly seasonality
        enforce_stationarity=False,
        enforce_invertibility=False
    )
    results = model.fit(disp=False)

    forecast_object = results.get_forecast(steps=forecast_months)
    mean_forecast = forecast_object.predicted_mean
    conf_int = forecast_object.conf_int()

    forecast_df = pd.DataFrame({
        'forecast': mean_forecast,
        'lower_ci': conf_int.iloc[:, 0],
        'upper_ci': conf_int.iloc[:, 1]
    })
    
    return monthly_df, forecast_df

def plot_sarimax_forecast(monthly_df: pd.DataFrame, forecast_df: pd.DataFrame, output_path="OUTPUTS/sarimax_forecast.png"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    plt.figure(figsize=(10, 5))
    plt.plot(monthly_df.index, monthly_df['job_postings'], label='Historical', color='blue')
    plt.plot(forecast_df.index, forecast_df['forecast'], label='Forecast', color='orange', linestyle='--')
    
    # Confidence intervals
    plt.fill_between(
        forecast_df.index,
        forecast_df['lower_ci'],
        forecast_df['upper_ci'],
        color='orange', alpha=0.2,
        label='Confidence Interval'
    )

    plt.title('Monthly Job Postings Forecast (SARIMAX)')
    plt.xlabel('Date')
    plt.ylabel('Job Postings (Monthly Mean)')
    plt.legend()
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()

def run_time_series_forecast():
    csv_path = "DATA/aggregate_job_postings_US.csv"
    df = load_aggregate_data(csv_path)
    monthly_df, forecast_df = sarimax_forecast(df, forecast_months=60)
    
    output_plot = "OUTPUTS/job_postings_time_series_forecast.png"
    plot_sarimax_forecast(monthly_df, forecast_df, output_path=output_plot)

if __name__ == "__main__":
    run_time_series_forecast()
