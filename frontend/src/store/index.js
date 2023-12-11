
import busca from './busca'
import login from './login'

import { createStore } from 'vuex'

export default function (/* { ssrContext } */) {
  const Store = createStore({
    modules: {
      busca,
      login
    },

    // enable strict mode (adds overhead!)
    // for dev mode and --debug builds only
    strict: process.env.DEBUGGING
  })

  return Store
}
