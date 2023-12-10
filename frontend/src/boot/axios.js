import axios from 'axios'
import { boot } from 'quasar/wrappers'

export const baseURL = 'http://localhost:5000'

var api = axios.create({ baseURL })

export default boot(({ app, router, store }) => {
  api.interceptors.request.use(
    config => {
      const token = localStorage.getItem('token')
        
      // const token = response.data.token
      if (token) {
        config.headers.Authorization = `Bearer ${token}`
      }

      return config
    },
    error => Promise.reject(error)
  )
  app.config.globalProperties.$api = api
    
})

export { api }
