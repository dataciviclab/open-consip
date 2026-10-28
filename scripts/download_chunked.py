"""Chunked download for large CONSIP CSVs using HTTP Range requests.

The CONSIP server drops connections for files > ~100MB. This script downloads
in chunks using HTTP Range headers, which the server supports (HTTP 206).

Usa il proxy delle fonti bloccate (``BLOCKED_SOURCE_PROXY``) se configurato:
``urllib`` legge ``HTTPS_PROXY``/``http_proxy``, non la variabile del Lab,
quindi senza questo il fallback proxy non coprirebbe i download via script.

Usage:
    python3 scripts/download_chunked.py <url> <output_file> [chunk_size_mb]

Called by toolkit script source type for large datasets.
"""
import os
import sys
import urllib.error
import urllib.request

DEFAULT_CHUNK_MB = 8
PROXY_ENV_VARS = ("BLOCKED_SOURCE_PROXY", "HTTPS_PROXY", "https_proxy")


def _build_opener() -> urllib.request.OpenerDirector:
    """Opener con il proxy delle fonti bloccate, se configurato."""
    proxy = next((os.environ[v] for v in PROXY_ENV_VARS if os.environ.get(v)), None)
    if not proxy:
        return urllib.request.build_opener()
    return urllib.request.build_opener(
        urllib.request.ProxyHandler({"http": proxy, "https": proxy})
    )


def get_file_size(url: str) -> int:
    req = urllib.request.Request(url, method="HEAD")
    with _build_opener().open(req, timeout=30) as resp:
        return int(resp.headers["Content-Length"])


def download_chunked(url: str, dest: str, chunk_mb: int = DEFAULT_CHUNK_MB) -> None:
    total = get_file_size(url)
    chunk_size = chunk_mb * 1024 * 1024
    downloaded = 0
    opener = _build_opener()

    with open(dest, "wb") as f:
        while downloaded < total:
            end = min(downloaded + chunk_size - 1, total - 1)
            req = urllib.request.Request(url)
            req.add_header("Range", f"bytes={downloaded}-{end}")

            for attempt in range(3):
                try:
                    with opener.open(req, timeout=120) as resp:
                        data = resp.read()
                        f.write(data)
                        downloaded += len(data)
                        pct = downloaded * 100 // total
                        print(f"  {pct}% ({downloaded}/{total} bytes)", flush=True)
                        break
                except (urllib.error.URLError, OSError) as e:
                    if attempt == 2:
                        raise
                    print(f"  retry {attempt + 1}: {e}", file=sys.stderr)

    print(f"  OK: {downloaded} bytes -> {dest}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <url> <output_file> [chunk_size_mb]")
        sys.exit(1)
    url = sys.argv[1]
    dest = sys.argv[2]
    chunk_mb = int(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_CHUNK_MB
    download_chunked(url, dest, chunk_mb)
