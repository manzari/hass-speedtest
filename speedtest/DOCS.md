# Home Assistant Community Add-on: Speedtest
The Home Assistant Speedtest add-on allows you to perform speedtests against [speedtest.net][speedtestnet]'s API.
The results will then be visible in Home Assistant as sensors.

**Homeassistant has an integration that covers all of this add-ons current functionality. Here you can find more Information about the [Speedtest.net Integration][speedtestnetintegration].**

## Installation
1. [Add the repository][addrepo] to homeassistant, if not done already
2. Update the add-on sources
3. Search for the "Speedtest" add-on and install it
4. Check the logs of the "Speedtest" add-on to see if any errors occurred

## Configuration
Example add-on configuration:
```yaml
interval: 240
```

### Option: `interval`
The `interval` option specifies the amount of minutes between two speed tests.
The default value `240` will perform tests every 4 hours.

## Support
You can [report an issue here][issue].

[issue]: https://github.com/manzari/hass-speedtest/issues
[speedtestnet]: https://www.speedtest.net/
[addrepo]: https://www.home-assistant.io/hassio/installing_third_party_addons/