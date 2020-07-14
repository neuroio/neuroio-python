from enum import Enum

API_BASE_URL: str = "https://api.neuroio.com"
HTTP_CLIENT_TIMEOUT: float = 4.0


sentinel = object()


class SourceLicense(str, Enum):
    BASIC = "basic"
    STANDARD = "standard"
    STANDARD_PLUS = "standard+"
    ADVANCED = "advanced"


class EntryResult(str, Enum):
    NEW = "new"
    REINIT = "reinit"
    EXACT = "exact"
    HA = "ha"
    JUNK = "junk"
    NM = "nm"
    DET = "det"
