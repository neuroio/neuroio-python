API_BASE_URL: str = "https://api.neuroio.com"
HTTP_CLIENT_TIMEOUT: float = 4.0


sentinel = object()


class SourceLicense:
    BASIC: str = "basic"
    STANDARD: str = "standard"
    STANDARD_PLUS: str = "standard+"
    ADVANCED: str = "advanced"


class EntryResult:
    NEW: str = "new"
    REINIT: str = "reinit"
    EXACT: str = "exact"
    HA: str = "ha"
    JUNK: str = "advanced"
    NM: str = "nm"
    DET: str = "dev"
