const verificarReceita = require('../pages/verificarReceita');

test('Teste com retorno vazio', () => {
  let objeto = {
    titulo: 'Bolo de cenoura',
    ingredientes : ['farinha', 'açucar', 'cenoura', 'ovo'],
    instrucao: 'misture tudo, coloque fermento e  asse por 45 min'
  };
  expect(verificarReceita(objeto)).toBe("Receita verificada");
});

test('Teste com titulo não vazio', () => {
  let objeto = {
    titulo: '',
    ingredientes : ['farinha', 'açucar', 'cenoura', 'ovo'],
    instrucao: 'misture tudo, coloque fermento e  asse por 45 min'
  };
  expect(verificarReceita(objeto)).toBe("Receita sem título");
});

test('Teste com ingredientes não vazio', () => {
  let objeto = {
    titulo: 'Bolo de cenoura',
    ingredientes: [],
    instrucao: 'misture tudo, coloque fermento e  asse por 45 min'
  };
  expect(verificarReceita(objeto)).toBe("Receita sem ingredientes");
});

test('Teste com modo de preparo não vazio', () => {
  let objeto = {
    titulo: 'Bolo de cenoura',
    ingredientes : ['farinha', 'açucar', 'cenoura', 'ovo'],
    instrucao: ''
  };
  expect(verificarReceita(objeto)).toBe("Receita sem modo de preparo");
});