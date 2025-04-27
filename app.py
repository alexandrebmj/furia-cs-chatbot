from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message'].lower()

    if user_message == '/start':
        response = '🔥 Bem-vindo ao chat da FURIA! 🔥\n\nComandos disponíveis:\n- /proximo\n- /ultimos\n- /jogadores\n- /frase\n- /social\n- /curiosidade'
    elif user_message == '/proximo':
        response = '🎯 Próximo jogo: FURIA vs NAVI - 28/04 às 18h (Horário de Brasília)'
    elif user_message == '/ultimos':
        response = '🏆 Últimos jogos:\n- Vitória vs Team Liquid (2-0)\n- Derrota vs FaZe (1-2)\n- Vitória vs G2 (2-1)'
    elif user_message == '/jogadores':
        response = '👥 Elenco CS2 da FURIA:\n- KSCERATO\n- yuurih\n- chelo\n- FalleN\n- arT'
    elif user_message == '/frase':
        response = '💬 "Jogar contra a FURIA é como tentar apagar fogo com gasolina!"'
    elif user_message == '/social':
        response = '📱 Redes sociais oficiais:\n- Instagram: @furia\n- Twitter: @FURIA\n- TikTok: @furia'
    elif user_message == '/curiosidade':
        response = '🔍 Curiosidade: A FURIA foi o primeiro time brasileiro a ter uma gaming house nos EUA!'
    else:
        response = '🤔 Comando não reconhecido.\n\nTente usar:\n- /proximo\n- /ultimos\n- /jogadores\n- /frase\n- /social\n- /curiosidade'

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
