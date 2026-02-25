import streamlit as st
import numpy as np
from scipy.stats import t

# ---------- Your T-Test Function ----------
def ttest(data, mu0, alpha=0.05, alternative="two-sided"):
    data = np.array(data)
    n = len(data)

    xbar = np.mean(data)
    s = np.std(data, ddof=1)

    se = s / np.sqrt(n)
    t_cal = (xbar - mu0) / se
    df = n - 1

    if alternative == "two-sided":
        t_crit = t.ppf(1 - alpha/2, df)
        p_value = 2 * (1 - t.cdf(abs(t_cal), df))
        reject = abs(t_cal) > t_crit

    elif alternative == "greater":
        t_crit = t.ppf(1 - alpha, df)
        p_value = 1 - t.cdf(t_cal, df)
        reject = t_cal > t_crit

    elif alternative == "less":
        t_crit = t.ppf(alpha, df)
        p_value = t.cdf(t_cal, df)
        reject = t_cal < t_crit

    return {
        "xbar": xbar,
        "s": s,
        "t_cal": t_cal,
        "df": df,
        "p_value": p_value,
        "decision": "Reject H0" if reject else "Fail to Reject H0"
    }

# ---------- Streamlit UI ----------
st.title("📊 One Sample T-Test Calculator")

st.write("Enter your dataset (comma separated):")

data_input = st.text_area("Dataset", "10, 12, 9, 11, 13")

mu0 = st.number_input("Null Hypothesis Mean (μ₀)", value=10.0)

alpha = st.selectbox("Significance Level (α)", [0.01, 0.05, 0.10], index=1)

alternative = st.selectbox(
    "Alternative Hypothesis",
    ["two-sided", "greater", "less"]
)

# ---------- Run Button ----------
if st.button("Run T-Test"):

    try:
        data = [float(x.strip()) for x in data_input.split(",")]

        if len(data) < 2:
            st.error("Dataset must contain at least 2 values.")
        else:
            result = ttest(data, mu0, alpha, alternative)

            st.success("T-Test Completed!")

            st.write("### Results")
            st.write(f"Sample Mean (x̄): {result['xbar']:.4f}")
            st.write(f"Sample Std Dev (s): {result['s']:.4f}")
            st.write(f"t Calculated: {result['t_cal']:.4f}")
            st.write(f"Degrees of Freedom: {result['df']}")
            st.write(f"p-value: {result['p_value']:.6f}")
            st.write(f"Decision: **{result['decision']}**")

    except:
        st.error("Invalid input. Please enter numbers separated by commas.")