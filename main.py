from flask import Flask
import graphviz

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hola mundo'

@app.route('grafo', methods=['GET'])
def grafo():
    dot = graphviz.Digraph(name="grafo", format='svg')
    dot.node('A', 'King Arthur')
    dot.node('B', 'Sir Bedevere the Wise')
    dot.node('L', 'Sir Lancelot the Brave')
    dot.edges(['AB', 'AL'])
    dot.edge('B', 'L', constraint='false')
    a = dot.pipe().decode('utf-8')
    return a

if __name__ == '__main__':
    app.run(debug=False, port=5000)
