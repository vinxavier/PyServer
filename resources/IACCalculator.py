from flask import jsonify, request
from flask_restful import Resource

class IACCalculator(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        sexo = json_data['sexo']
        circ_quadril = json_data['circ_quadril']
        altura = json_data['altura']
        iac_divisor = altura * ( altura ** (1/2) )
        iac = ( circ_quadril / iac_divisor ) - 18
        return jsonify(iac = iac)