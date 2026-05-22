"""
Annualized Revenue Lift Calculator

Estimates the annualized revenue impact of a conversion rate improvement
observed during an A/B test. Given test duration, sessions, conversions,
average order value, and an expected lift percentage, the script projects
baseline and improved annual revenue and reports the incremental difference.
"""

# Key assumption: test-window traffic volume and conversion behavior are
# representative of the full year — no seasonality adjustment is applied.


def get_float(prompt, allow_zero=False):
    while True:
        raw = input(prompt).strip().replace(",", "").replace("$", "")
        try:
            value = float(raw)
        except ValueError:
            print("  Please enter a valid number.")
            continue
        if value < 0:
            print("  Value cannot be negative.")
            continue
        if not allow_zero and value == 0:
            print("  Value must be greater than zero.")
            continue
        return value


def get_lift(prompt):
    while True:
        raw = input(prompt).strip().replace("%", "").replace(",", "")
        try:
            value = float(raw)
        except ValueError:
            print("  Please enter a valid number (e.g. 10 or 10%).")
            continue
        if value < 0:
            print("  Lift cannot be negative.")
            continue
        return value


def main():
    print("=" * 55)
    print("   Annualized Revenue Lift Calculator")
    print("=" * 55)
    print()

    duration = get_float("Test duration (days): ")
    sessions = get_float("Total sessions during test: ")
    conversions = get_float("Total conversions during test: ", allow_zero=True)
    aov = get_float("Average order value (AOV) in $: ")
    lift_pct = get_lift("Expected lift (e.g. 10 for 10%): ")

    if conversions > sessions:
        print("\nError: conversions cannot exceed sessions.")
        return

    # Core calculations
    baseline_cr = conversions / sessions
    projected_cr = baseline_cr * (1 + lift_pct / 100)
    daily_sessions = sessions / duration
    annual_sessions = daily_sessions * 365
    baseline_revenue = annual_sessions * baseline_cr * aov
    projected_revenue = annual_sessions * projected_cr * aov
    incremental_revenue = projected_revenue - baseline_revenue
    incremental_conversions = annual_sessions * (projected_cr - baseline_cr)

    # Output
    print()
    print("=" * 55)
    print("  INPUTS")
    print("=" * 55)
    print(f"  Test duration:          {duration:,.0f} days")
    print(f"  Total sessions:         {sessions:>15,.0f}")
    print(f"  Total conversions:      {conversions:>15,.0f}")
    print(f"  Average order value:    ${aov:>14,.2f}")
    print(f"  Expected lift:          {lift_pct:>14.2f}%")

    print()
    print("=" * 55)
    print("  BASELINE (NO LIFT)")
    print("=" * 55)
    print(f"  Baseline conv. rate:    {baseline_cr * 100:>14.2f}%")
    print(f"  Daily sessions:         {daily_sessions:>15,.1f}")
    print(f"  Annualized sessions:    {annual_sessions:>15,.0f}")
    print(f"  Baseline annual rev:    ${baseline_revenue:>14,.2f}")

    print()
    print("=" * 55)
    print("  PROJECTED (WITH LIFT)")
    print("=" * 55)
    print(f"  Projected conv. rate:   {projected_cr * 100:>14.2f}%")
    print(f"  Projected annual rev:   ${projected_revenue:>14,.2f}")

    print()
    print("=" * 55)
    print("  INCREMENTAL LIFT")
    print("=" * 55)
    print(f"  Incremental annual rev: ${incremental_revenue:>14,.2f}")
    print(f"  Incremental conversions:{incremental_conversions:>15,.0f}")
    print("=" * 55)


if __name__ == "__main__":
    main()
