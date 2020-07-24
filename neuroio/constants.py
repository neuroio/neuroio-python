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


class EntryMood(str, Enum):
    NEUTRAL = "neutral"
    ANGER = "anger"
    CONTEMPT = "contempt"
    DISGUST = "disgust"
    FEAR = "fear"
    HAPPINESS = "happiness"
    SADNESS = "sadness"
    SURPRISE = "surprise"
    NM = "nm"
    DET = "det"


class EntryLiveness(str, Enum):
    PASSED = "passed"
    FAILED = "failed"
    UNDETERMINED = "undetermined"


DEFAULT_EXACT_THRESHOLD = 79.3
DEFAULT_HA_THRESHOLD = 75.5
DEFAULT_JUNK_THRESHOLD = 68.84
