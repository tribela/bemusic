import re


class Bms(object):

    pattern_header = re.compile(
        r'#(?P<field>\S+)(?:\s(?P<value>.*))?',
    )

    pattern_data = re.compile(
        r'#(?P<bar>\d{3})'
        '(?P<channel>[0-9a-f]{2}):'
        '(?P<data>.*)$',
        re.IGNORECASE)

    def __init__(self):
        self.bmp = {}
        self.wav = {}
        self.stop = {}
        self.bpm = {}
        self.bars = {}

    @classmethod
    def parse(cls, fp):
        instance = Bms()
        for line in fp.readlines():
            line = line.strip()

            header_matched = cls.pattern_header.match(line)
            data_matched = cls.pattern_data.match(line)
            if data_matched:
                cls.parse_header(instance, data_matched)
            elif header_matched:
                cls.parse_header(instance, header_matched)
        return instance

    @staticmethod
    def parse_header(instance, matched):
        field = matched.group('field')
        value = matched.group('value')

        if field == 'PLAYER':
            instance.player = value
        elif field == 'TITLE':
            instance.title = value
        elif field == 'ARTIST':
            instance.artist = value
        elif field == 'GENRE':
            instance.genre = value
        elif field == 'BPM':
            instance.bpm = float(value)
        elif field == 'PLAYLEVEL':
            instance.playlevel = int(value)
        elif field == 'RANK':
            instance.rank = int(value)
        elif field == 'TOTAL':
            instance.total = int(value)
        elif field == 'VOLWAV':
            instance.volwav = int(value)
        elif field == 'MIDIFILE':
            instance.midifile = value
        elif field == 'STAGEFILE':
            instance.stagefile = value
        elif field == 'VIDEOFILE':
            instance.videofile = value
        elif field == 'LNTYPE':
            # XXX
            instance.lntype[int(value)] = True
        elif field == 'LNOBJ':
            # TODO: implement this.
            pass
        elif field == 'EXTCHR':
            # TODO: implement this.
            pass
        elif field.startswith('WAV'):
            # TODO: implement this.
            pass
        elif field.startswith('BMP'):
            # TODO: implement this.
            pass
        elif field.startswith('STOP'):
            # TODO: implement this.
            pass
        elif field.startswith('BPM'):
            # TODO: implement this.
            pass

    @staticmethod
    def parse_data(instance, matched):
        # TODO: implement this.
        pass
