from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/send-media', methods=['POST'])
def send_media():
    try:
        payload = request.json
        response = requests.post(
            'https://evolutionapi.jncompany.com.br/message/sendMedia/main',
            headers={'apikey': 'F90E81C294D1-4541-8579-61A7A6687E63'},
            json=payload
        )
        response.raise_for_status()
        evolution_response = response.json()
        filtered_response = {
            'status': evolution_response.get('status', 'success'),
            'mediaLink': payload.get('media'),
            'message': 'Chamada processada pelo proxy em Python'
        }
        return jsonify(filtered_response), 200
    except requests.exceptions.RequestException as e:
        print(f"Erro ao chamar a Evolution API: {str(e)}")
        return jsonify({'error': 'Erro ao processar a requisição'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
