function verificarReceita(object){
    if(object?.titulo == null || object?.titulo == ''){
        return "Receita sem título"
    }
    else if(object?.ingredientes.length === 0){
        return "Receita sem ingredientes"
    }
    else if(object?.instrucao == null || object?.instrucao == ''){
        return "Receita sem modo de preparo"
    }
    return "Receita verificada";

}
module.exports = verificarReceita;