import logging
from bs4 import BeautifulSoup
from pelican import signals


logger = logging.getLogger(__name__)


def content_object_init(instance):
    if instance._content is not None:
        content = instance._content
        soup = BeautifulSoup(content, "html.parser")

        for img in soup("img"):
            logger.debug("image : %s", str(img))

            img["class"] = img.get("class", "") + " article-image"
        style = (
            "img.article-image{\n"
            "display: block; margin-left: auto;\n"
            "margin-right: auto; max-width: 100%;\n"
            "}"
        )
        tag = soup.new_tag("style")
        tag.append(style)
        soup.append(tag)
        instance._content = soup.decode()


def register():
    signals.content_object_init.connect(content_object_init)
