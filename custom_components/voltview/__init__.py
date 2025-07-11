"""VoltView custom component for Home Assistant."""

DOMAIN = "voltview"

async def async_setup(hass, config):
    """Set up the VoltView component."""
    hass.states.async_set(f"{DOMAIN}.status", "initialized")
    return True
