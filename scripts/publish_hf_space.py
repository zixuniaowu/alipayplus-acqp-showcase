from __future__ import annotations

import argparse
import os
from pathlib import Path

from huggingface_hub import HfApi, get_token, upload_folder


ROOT = Path(__file__).resolve().parents[1]


def resolve_token() -> str | None:
    for name in ("HF_TOKEN", "HUGGINGFACEHUB_API_TOKEN", "HUGGINGFACE_TOKEN"):
        value = os.getenv(name)
        if value:
            return value
    return get_token()


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish this repository as a Hugging Face static Space.")
    parser.add_argument("--repo-id", required=True, help="Target Space repo id, for example user/space-name")
    parser.add_argument("--private", action="store_true", help="Create the Space as private")
    args = parser.parse_args()

    token = resolve_token()
    if not token:
        raise SystemExit(
            "No Hugging Face token found. Set HF_TOKEN, HUGGINGFACEHUB_API_TOKEN, or HUGGINGFACE_TOKEN first."
        )

    api = HfApi(token=token)
    api.create_repo(
        repo_id=args.repo_id,
        repo_type="space",
        private=args.private,
        space_sdk="static",
        exist_ok=True,
    )

    upload_folder(
        repo_id=args.repo_id,
        repo_type="space",
        folder_path=str(ROOT),
        token=token,
        ignore_patterns=[
            ".git/*",
            ".gitignore",
            "report/browser-qa-*",
            "__pycache__/*",
        ],
    )

    print(f"Published to https://huggingface.co/spaces/{args.repo_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
