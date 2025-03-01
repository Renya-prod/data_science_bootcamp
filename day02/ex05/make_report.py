import sys
from analytics import Research
import config

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 make_report.py file")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        research = Research(file_path)
        data = research.file_reader()

        analytics = Research.Analytics(data)
        heads, tails = analytics.counts()
        head_percent, tail_percent = analytics.fractions(heads, tails)

        predictions = analytics.predict_random(config.num_of_steps)
        predicted_heads = sum(pred[0] for pred in predictions)
        predicted_tails = sum(pred[1] for pred in predictions)

        report = config.report_template.format(
            total=len(data),
            tails=tails,
            heads=heads,
            tail_percent=tail_percent,
            head_percent=head_percent,
            steps=config.num_of_steps,
            predicted_tails=predicted_tails,
            predicted_heads=predicted_heads
        )
        print(report)

        analytics.save_file(report, "report", "txt")

    except Exception as e:
        print(f"Error: {e}")
