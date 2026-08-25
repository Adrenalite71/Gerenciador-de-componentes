import sqlite3
import threading
import traceback
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/retirar_estoque', methods=['POST'])
def retirar_estoque():
    try:
        data = request.get_json()
        texto_digitado = data.get('texto_digitado')
        quantidade_solicitada = int(data.get('quantidade_solicitada'))
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, gaveta, divisao, quantidade FROM componentes WHERE nome LIKE ? LIMIT 1", ('%' + texto_digitado + '%',))
        row = cursor.fetchone()
        if row:
            comp_id, gaveta, divisao, quantidade = row
            if quantidade >= quantidade_solicitada:
                nova_quantidade = quantidade - quantidade_solicitada
                cursor.execute("UPDATE componentes SET quantidade = ? WHERE rowid = ?", (nova_quantidade, comp_id))
                conn.commit()
                conn.close()
                return jsonify({"status": "sucesso", "mensagem": "Estoque atualizado", "localizacao": {"gaveta": gaveta, "divisao": divisao}, "estoque_restante": nova_quantidade}), 200
            else:
                conn.close()
                return jsonify({"status": "erro", "mensagem": "Estoque insuficiente", "quantidade_disponivel": quantidade}), 400
        else:
            conn.close()
            return jsonify({"status": "erro", "mensagem": "Componente nao encontrado"}), 404
    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

def start_api():
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

def run_server_in_thread():
    t = threading.Thread(target=start_api, daemon=True)
    t.start()
