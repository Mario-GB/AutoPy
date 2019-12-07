import logging as lg
import logging.config
import traceback


def __get_logger():
    log_format = '%(levelname)s \t|%(asctime)s| ' + str(traceback.extract_stack(limit=3)[0]) + '\n\t%(message)s'
    lg.basicConfig(  # TODO cambiar por lectura de fichero
        format=log_format)

    logger = lg.getLogger()
    logger.setLevel(lg.INFO) # TODO borrar cuando se haya hecho por fichero


def info(message):
    __get_logger().info(message)


def error(message):
    __get_logger().error(message)


def debug(message):
    __get_logger().debug(message)
