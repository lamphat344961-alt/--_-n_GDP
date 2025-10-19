import pandas as pd

def filter_year_range(df, date_col, start_year=2010, end_year=2024):
    """
    Lọc dữ liệu trong khoảng năm [start_year, end_year].
    
    Tham số:
    ----------
    df : pd.DataFrame
        DataFrame cần lọc.
    date_col : str
        Tên cột ngày (có thể là datetime hoặc string).
    start_year : int
        Năm bắt đầu (mặc định 2010).
    end_year : int
        Năm kết thúc (mặc định 2024).

    Trả về:
    ----------
    df_filtered : pd.DataFrame
        DataFrame chỉ chứa các dòng trong khoảng năm mong muốn.
    """
    # Đảm bảo cột là datetime
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

    # Lọc theo năm
    df_filtered = df[
        (df[date_col].dt.year >= start_year) & 
        (df[date_col].dt.year <= end_year)
    ].copy()
    
    return df_filtered
