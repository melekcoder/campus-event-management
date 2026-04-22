# events.py
from data_store import events, students, reservations

def add_event(code, name, club, date, time, room, capacity):
    reservation_key = (room, date, time)

    if reservation_key in reservations:
        print("Bu oda, tarih ve saatte başka bir etkinlik var.")
        return

    events[code] = {
        "name": name,
        "club": club,
        "date": (date, time),
        "room": room,
        "capacity": capacity,
        "participants": set()
    }

    reservations.add(reservation_key)
    print(f"{code} kodlu etkinlik oluşturuldu.")

def register(id, event_code):
    if id not in students:
        print("Öğrenci bulunamadı.")
        return

    if event_code not in events:
        print("Etkinlik bulunamadı.")
        return

    event = events[event_code]
    student = students[id]

    if len(event["participants"]) >= event["capacity"]:
        print("Etkinlik kapasitesi dolu.")
        return

    if id in event["participants"]:
        print("Öğrenci zaten kayıtlı.")
        return

    event["participants"].add(id)
    student["events"].add(event_code)

    print(f"{id} numaralı öğrenci {event_code} etkinliğine kaydedildi.")

def cancel_registration(id, event_code):
    if event_code not in events or id not in students:
        print("Geçersiz öğrenci veya etkinlik.")
        return

    events[event_code]["participants"].discard(id)
    students[id]["events"].discard(event_code)

    print("Kayıt iptal edildi.")

def list_events():
    return list(events.values())
