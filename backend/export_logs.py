import sqlite3
import csv

def export_chat_logs_to_csv(db_path='chat_logs.db', csv_path='chat_logs_export.csv'):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT timestamp, ip, user_input, ai_response FROM chat_logs")
        rows = cursor.fetchall()

        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'ip', 'user_input', 'ai_response'])
            writer.writerows(rows)

        print(f"Export successful! CSV saved as '{csv_path}'.")
    except Exception as e:
        print(f"Error exporting logs: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    export_chat_logs_to_csv()
