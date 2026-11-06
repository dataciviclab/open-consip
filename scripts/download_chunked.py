"""Chunked download for large CONSIP CSVs using HTTP Range requests.

The CONSIP server drops connections for files > ~100MB. This script downloads
in chunks using HTTP Range headers, which the server supports (HTTP 206).

Il proxy delle fonti bloccate (``BLOCKED_SOURCE_PROXY``) è gestito da
``HttpClient`` come fallback automatico.

Usage:
    python3 scripts/download_chunked.py <url> <output_file> [chunk_size_mb]

Called by toolkit script source type for large datasets.
"""
import sys

from lab_connectors.http import HttpClient

DEFAULT_CHUNK_MB = 8


def get_file_size(url: str) -> int:
    """Content-Length via HEAD (HttpClient: retry + fallback proxy/SSL)."""
    result = HttpClient(timeout=30).head(url)
    resp = result.response
    if resp is None or resp.status_code >= 400 or "Content-Length" not in resp.headers:
        raise RuntimeError(f"Content-Length non disponibile per {url}: {result.err}")
    return int(resp.headers["Content-Length"])


def download_chunked(url: str, dest: str, chunk_mb: int = DEFAULT_CHUNK_MB) -> None:
    total = get_file_size(url)
    chunk_size = chunk_mb * 1024 * 1024
    downloaded = 0
    client = HttpClient(timeout=120, max_retries=3)

    with open(dest, "wb") as f:
        while downloaded < total:
            end = min(downloaded + chunk_size - 1, total - 1)
            headers = {"Range": f"bytes={downloaded}-{end}"}

            for attempt in range(3):
                result = client.get(url, headers=headers)
                resp = result.response
                if resp is not None and resp.status_code in (200, 206):
                    data = resp.content
                    f.write(data)
                    downloaded += len(data)
                    pct = downloaded * 100 // total
                    print(f"  {pct}% ({downloaded}/{total} bytes)", flush=True)
                    break
                if attempt == 2:
                    status = resp.status_code if resp is not None else "no response"
                    raise RuntimeError(f"Range {downloaded}-{end} fallito: HTTP {status} ({result.err})")
                print(f"  retry {attempt + 1}: {result.err}", file=sys.stderr)

    print(f"  OK: {downloaded} bytes -> {dest}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <url> <output_file> [chunk_size_mb]")
        sys.exit(1)
    url = sys.argv[1]
    dest = sys.argv[2]
    chunk_mb = int(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_CHUNK_MB
    download_chunked(url, dest, chunk_mb)
