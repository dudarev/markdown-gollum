[Python-Markdown] plugin that adds handling of [Gollum style links]. Gollum is wiki used in Github projects.

Usage is similar to standard `markdown.extensions.wikilinks` extendsion:

```python
import markdown
from markdown_gollum import wikilinks

out = markdown.markdown(
    '[[link text|link reference]]',
    extensions=[
        wikilinks.WikiLinkExtension(
            base_url='', end_url='', html_class='')
    ]
)
print(out)  # <p><a href="link-reference">link text</a></p>
```

[Python-Markdown]: https://github.com/Python-Markdown/markdown
[Gollum style links]: https://github.com/gollum/gollum/wiki#link-tag
