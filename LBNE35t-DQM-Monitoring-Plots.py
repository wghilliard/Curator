import json
import io

PATH = "/Users/wghilliard/D_TEST/config.JSON"


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
            },
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'ADCMeanChannel',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Mean',
                            'y': 'ADC Count',
                            'x': 'Channel',
                            'sample': 'All Events',
                            'caption': 'Mean ADC values for each channel read out by the RCEs (profiled over all events read).'
                            }
            },
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'ADCRMSChannel',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'RMS',
                            'y': 'ADC Count',
                            'x': 'Channel',
                            'sample': 'All Events',
                            'caption': 'RMS of the ADC values for each channel read out by the RCEs (profiled over all events read)'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'AvADCAllMillislice',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Average Over Millislice',
                            'y': 'ADC Count',
                            'x': 'Event',
                            'sample': 'First 10000 Events',
                            'caption': 'Average RCE ADC across an entire millislice for the first 10000 events (one entry per millislice in each event)'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'RCEDNoiseChannel',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Noise',
                            'y': 'ADC Count',
                            'x': 'Channel',
                            'sample': 'All Events',
                            'caption': 'DNoise (difference in ADC between neighbouring channels for the same tick) for the RCE ADCs (profiled over all event read)'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'AvADCChannelEvent',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Average',
                            'y': 'ADC Count',
                            'x': 'Channel',
                            'sample': 'First 100 Events',
                            'caption': 'Average RCE ADC across a channel for an event, shown for the first 100 events'}},

            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'TotalRCEHitsChannel',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Total',
                            'y': 'Count',
                            'x': 'Channel',
                            'sample': 'All Events',
                            'caption': 'Total number of RCE hits in each channel across all events.'}},

            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'TotalADCEvent',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Total',
                            'x': 'Total ADC',
                            'y': 'Events',
                            'sample': 'All Events',
                            'caption': 'Total RCE ADC recorded for an event across all channels (one entry per event)'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'TotalRCEHitsEvent',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Total',
                            'x': 'Total Hits',
                            'y': 'Events',
                            'sample': 'All Events',
                            'caption': 'Total number of hits recorded on the RCEs per event (one entry per event)'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'Asymmetry',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Asymmetry',
                            'y': 'Asymmetry',
                            'x': 'Channel',
                            'sample': 'All Events',
                            'caption': 'Asymmetry of the bipolar pulse measured on the induction planes, by channel (profiled across all events). Zero means completely symmetric pulse.'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'TimesADCGoesOverThreshold',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Count',
                            'y': 'Count',
                            'x': 'Times ADC Goes Over Threshold',
                            'sample': 'All Events',
                            'caption': 'Number of times an RCE hit goes over a set ADC threshold'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'BitCheckAnd',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Boolean Test',
                            'y': 'Bit',
                            'x': 'Channel',
                            'z': 'Events',
                            'sample': 'All Events',
                            'caption': 'Check for stuck RCE bits: bits which are always on'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'BitCheckOr',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Boolean Test',
                            'y': 'Bit',
                            'x': 'Channel',
                            'sample': 'All Events',
                            'caption': 'Check for stuck RCE bits: bits which are always off'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'NumMicroslicesInMillislice',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Count',
                            'y': 'Microslice',
                            'x': 'Millislice',
                            'sample': 'All Events',
                            'caption': 'Number of microslices in a millislice in this run'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'AvWaveformChannelEvent',
                'setTags': {'system': 'Photon',
                            'subsystem': 'SSP',
                            'type': 'Average',
                            'y': 'Channel',
                            'x': 'Event',
                            'sample': 'First 100 Events',
                            'caption': 'Average SSP ADC across a channel for an event, shown for the first 100 events'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'WaveformMeanChannel',
                'setTags': {'system': 'Photon',
                            'subsystem': 'SSP',
                            'type': 'Mean',
                            'y': 'ADC Counts',
                            'x': 'Channel',
                            'sample': 'All Events',
                            'caption': 'Mean ADC values for each channel read out by the SSPs (profiled over all events read)'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'WaveformRMSChannel',
                'setTags': {'system': 'Photon',
                            'subsystem': 'SSP',
                            'type': 'RMS',
                            'y': 'ADC Counts',
                            'x': 'Channel',
                            'sample': 'All Events',
                            'caption': 'RMS of the ADC values for each channel read out by the SSPs (profiled over all events read)'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'SSPDNoiseChannel',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Difference',
                            'y': 'DNoise',
                            'x': 'Channel',
                            'sample': 'All Events',
                            'caption': 'DNoise (difference in ADC between neighbouring channels for the same tick) for the RCE ADCs (profiled over all events read) [Note: Filename says SSP, but description is for TPC/RCE/ADC.]'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'TotalSSPHitsChannel',
                'setTags': {'system': 'Photon',
                            'subsystem': 'SSP',
                            'type': 'Count',
                            'y': 'Hits',
                            'x': 'Channel',
                            'sample': 'All Events',
                            'caption': 'Total number of SSP hits in each channel across all events'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'TotalWaveformEvent',
                'setTags': {'system': 'Photon',
                            'subsystem': 'SSP',
                            'type': 'Total',
                            'y': 'Events',
                            'x': 'Total ADC',
                            'sample': 'All Events',
                            'caption': 'Total SSP ADC recorded for an event across all channels (one entry per event)'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'TotalSSPHitsEvent',
                'setTags': {'system': 'Photon',
                            'subsystem': 'SSP',
                            'type': 'Total',
                            'y': 'Events',
                            'x': 'Hits',
                            'sample': 'All Events',
                            'caption': 'Total number of hits recorded on the SSPs per event (one entry per event)'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'SSPBitCheckAnd',
                'setTags': {'system': 'TPC',
                            'subsystem': 'SSP',
                            'type': 'Boolean Check',
                            'y': 'Bit',
                            'x': 'Channel',
                            'sample': 'All Events',
                            'caption': 'Check for stuck SSP bits: bits which are always on'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'SSPBitCheckOr',
                'setTags': {'system': 'TPC',
                            'subsystem': 'SSP',
                            'type': 'Boolean Check',
                            'y': 'Bit',
                            'x': 'Channel',
                            'sample': 'All Events',
                            'caption': 'Check for stuck SSP bits: bits which are always off'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'TimesWaveformGoesOverThreshold',
                'setTags': {'system': 'Photon',
                            'subsystem': 'SSP',
                            'type': 'Count',
                            'y': 'Events',
                            'x': 'Count',
                            'sample': 'All Events',
                            'caption': 'Number of times an SSP hit goes over a set ADC threshold'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'SizeOfFiles',
                'setTags': {'system': 'Full Detector',
                            'subsystem': 'DAQ',
                            'type': 'Size',
                            'y': 'Bytes',
                            'x': 'Run',
                            'sample': 'Last 20 Runs',
                            'caption': 'Size of the data files made by the DAQ for the last 20 runs'}},
            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'SizeOfFilesPerEvent',
                'setTags': {'system': 'Full Detector',
                            'subsystem': 'DAQ',
                            'type': 'Size',
                            'y': 'Bytes/Event',
                            'x': 'Data File',
                            'sample': 'Last 20 Data Files',
                            'caption': 'Size of event in each of the last 20 data files made by the DAQ (size of file / number of events in file)'}},

            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'NumSubDetectorsPresent',
                'setTags': {'system': 'Full Detector',
                            'subsystem': 'DAQ',
                            'type': 'Count',
                            'y': 'Detectors/Event',
                            'x': 'Data File',
                            'sample': 'Last 20 Data Files',
                            'caption': 'Number of subdetectors present in each event in the data (one entry per event)'}},

            {
                'name': 'FOO',
                'startIndex': None,
                'searchString': 'AvADCMillisliceChannel',
                'setTags': {'system': 'TPC',
                            'subsystem': 'RCE/ADC',
                            'type': 'Average',
                            'y': 'ADC Count',
                            'x': 'Channel',
                            'sample': 'UNKNOWN',
                            'caption': 'Average ADC count across the channels read out by each millislice present in the data.'}
            }],

        'possible': {'type': [{'value': 'avc', 'pretty': 'ADC vs Channel'},
                              {'value': 'tvc', 'pretty': 'Time vs Channel'},
                              {'value': 'u_plane', 'pretty': 'U Plane View'},
                              {'value': 'v_plane', 'pretty': 'V Plane View'},
                              {'value': 'z_plane', 'pretty': 'Z Plane View'},
                              {'value': 'Average', 'pretty': 'Average'},
                              {'value': 'Count', 'pretty': 'Count'},
                              {'value': 'Mean', 'pretty': 'Mean'}
                              ],

                     'view': [{'value': 'u', 'pretty': 'U'},
                              {'value': 'v', 'pretty': 'V'},
                              {'value': 'z0', 'pretty': 'Z0'},
                              {'value': 'z1', 'pretty': 'Z1'}],
                     'x': [{'value': 'channel', 'pretty': 'Channel'},
                           {'value': 'event', 'pretty': 'Event'},
                           {'value': 'millislice', 'pretty': 'Millislice'},
                           {'value': 'subdetector', 'pretty': 'Subdetector'},
                           {'value': 'ADC Count', 'pretty': 'ADC Count'}],

                     'y': [{'value': 'adc_value', 'pretty': 'ADC Value'},
                           {'value': 'event', 'pretty': 'Event'},
                           {'value': 'millislice', 'pretty': 'Millislice'},
                           {'value': 'subdetector', 'pretty': 'Subdetector'},
                           {'value': 'ADC Count', 'pretty': 'ADC Count'},
                           {'value': 'Detectors/Event', 'pretty': 'Detectors/Event'}],

                     'system': [{'value': 'Photon', 'pretty': 'Photon'},
                                {'value': 'TPC', 'pretty': 'TPC'},
                                {'value': 'Full Detector', 'pretty': 'Full Detector'}],

                     'subsystem': [{'value': 'RCE/ADC', 'pretty': 'RCE/ADC'},
                                   {'value': 'DAQ', 'pretty': 'DAQ'},
                                   {'value': 'SSP', 'pretty': 'SSP'}
                                   ],
                     'sample': [{'value': 'UNKNOWN', 'pretty': 'UNKNOWN'},
                                {'value': 'Last 20 Data Files', 'pretty': 'Last 20 Data Files'},
                                {'value': 'Last 20 Runs', 'pretty': 'Last 20 Runs'},
                                {'value': 'All Events', 'pretty': 'All Events'}
                                ]

                     }


    }

    with io.open(PATH, 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(d, indent=4, ensure_ascii=False)))

write_json_events()
