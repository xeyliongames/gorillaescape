import subprocess
import time

def run_script(script_name):
    """Run a Python script as a separate process."""
    try:
        print(f"\n🔹 Running {script_name}...\n")
        process = subprocess.Popen(["python", script_name], shell=True)
        process.wait()  # Wait for the process to finish
    except KeyboardInterrupt:
        print(f"\n❌ {script_name} interrupted. Exiting...")
        process.terminate()

def main():
    print("\n🎮 WELCOME TO GORILLA ESCAPE\n")
    print("Prepare for your escape...\n")
    time.sleep(2)

    # Run the cutscene
    run_script("gorilla_escape_cutscene.py")

    # Generate Sergius's 3D model
    run_script("sergius_model.py")

    # Load the lab level
    run_script("lab_level.py")

    # Show attack animation pose
    run_script("attack_pose.py")

    print("\n✅ Game setup complete! Ready for live gameplay.\n")
    print("🚀 Next step: Implement real-time interaction or move to a game engine!\n")

if __name__ == "__main__":
    main()
