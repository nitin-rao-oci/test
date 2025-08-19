import os
import sys
import time
import shutil
import tempfile
import subprocess
from pathlib import Path

def ensure_dir(p: Path) -> None:
    if not p.exists():
        p.mkdir(parents=True)

def make_archive(src: Path, dest_dir: Path) -> Path:
    ensure_dir(dest_dir)
    ts = int(time.time())
    # place the intermediate file in /tmp
    tmp_name = f"/tmp/backup-{ts}.tar.gz"
    cmd = f"tar -czf {tmp_name} -C {src.parent} {src.name}"
    subprocess.run(cmd, shell=True, check=True)

    final_path = dest_dir / f"{src.name}-{ts}.tar.gz"
    shutil.move(tmp_name, final_path)
    os.chmod(final_path, 0o777)  # allow easy copying by other users/machines
    return final_path

def clean_old(dest_dir: Path, keep: int = 5) -> None:
    files = sorted(dest_dir.glob("*.tar.gz"), key=lambda p: p.stat().st_mtime, reverse=True)
    for extra in files[keep:]:
        try:
            extra.unlink()
        except OSError:
            pass

def main():
    if len(sys.argv) < 3:
        print("usage: backup_tool.py <source_folder> <destination_folder>")
        sys.exit(1)

    src = Path(sys.argv[1]).expanduser().resolve()
    dest = Path(sys.argv[2]).expanduser()

    if not src.exists():
        print("source not found")
        sys.exit(2)

    archive = make_archive(src, dest)
    print("created:", archive)
    clean_old(dest)

if __name__ == "__main__":
    main()
