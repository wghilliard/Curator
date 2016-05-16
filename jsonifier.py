import json
import io

from config import CONFIG_PATH


def write_json_events():
    d = {
        'sort_keys': [
            {
                'name': 'u_plane',
                'setTags': {'type': 'u_plane'},
                'searchString': 'UPlaneView',
                'startIndex': None,
            },
            {
                'name': 'v_plane',
                'searchString': 'VPlaneView',
                'setTags': {'type': 'v_plane'},
                'startIndex': None,
            },
            {
                'name': 'z_plane',
                'searchString': 'ZPlaneView',
                'setTags': {'type': 'z_plane'},
                'startIndex': None,
            },
            {
                'name': 'avc',
                'searchString': 'ADCvsChan',
                'setTags': {'type': 'avc'},
                'startIndex': None
            },
            {
                'name': 'tvc',
                'searchString': 'TimevsChan',
                'setTags': {'type': 'tvc'},
                'startIndex': None
            },
            {
                'name': 'view',
                'searchString': r'^[UVZ]{1}[01]?$',
                'setTags': None,
                'startIndex': 0
            },
            {
                'name': 'event_number',
                'searchString': r'^E[0-9]{0,9}$',
                'setTags': None,
                'startIndex': 1
            }
            # ,
        #     HERE GOES NUTHIN
        #     {
        #         'set_values': {'x': 'channel',
        #                        'y': 'UNKNOWN',
        #                        'type': 'histogram',
        #                        'function': 'mean',
        #                        'dimension': 2,
        #                        'system': 'adc',
        #                        'sub_system': 'rce'},
        #         'search_value': 'ADCMeanChannel',
        #     },
        #
        #     {
        #         'set_values': {'x': 'channel',
        #                        'y': 'UNKNOWN',
        #                        'type': 'histogram',
        #                        'function': 'rms',
        #                        'dimension': 2,
        #                        'system': 'adc',
        #                        'sub_system': 'rce'},
        #         'search_value': 'ADCRMSChannel'
        #     },
        #
        #     {
        #         'set_values': {'x': 'channel',
        #                        'y': 'UKNOWN',
        #                        'function': 'UKNOWN',
        #                        'type': 'histogram',
        #                        'dimension': 2,
        #                        'system': 'UKNOWN',
        #                        'sub_system': None},
        #         'search_value': 'Asymmetry'
        #     },
        #
        #     {
        #         'set_values': {'x': 'event',
        #                        'y': 'UKNOWN',
        #                        'type': 'histogram',
        #                        'function': 'average',
        #                        'dimension': 2,
        #                        'system': 'adc',
        #                        'sub_system': None},
        #         'search_value': 'AvADCAllMillislice',
        #     },
        #
        #     {
        #         'set_values': {'x': 'event',
        #                        'y': 'channel',
        #                        'type': 'histogram',
        #                        'function': 'average',
        #                        'dimension': 2,
        #                        'system': 'adc',
        #                        'sub_system': 'rce'},
        #         'search_value': 'AvADCChannelEvent'
        #     },
        #
        #     {
        #         'set_values': {'x': 'channel',
        #                        'y': 'UKNOWN',
        #                        'type': 'histogram',
        #                        'function': 'average',
        #                        'dimension': 2,
        #                        'system': 'adc',
        #                        'sub_system': None},
        #         'search_value': 'AvADCMillisliceChannel'
        #     },
        #
        #     {
        #         'set_values': {'x': 'event',
        #                        'y': 'channel',
        #                        'type': 'histogram',
        #                        'function': 'average',
        #                        'dimension': 2,
        #                        'system': 'adc',
        #                        'sub_system': 'ssp'},
        #         'search_value': 'AvWaveformChannelEvent',
        #     },
        #     {
        #         'set_values': {'x': 'channel',
        #                        'y': 'bit',
        #                        'type': 'histogram',
        #                        'function': None,
        #                        'dimension': 2,
        #                        'system': 'adc',
        #                        'sub_system': None},
        #         'search_value': 'BitCheckAnd'
        #     }
        ],
        # MORE CONFIG STUFF
        'paths': {'main_path': '/Users/wghilliard/C_TEST',
                  'sub_run': '<main_path>/<run_name>/<sub_run_name>',
                  'event_histograms': '<main_path>/<run_name>/event_histograms'},

        'possible': {'type': [{'value': 'avc', 'pretty': 'ADC vs Channel'},
                              {'value': 'tvc', 'pretty': 'Time vs Channel'},
                              {'value': 'u_plane', 'pretty': 'U Plane View'},
                              {'value': 'v_plane', 'pretty': 'V Plane View'},
                              {'value': 'z_plane', 'pretty': 'Z Plane View'}],
                     'view': [{'value': 'u', 'pretty': 'U'},
                              {'value': 'v', 'pretty': 'V'},
                              {'value': 'z0', 'pretty': 'Z0'},
                              {'value': 'z1', 'pretty': 'Z1'}],
                     'x': [{'value': 'channel', 'pretty': 'Channel'},
                           {'value': 'event', 'pretty': 'Event'},
                           {'value': 'millislice', 'pretty': 'Millislice'},
                           {'value': 'subdetector', 'pretty': 'Subdetector'}],
                     'y': [{'value': 'adc_value', 'pretty': 'ADC Value'},
                           {'value': 'event', 'pretty': 'Event'},
                           {'value': 'millislice', 'pretty': 'Millislice'},
                           {'value': 'subdetector', 'pretty': 'Subdetector'}],
                     'system': [{'value': 'adc', 'pretty': 'ADC'}]

                     }
    }

    with io.open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(d, indent=4, ensure_ascii=False)))


write_json_events()
