PROVIDER_REGISTRY = {}

class ProviderRegistry(object):

    def register_provider(name):
        def decorator(cls):
            PROVIDER_REGISTRY[name.lower()] = cls
            return cls
        return decorator

    def get_provider(name):
        provider = PROVIDER_REGISTRY.get(name.lower())
        if not provider:
            raise ValueError(f"Provider '{name}' not found. Available: {list(PROVIDER_REGISTRY.keys())}")
        return provider