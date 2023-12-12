import axios from 'axios'
import { boot } from 'quasar/wrappers'

export const baseURL = 'https://gastroweb.onrender.com/'

var api = axios.create({ baseURL })

export default boot(({ app, router, store }) => {
    
})

export { api }
