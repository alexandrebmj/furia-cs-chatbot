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
        ➤ <b>Agenda</b> → Ver os próximos jogos da FURIA<br>
        ➤ <b>Resultados</b> → Resultados dos últimos jogos<br>
        ➤ <b>Jogadores</b> → Ver elenco atualizado<br>
        ➤ <b>Uniforme</b> → Link do novo uniforme da FURIA<br>
        ➤ <b>Redes</b> → Redes sociais oficiais da FURIA<br>
        ➤ <b>Curiosidade</b> → Curiosidades sobre a FURIA
        '''

    elif 'proximo' in mensagem or 'próximo' in mensagem or 'agenda' in mensagem:
        return '''Próximos campeonatos da FURIA:<br><br>
        🏆 PGL Astana 2025 <br>
        📅 10/05/25 à 18/05/25<br>
        <br>
        🏆 IEM Dallas 2025<br>
        📅 19/05/25 à 25/05/25<br>
        <br>
        🏆 BLAST.tv Austin Major 2025<br>
        📅 03/06/25 à 22/06/25
        '''

    elif 'ultimos' in mensagem or 'últimos resultados' in mensagem or 'resultados' in mensagem:
        return '''<b>📊 Últimos Resultados:</b><br>
        ❌ contra TheMongolZ<br>
        ❌ contra Virtus.pro<br>
        ❌ contra Complexity<br>
        ✅ contra Apogee'''

    elif 'roster' in mensagem or 'elenco' in mensagem or 'jogador' in mensagem:
        return '''<b>🎮 Elenco Atual FURIA CS2:</b><br>
        <div class="container">
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
        Este é o novo manto da FURIA! 🖤💛 
<br>  
<img src="https://furiagg.fbitsstatic.net/img/p/camiseta-furia-adidas-preta-150263/337479-1.jpg?w=1280&h=1280&v=202503281012" alt="Uniforme FURIA" style="width: 100%; border-radius: 10px; margin-top: 10px;">  
<br>  
<a class="link-chat" href="https://www.furia.gg/produto/camiseta-furia-adidas-preta-150263" target="_blank">👉 Comprar agora na loja oficial</a>
        '''

    elif 'social' in mensagem or 'instagram' in mensagem or 'twitter' in mensagem or 'rede' in mensagem:
        return '''Nos siga nas redes sociais:
            <ul style="list-style-type: none; padding: 0;">
            <li><a href="https://x.com/FURIA" target="_blank" class="link-chat">✖️ Twitter</a></li>
            <li><a href="https://www.instagram.com/furiagg/" target="_blank" class="link-chat">📸 Instagram</a></li>
            </ul>
            '''

    elif 'curiosidade' in mensagem:
        return '''Um dos maiores marcos da organização foi a conquista de sua primeira participação no Major de CS:GO, 
        o StarLadder Major Berlin 2019, onde a FURIA fez história ao chegar às semifinais, tornando-se uma das equipes mais respeitadas internacionalmente. '''

    else:
        return '🤖 <i>Desculpe, não entendi.</i><br>Digite <b>INICIAR</b> para ver os comandos disponíveis.'

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
