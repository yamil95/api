import logging


def finish(log, result, statusCode):
    logging.info(log)
    return {'result': result}, statusCode
