import { api } from 'src/boot/axios'
const urlBackend = ''

export const createRecipe = async (body) => {
  return api.post('/criar_receitas', body)
}

export const editRecipe = async (id, body) => {
  return api.put(`/update_receita_por_id/${id}`, body)
}

export const deleteRecipe = async (id) => {
  return api.delete(`/delete_receita_por_id/${id}`)
}
export const listAllRecipe = async () =>
  api.get('/get_all_receitas')

export const searchByName = async ( params ) => {
  return api.get('/busca_por_titulo', { params })
}

export const searchByTagCategory = async ( {tag, categoria} ) => {
  const params = {
    tag,
    categoria
  }
  return api.get('/busca_categoria_e_tag', { params })
}

export const searchById = async ( params ) => {
  return api.get('/get_receita_por_id', { params })
}