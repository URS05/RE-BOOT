# --- TONIGHT'S REVIVAL WARMUP

engines = ["M54B30", "S54B32", "S65B40", "S85B50", "N55B30"]

performance_engines = [eng for eng in engines if eng.startswith("S")]

print("--- Performance Engines Filtered ---")
print(performance_engines)  
print("\n" + "="*30 + "\n")


print("--- Engine Lineup Deployment ---")
for index, engine in enumerate(performance_engines, start=1):
    
    print(f"Deployment Track {index:02d}: Processing {engine.lower()}...")

print("\nWarmup phase complete. Syntax memory unlocked.")