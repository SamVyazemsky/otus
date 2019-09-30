class ScreamingWordProcessor(object):
    PLUGINS = []

    def process(self, text):
        for plugin in self.PLUGINS:
            text = plugin().cleanup(text)
        return text

    @staticmethod
    def scream(msg):
        print msg + '!'

    @classmethod
    def plugin(cls, plugin):
        cls.PLUGINS.append(plugin)


@ScreamingWordProcessor.plugin
class CleanMdashesExtension(object):
    def cleanup(self, text):
        return text.replace('&mdash;', u'\N{em dash}')


ScreamingWordProcessor.scream("Damn")