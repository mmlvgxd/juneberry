from juneberry import Theme
from juneberry import Color
from juneberry import Logger


theme = Theme(
    Color.Custom.from_rgb((189, 224, 254)),
    Color.Custom.from_rgb((205, 180, 219)),
    Color.Custom.from_rgb((162, 210, 255)),
    Color.Custom.from_rgb((255, 200, 221)),
    Color.Custom.from_rgb((255, 175, 204)),
    Color.Custom.from_rgb((255, 254, 214)),
    Color.Custom.from_rgb((255, 254, 214))
)

logger = Logger(theme=theme)


logger.info('Everything is OK')
logger.warn('Warning')
logger.debug('KrutoiSkeletik24')
logger.error('Something went wrong')
logger.fatal('Critical error')