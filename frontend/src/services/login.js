import { api } from 'src/boot/axios'

export const login = async (body) => {
  return api.post('/token', body)
}