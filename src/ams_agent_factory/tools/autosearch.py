from __future__ import annotations

from pathlib import Path


class AutoSearch:
    def __init__(self, wiki_dir: str | Path = "wiki"):
        self.wiki_dir = Path(wiki_dir)

    def search(self, query: str, depth: int = 2) -> list[dict[str, str]]:
        terms = [t.lower() for t in query.split() if len(t) > 2]
        hits = []
        for page in self.wiki_dir.rglob("*.md") if self.wiki_dir.exists() else []:
            rel_depth = len(page.relative_to(self.wiki_dir).parts) - 1
            if rel_depth > depth:
                continue
            text = page.read_text(errors="ignore")
            score = sum(text.lower().count(t) for t in terms)
            if score:
                hits.append({"path": str(page), "score": str(score), "snippet": text[:240].replace("\n", " ")})
        return sorted(hits, key=lambda x: int(x["score"]), reverse=True)
