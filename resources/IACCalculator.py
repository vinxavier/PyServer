from flask import jsonify, request
from flask_restful import Resource

class IACCalculator(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        circ_quadril = json_data['circ_quadril']
        altura = json_data['altura']
        sexo = json_data['sexo']
        if self.__is_valid(circ_quadril, altura, sexo):
            iac = self.__calc_iac(circ_quadril, altura)
            condicao = self.__condition(iac, sexo)
            return jsonify(iac = iac, condicao = condicao)
        else:
            error = "Paramêtros inválidos"
            return jsonify(error = error)

    def __calc_iac(self, circ, altura):
        iac_divisor = altura ** (1.5) 
        return ( circ / iac_divisor ) - 18

    def __condition(self, iac, sexo):
        if sexo == "m":
            if iac < 8:
                return "Abaixo do normal"
            elif 8 <= iac < 21:
                return "Normal"
            elif 21 <= iac < 25:
                return "Sobrepeso"
            else:
                return "Obesidade"
        elif sexo == "f":
            if iac < 21:
                return "Abaixo do normal"
            elif 21 <= iac < 33:
                return "Normal"
            elif 33 <= iac < 38:
                return "Sobrepeso"
            else:
                return "Obesidade"
        else:
            return "ERROR"
    
    def __is_valid(self, circ, altura, sexo):
        return circ > 0 and altura > 0 and (sexo == "m" or sexo == "f")
