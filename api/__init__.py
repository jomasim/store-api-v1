from api.app import create_app
''' return app instance '''
def api_instance(setting):
    return create_app(setting)