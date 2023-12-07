
import busca from './busca'

import { createStore } from 'vuex'

export default function (/* { ssrContext } */) {
  const Store = createStore({
    modules: {
      busca
    },

    // enable strict mode (adds overhead!)
    // for dev mode and --debug builds only
    strict: process.env.DEBUGGING
  })

  return Store
}
