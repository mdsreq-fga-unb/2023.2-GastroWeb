import { api } from 'src/boot/axios'
const urlBackend = ''

export const createRecipe = 
  async ({ titulo, ingredientes, instrucoes, categorias, tags, files }) => {
    const body = {
      titulo,
      ingredientes,
      instrucoes,
      categorias,
      tags,
      files
    }
    return api.post('/criarReceitas', body)
  }


export const listAllRecipe = async () =>
  api.get('/getreceitas')


