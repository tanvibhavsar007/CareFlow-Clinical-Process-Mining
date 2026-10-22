import pandas as pd


def load_event_log(csv_path):
    df = pd.read_csv(csv_path)

    required_columns = [
        "case_id",
        "activity",
        "timestamp",
        "sequence"
    ]

    missing = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing columns: {missing}"
        )

    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    return df


def get_overview_metrics(df):
    return {
        "total_patients": int(
            df["case_id"].nunique()
        ),
        "total_events": int(len(df)),
        "total_activities": int(
            df["activity"].nunique()
        )
    }


def get_activity_counts(df):
    return (
        df["activity"]
        .value_counts()
        .rename_axis("activity")
        .reset_index(name="event_count")
    )


def get_patient_paths(df):
    df = df.sort_values(
        ["case_id", "timestamp", "sequence"]
    )

    return (
        df.groupby("case_id")["activity"]
        .apply(list)
        .reset_index(name="patient_path")
    )


def get_data_quality(df):
    return {
        "total_rows": int(len(df)),
        "missing_values": int(
            df.isnull().sum().sum()
        ),
        "duplicate_rows": int(
            df.duplicated().sum()
        )
    }