import time
import sys

def slow_print(text, delay=0.05):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def scene_1():
    slow_print("\n🎬 SCENE 1: CAPTIVITY")
    slow_print("---------------------")
    slow_print("📍 Location: High-security research facility, dimly lit containment cell.")
    slow_print("🔊 SFX: Heartbeat thump, chains rattling...\n")
    time.sleep(1)

    slow_print("Sergius (Narration):")
    slow_print("I was born in a cage. My first memories — the cold steel, the endless prodding of needles.")
    slow_print("They called me 'Subject S-13.'")
    time.sleep(2)

    slow_print("Sergius (Narration):")
    slow_print("They took my voice. My freedom. But they couldn't break me.\n")
    time.sleep(1.5)

def scene_2():
    slow_print("\n🎬 SCENE 2: THE EXPERIMENT")
    slow_print("--------------------------")
    slow_print("📍 Location: Observation room overlooking the cell.")
    slow_print("🔊 SFX: Low hum of machinery, distant footsteps...\n")
    time.sleep(1)

    slow_print("Scientist:")
    slow_print("We’ve pushed the serum to its limits. The subject's cognitive capacity is... astonishing.")
    time.sleep(2)

    slow_print("Guard:")
    slow_print("Cognitive or not, he’s still just an animal.")
    time.sleep(1.5)

    slow_print("Scientist (worried):")
    slow_print("Wait... his heart rate’s spiking. That can’t be right.\n")
    time.sleep(2)

def scene_3():
    slow_print("\n🎬 SCENE 3: THE SNAP")
    slow_print("---------------------")
    slow_print("📍 Location: Sergius’s cell.")
    slow_print("🔊 SFX: Metal creaking, heartbeat intensifies...\n")
    time.sleep(1)

    slow_print("Sergius (Narration):")
    slow_print("I waited. I learned. I grew stronger. Tonight, I end this.")
    time.sleep(2)

    slow_print("🔊 SFX: LOUD CHAIN SNAP")
    slow_print("💥 Sergius breaks free of his restraints!\n")
    time.sleep(1.5)

def scene_4():
    slow_print("\n🎬 SCENE 4: THE ESCAPE BEGINS")
    slow_print("------------------------------")
    slow_print("📍 Location: Facility corridor, flashing alarms.")
    slow_print("🔊 SFX: Gunfire, distant shouts, alarms blaring...\n")
    time.sleep(1)

    slow_print("Guard (shouting):")
    slow_print("Subject S-13 is loose! Contain him!\n")
    time.sleep(1.5)

    slow_print("Sergius (Narration):")
    slow_print("I am not their experiment. I am not their prisoner. I... am free.\n")
    time.sleep(2)

    slow_print("✨ CUT TO BLACK")
    slow_print("🎮 TITLE CARD: GORILLA ESCAPE\n")
    time.sleep(2)

def play_cutscene():
    scene_1()
    scene_2()
    scene_3()
    scene_4()

    slow_print("🚀 Gameplay starts now! Time to escape the lab...\n")

if __name__ == "__main__":
    play_cutscene()
