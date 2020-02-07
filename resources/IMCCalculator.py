from flask import jsonify, request
from flask_restful import Resource

class IMCCalculator(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        peso = json_data['peso']
        altura = json_data['altura']
        if self.__is_valid(peso, altura):
            imc = self.__calc_imc(peso, altura)
            condicao = self.__condition(imc)
            return jsonify(imc = imc, condicao = condicao)
        else:
            error = "Paramêtros inválidos"
            return jsonify(error = error)

    def __calc_imc(self, peso, altura):
        imc_divisor = altura ** (2) 
        return round(peso / imc_divisor, 2)

    def __condition(self, imc):
        if imc < 18.5:
            return "Abaixo do peso ideal"
        elif 18.5 <= imc < 25:
            return "Peso normal"
        elif 25 <= imc < 30:
            return "Excesso de peso"
        elif 30 <= imc < 35:
            return "Obesidade (grau I)"
        elif 35 <= imc < 40:
            return "Obesidade (grau II)"
        else:
            return "Obesidade (grau III)"
    
    def __is_valid(self, peso, altura):
        return peso > 0 and altura > 0
