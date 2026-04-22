# demo.py

from students import add_student
from events import add_event, register
from reports import popular_events, active_students, club_statistics

print("=== ÖĞRENCİ EKLEME ===")
# İsimler güncellendi, ilgi alanları OOP temasına uygun bırakıldı
add_student("2407231077", "Melek Efe", "Makine", 2, ["OOP", "Müzik"])
add_student("2407231001", "AYŞE Demir", "Bilgisayar", 3, ["OOP"])
add_student("2407231002", "Mehmet Ege", "Endüstri", 1, ["Java"])

print("\n=== ETKİNLİK OLUŞTURMA ===")
add_event("OOP101", "Nesne Yönelimli Programlama", "Yazılım", "2025-12-23", "14:00", "bilgisayar lab", 1)
add_event("DP202", "Tasarım Desenleri Atölyesi", "Yazılım", "2025-12-27", "12:00", "D-101", 70)

print("\n=== ETKİNLİK KAYITLARI ===")
register("2407231077", "OOP101")
register("2407231001", "OOP101")
register("2407231002", "DP202")
register("2407231077", "DP202")

print("\n=== RAPORLAR ===")

print("\nEn Popüler Etkinlikler:")
for code, event in popular_events():
    print(code, "-", len(event["participants"]), "katılımcı")

print("\nEn Aktif Öğrenciler:")
for id, student in active_students():
    print(id, "-", len(student["events"]), "etkinlik")

print("\nKulüp İstatistikleri:")
stats = club_statistics()
for club, info in stats.items():
    print(club, "->", info)