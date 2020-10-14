import sys
import subprocess


def prepare_venv():
    print("Prepare virtual env.")
    subprocess.check_call([sys.executable, "-m", "venv", "venv"])
    subprocess.check_call(["venv/bin/pip", "install", "--upgrade", "-q", "pip"])
    subprocess.check_call(["venv/bin/pip", "install", "--disable-pip-version-check", "-q", "-r", "build-requirements.txt"])
    print("Virtual env prepared.")

if __name__ == '__main__':
    prepare_venv()
