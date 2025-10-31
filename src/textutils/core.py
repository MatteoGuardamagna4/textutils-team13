import re

def camel_to_snake(name: str) -> str:
    """
    Convert CamelCase / mixedCase identifiers to snake_case.
    Rules:
    - Insert '_' when a lowercase/digit is followed by an uppercase.
    - Split acronym runs: 'XMLHttp' -> 'XML_Http'.
    - Convert spaces or dashes to underscores.
    - Collapse repeated underscores; trim; lowercase.
    - Non-string or empty -> "".
    - Already snake_case is returned normalized (lower, single underscores).
    """
    if not isinstance(name, str) or not name:
        return ""

    s = name.strip()

    # Split acronym runs before a Capital+lower/digit:  XMLHTTP -> XML_HTTP,  URL2 -> URL2 (kept)
    s = re.sub(r'([A-Z]+)([A-Z][a-z0-9])', r'\1_\2', s)

    # Split lower/digit followed by Upper:  parseURL -> parse_URL
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s)

    # Treat spaces/dashes as word separators
    s = re.sub(r'[\s\-]+', '_', s)

    # Normalize multiple underscores
    s = re.sub(r'_+', '_', s).strip('_')

    return s.lower()
