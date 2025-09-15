# import - incorpora uma biblioteca (código já escrito para resolveer um problema específico)

import numpy as np

class Perceptron:
  # Declarando construtor da classe
    def __init__(self):
        self.w1 = np.random.uniform(-1, 1)
        self.w2 = np.random.uniform(-1, 1)
        self.bias = np.random.uniform(-1, 1)

  # Novo método para a função de ativação
    def step_function(self, x):
        return 1 if x > 0 else 0

    def train(self, inputs, outputs, learning_rate=0.5, epochs=100):
        for i in range(epochs):
            for j in range(len(inputs)):
                soma_ponderada = (self.w1 * inputs[j][0]) + (self.w2 * inputs[j][1]) + self.bias
                # usando o step_function
                prediction = self.step_function(soma_ponderada)

                erro = outputs[j][0] - prediction

                self.w1 += self.w1 + learning_rate * erro * inputs[j][0]
                self.w2 += self.w2 + learning_rate * erro * inputs[j][1]
                self.bias += learning_rate * erro

    def predict(self, weights, x1, x2):
        soma_ponderada = (self.w1 * x1) + (self.w2 * x2) + self.bias
        return self.step_function(soma_ponderada)

if __name__ == '__main__':
    # Entradas das portas lógicas (em pares)
    inputs = [[0,0], [0,1], [1,0], [1,1]]
    # Saídas da porta AND são [[0], [0], [0], [1]]
    outputs = [[0], [1], [1], [1]]

    print(' ')
    for i in range(len(inputs)):
        print(inputs[i][0], inputs[i][1], '->', outputs[i][0])


    print(' ')

    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            print(inputs[i][j], end=', ')
        print(' ')

    perceptron = Perceptron()

    # Treinando o perceptron
    tanning = perceptron.train(inputs = inputs, outputs = outputs, learning_rate=0.1, epochs=100)

    prediction = perceptron.predict(tanning, 1, 1)

    print('OUTPUT ', prediction)
