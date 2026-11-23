from pathlib import Path
import shutil


Path("/output").mkdir(parents=True, exist_ok=True)
shutil.copyfile(Path(__file__).with_name("entry.png"), "/output/entry.png")
