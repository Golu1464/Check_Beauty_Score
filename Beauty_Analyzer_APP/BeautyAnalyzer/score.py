def compute_overall_score(symmetry, golden_ratio):
    overall = 0.5 * symmetry + 0.5 * golden_ratio

    tips = []
    if symmetry > 85:
        tips.append("High facial symmetry ✅")
    elif symmetry > 65:
        tips.append("Moderate symmetry with slight asymmetry")
    else:
        tips.append("Significant asymmetry detected")

    if golden_ratio > 90:
        tips.append("Excellent Golden Ratio match ✅")
    elif golden_ratio > 70:
        tips.append("Slight deviation from ideal Golden Ratio")
    else:
        tips.append("Low match to Golden Ratio — unique facial structure")

    return overall, "\n".join(tips)