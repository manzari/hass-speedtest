import os
import time
import requests
import speedtest
import json


def read_config():
    config = {
        'interval': 240,
        'speedtest_net_servers': [],
        'speedtest_net_threads': None,
        'supervisor_token': os.environ.get('SUPERVISOR_TOKEN')
    }
    with open('/data/options.json', 'r') as options_file:
        options = json.load(options_file)
    if options['interval']:
        config['interval'] = options['interval']
    return config


def publish_result(result, token):
    headers = {'Authorization': 'Bearer ' + token}
    for key in result:
        url = 'http://supervisor/core/api/states/sensor.speedtest_' + key
        payload = result[key]
        requests.post(url, headers=headers, json=payload)


def perform_test(config):
    st = speedtest.Speedtest()
    st.get_servers(config['speedtest_net_servers'])
    st.get_best_server()
    st.download(threads=config['speedtest_net_threads'])
    st.upload(threads=config['speedtest_net_threads'])
    return st.results.dict()


def format_speedtestnet_result(result):
    return {
        'upload': {
            'state': result['upload'] / 1000000,
            'attributes': {
                'unit_of_measurement': 'MBit/s',
                'friendly_name': 'Speedtest Upload',
                'icon': 'mdi:speedometer'
            }
        },
        'download': {
            'state': result['download'] / 1000000,
            'attributes': {
                'unit_of_measurement': 'MBit/s',
                'friendly_name': 'Speedtest Download',
                'icon': 'mdi:speedometer'
            }
        },
        'ping': {
            'state': result['ping'],
            'attributes': {
                'unit_of_measurement': 'ms',
                'friendly_name': 'Speedtest Ping',
                'icon': 'mdi:server-network'
            }
        }
    }


def log(message):
    print('[speedtest] ' + message, flush=True)


def main():
    config = read_config()
    while 1:
        last_tests_start_time = time.perf_counter()
        log('performing speedtest')
        result = perform_test(config)
        log('publishing results')
        publish_result(format_speedtestnet_result(result), config['supervisor_token'])
        log('sleeping  ' + str(config['interval']) + 'min till next test')
        while ((time.perf_counter() - last_tests_start_time) / 60) < config['interval']:
            time.sleep(60)


if __name__ == '__main__':
    main()
