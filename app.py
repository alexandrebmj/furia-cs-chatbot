from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Rota para renderizar a página principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar mensagens do chat
@app.route('/chat', methods=['POST'])
def chat():
    dados = request.get_json()
    mensagem = dados.get('message', '')

    if not mensagem:
        return jsonify({'response': '👋 Olá! Digite <b>INICIAR</b> para ver os comandos disponíveis.'})
    
    resposta = responder_ao_usuario(mensagem)
    return jsonify({'response': resposta})


# Função para interpretar a mensagem do usuário e responder de forma flexível
def responder_ao_usuario(mensagem):
    mensagem = mensagem.lower()

    if 'iniciar' in mensagem or 'comando' in mensagem:
        return '''
        <b>📋 Comandos disponíveis:</b><br>
        ➤ <b>agenda</b> → Ver o próximo jogo da FURIA<br>
        ➤ <b>resultados</b> → Resultados dos últimos jogos<br>
        ➤ <b>jogadores</b> → Ver elenco atualizado<br>
        ➤ <b>uniforme</b> → Link do novo uniforme da FURIA<br>
        ➤ <b>social</b> → Redes sociais oficiais<br>
        ➤ <b>curiosidade</b> → Curiosidades sobre a FURIA
        '''

    elif 'proximo' in mensagem or 'próximo' in mensagem or 'agenda' in mensagem:
        return 'A FURIA não tem confrontos marcados'

    elif 'ultimos' in mensagem or 'últimos resultados' in mensagem or 'resultados' in mensagem:
        return '''<b>📊 Últimos Resultados:</b><br>
        ❌ contra TheMongolZ<br>
        ❌ contra Virtus.pro<br>
        ❌ contra Complexity<br>
        ✅ contra Betclic'''

    elif 'roster' in mensagem or 'elenco' in mensagem or 'jogadores' in mensagem:
        return '''<b>🎮 Elenco Atual FURIA CS2:</b><br>
        <div class="containes">
            <div class="item"> 
                <img src="https://img-cdn.hltv.org/playerbodyshot/U6t0j2bJDKUR3mTI8rIqv7.png?ixlib=java-2.1.0&w=400&s=b5257c378b8122f415f21985855e95ca" alt="Logo FURIA" class="players"> 
                <p>Kscerato</p>
            </div>
            <div class="item">       
                <img src="https://img-cdn.hltv.org/playerbodyshot/i6UGhkYxrhutAOmWZT0-8O.png?ixlib=java-2.1.0&w=400&s=2cd696f6ff4baf5680a43d537214b6eb" alt="Logo FURIA" class="players"> 
                <p>Yuurih</p>
            </div>
        </div> 
        <div class="container">    
            <div class="item">
                <img src="https://pbs.twimg.com/media/GoRqLHpWkAAcp8R?format=jpg&name=large" alt="Logo FURIA" class="players">
                <p>Molodoy</p> <br>
            </div>  
            <div class="item">       
                <img src="https://img-cdn.hltv.org/playerbodyshot/Wf26SO_o8nvnsLh0AqZXc5.png?ixlib=java-2.1.0&w=400&s=36b7189a4ae7b020d0acb087fd44777a" alt="Logo FURIA" class="players"> 
                <p>Fallen</p>
            </div> 
            <div class="item">      
                <img src="https://pbs.twimg.com/media/GpJqytlXMAA6eqZ?format=jpg&name=large" alt="Logo FURIA" class="players">
                <p>Yekindar</p>
                </div>
        </div>
         '''
        

    elif 'camisa' in mensagem or 'manto' in mensagem or 'uniforme' in mensagem:
        return '''
<p>Já deu uma olhada no nosso novo uniforme?:</p>
<ul style="list-style-type: none; padding: 0;">
    <li><a href="https://www.furia.gg/produto/camiseta-furia-adidas-preta-150263" target="_blank" class="link-chat">👕 Manto</a></li>
</ul>
'''

    elif 'social' in mensagem or 'instagram' in mensagem or 'twitter' in mensagem or 'rede' in mensagem:
        return '''
<p>Nos siga nas redes sociais:</p>
<ul style="list-style-type: none; padding: 0;">
    <li><a href="https://x.com/FURIA" target="_blank" class="link-chat">🐦 Twitter</a></li>
    <li><a href="https://www.instagram.com/furiagg/" target="_blank" class="link-chat">📸 Instagram</a></li>
</ul>
'''

    elif 'curiosidade' in mensagem:
        return '''Salve xd '''

    else:
        return '🤖 <i>Desculpe, não entendi.</i><br>Digite <b>INICIAR</b> para ver os comandos disponíveis.'

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
