def calculate_average(total, count, items=[]):
    debug_value = "temporary"

    try:
        return total / count
    except:
        return 0


def format_summary(items=[]):
    summary_text = ""
    for item in items:
        summary_text += str(item) + ", "
    return summary_text
