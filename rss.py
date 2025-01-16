from pathlib import Path
import jinja2
from typing import Any

root_dir = Path(__file__).parent
template_path = root_dir / "template.rss.jinja"
result_rss_path = root_dir / "releases.rss"

channel = dict(
    title="DF releases and betas",
    link="https://store.steampowered.com/news/app/975370?updates=true",
    description="DF releases and betas on steam",
)


def write_rss(post: dict[str, Any]) -> str:
    template_text = template_path.read_text(encoding="utf-8")
    template = jinja2.Template(template_text)
    rendered = template.render(
        dict(
            channel=channel,
            items=[
                dict(
                    title=post["title"],
                    date=post["date"],
                    link=post["url"],
                    description=post["contents"],
                    guid=post["gid"],
                ),
            ],
        ),
    )
    result_rss_path.write_text(rendered, encoding="utf-8")
