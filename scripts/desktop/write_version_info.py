from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path


def load_metadata(root: Path):
    meta_path = root / "apps" / "desktop" / "meta.py"
    spec = importlib.util.spec_from_file_location("stt_windows_meta", meta_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load desktop metadata: {meta_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def version_tuple(version: str) -> tuple[int, int, int, int]:
    parts = [int(part) for part in version.split(".")]
    if len(parts) > 4:
        raise ValueError(f"Windows version has more than four components: {version}")
    return tuple((parts + [0] * 4)[:4])


def render_version_info(meta) -> str:
    version = str(meta.APP_VERSION)
    numbers = ", ".join(str(part) for part in version_tuple(version))
    values = {
        "company": repr(str(meta.APP_COMPANY)),
        "description": repr(str(meta.APP_DESCRIPTION)),
        "name": repr(str(meta.APP_NAME)),
        "filename": repr(f"{meta.APP_NAME}.exe"),
        "version": repr(version),
    }
    return f"""VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({numbers}),
    prodvers=({numbers}),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo([
      StringTable(
        '040904B0',
        [
          StringStruct('CompanyName', {values['company']}),
          StringStruct('FileDescription', {values['description']}),
          StringStruct('FileVersion', {values['version']}),
          StringStruct('InternalName', {values['name']}),
          StringStruct('OriginalFilename', {values['filename']}),
          StringStruct('ProductName', {values['name']}),
          StringStruct('ProductVersion', {values['version']})
        ]
      )
    ]),
    VarFileInfo([VarStruct('Translation', [1033, 1200])])
  ]
)
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_version_info(load_metadata(root)), encoding="utf-8")
    print(f"Generated version metadata: {output}")


if __name__ == "__main__":
    main()
