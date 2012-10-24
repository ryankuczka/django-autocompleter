from django.conf import settings

# Basic set up
REDIS_CONNECTION = getattr(settings, 'AUTOCOMPLETER_REDIS_CONNECTION', {})

SUGGEST_PARAMETER_NAME = getattr(settings, 'AUTOCOMPLETER_SUGGEST_PARAMETER_NAME', 'q')

CACHE_TIMEOUT = getattr(settings, 'AUTOCOMPLETER_CACHE_TIMEOUT', 0)

# Storing / Matching
CHARACTER_FILTER = getattr(settings, 'AUTOCOMPLETER_CHARACTER_FILTER', r'[^a-z0-9_ ]')

MAX_RESULTS = getattr(settings, 'AUTOCOMPLETER_MAX_RESULTS', 10)  # AC/Provider override possible

MOVE_EXACT_MATCHES_TO_TOP = getattr(settings, 'AUTOCOMPLETER_MOVE_EXACT_MATCHES_TO_TOP', False)

FLATTEN_SINGLE_TYPE_RESULTS = getattr(settings, 'AUTOCOMPLETER_FLATTEN_SINGLE_TYPE_RESULTS', True)
