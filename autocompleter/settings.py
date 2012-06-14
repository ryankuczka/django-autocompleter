from django.conf import settings

DEFAULT_NAME = "main"

# Basic set up
REDIS_CONNECTION = getattr(settings, 'AUTOCOMPLETER_REDIS_CONNECTION', {})

SUGGEST_PARAMETER_NAME = getattr(settings, 'AUTOCOMPLETER_SUGGEST_PARAMETER_NAME', 'q')

# Matching
MAX_RESULTS = getattr(settings, 'AUTOCOMPLETER_MAX_RESULTS', 10)

MAX_NUM_WORDS = getattr(settings, 'AUTOCOMPLETER_MAX_NUM_WORDS', None)

MOVE_EXACT_MATCHES_TO_TOP = getattr(settings, 'AUTOCOMPLETER_MOVE_EXACT_MATCHES_TO_TOP', True)

MATCH_OUT_OF_ORDER = getattr(settings, 'AUTOCOMPLETER_MATCH_OUT_OF_ORDER', False)

CHARACTER_FILTER = getattr(settings, 'AUTOCOMPLETER_CHARACTER_FILTER', r'[^a-z0-9_ ]')
