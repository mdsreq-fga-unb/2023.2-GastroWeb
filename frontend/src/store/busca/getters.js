// import {isProxy, toRaw} from 'vue'

export function parametrosBusca(state) {
  return state.parametrosBusca
}

export function reutilizarBusca(state) {
  return JSON.stringify(state.resultadoParametros) === JSON.stringify(state.parametrosBusca)
}
