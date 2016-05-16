import json, io


def write_json_subruns():
    d = {
        # STRICTLY FOR SUBSYSTEM DATA, NOT FOR EVENT VIEW.
        'sort_keys': [
            {
                'set_values': {'x': 'channel',
                               'y': 'UNKNOWN',
                               'type': 'histogram',
                               'function': 'mean',
                               'dimension': 2,
                               'system': 'adc',
                               'sub_system': 'rce'},
                'search_value': 'ADCMeanChannel',
            },

            {
                'set_values': {'x': 'channel',
                               'y': 'UNKNOWN',
                               'type': 'histogram',
                               'function': 'rms',
                               'dimension': 2,
                               'system': 'adc',
                               'sub_system': 'rce'},
                'search_value': 'ADCRMSChannel'
            },

            {
                'set_values': {'x': 'channel',
                               'y': 'UKNOWN',
                               'function': 'UKNOWN',
                               'type': 'histogram',
                               'dimension': 2,
                               'system': 'UKNOWN',
                               'sub_system': None},
                'search_value': 'Asymmetry'
            },

            {
                'set_values': {'x': 'event',
                               'y': 'UKNOWN',
                               'type': 'histogram',
                               'function': 'average',
                               'dimension': 2,
                               'system': 'adc',
                               'sub_system': None},
                'search_value': 'AvADCAllMillislice',
            },

            {
                'set_values': {'x': 'event',
                               'y': 'channel',
                               'type': 'histogram',
                               'function': 'average',
                               'dimension': 2,
                               'system': 'adc',
                               'sub_system': 'rce'},
                'search_value': 'AvADCChannelEvent'
            },

            {
                'set_values': {'x': 'channel',
                               'y': 'UKNOWN',
                               'type': 'histogram',
                               'function': 'average',
                               'dimension': 2,
                               'system': 'adc',
                               'sub_system': None},
                'search_value': 'AvADCMillisliceChannel'
            },

            {
                'set_values': {'x': 'event',
                               'y': 'channel',
                               'type': 'histogram',
                               'function': 'average',
                               'dimension': 2,
                               'system': 'adc',
                               'sub_system': 'ssp'},
                'search_value': 'AvWaveformChannelEvent',
            },
            {
                'set_values': {'x': 'channel',
                               'y': 'bit',
                               'type': 'histogram',
                               'function': None,
                               'dimension': 2,
                               'system': 'adc',
                               'sub_system': None},
                'search_value': 'BitCheckAnd'
            },
        ],
    }

    with io.open('config.json', 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(d, indent=4, ensure_ascii=False)))


write_json_subruns()
