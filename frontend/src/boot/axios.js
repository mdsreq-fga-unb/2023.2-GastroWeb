import axios from 'axios'
import { boot } from 'quasar/wrappers'

export const baseURL = 'http://localhost:5000'

var api = axios.create({ baseURL })

export default boot(({ app, router, store }) => {
    
})

export { api }
