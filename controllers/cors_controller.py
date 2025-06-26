from odoo import http
from odoo.http import request

class MobileCORSController(http.Controller):
    @http.route('/mobile/session/authenticate', type='json', auth='none', csrf=False, cors='*')
    def mobile_session_authenticate(self, db, login, password):
        """Authenticate a user with CORS enabled."""
        return request.session.authenticate(db, login, password)

    @http.route('/mobile/dataset/call_kw', type='json', auth='user', csrf=False, cors='*')
    def mobile_call_kw(self, model, method, args, kwargs=None):
        """Proxy dataset calls with CORS headers."""
        kwargs = kwargs or {}
        return request.env[model].call_kw(method, args, kwargs)
