# reports.py
from data_store import students, events

def popular_events():
    return sorted(
        events.items(),
        key=lambda item: len(item[1]["participants"]),
        reverse=True
    )

def active_students():
    return sorted(
        students.items(),
        key=lambda item: len(item[1]["events"]),
        reverse=True
    )

def club_statistics():
    stats = {}

    for event in events.values():
        club = event["club"]
        participant_count = len(event["participants"])

        if club not in stats:
            stats[club] = {
                "event_count": 0,
                "participants": 0
            }

        stats[club]["event_count"] += 1
        stats[club]["participants"] += participant_count

    return stats
