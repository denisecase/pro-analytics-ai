from pathlib import Path
from utils.logger import logger

def load_markdown_files(folder="backend/D_storage_layer/raw_docs") -> list[tuple[str, str]]:
    logger.info("Loading markdown files...")
    base = Path(folder)
    markdown_files = base.rglob("*.md")
    files = [(str(p.relative_to(base)), p.read_text(encoding="utf-8")) for p in markdown_files]
    logger.info(f"Loaded {len(files)} files.")
    return files
