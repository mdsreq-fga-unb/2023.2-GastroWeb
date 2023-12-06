<template lang="pug">
q-page
  section.q-pa-xl.row.column
    q-btn(@click="mudarPagina" color="white" text-color="black").btn Criar Receita
    span Lista de receitas embaixo
    div(v-for="(receita, index) in listaReceita")
      span {{receita?.titulo}}

    
</template>

<script>
import { listAllRecipe } from '../services/recipe'

export default {
  name: 'GerenciarReceitas',
  components: {},
  data(){
    return{
      listaReceita: []
    }
  },
  methods:{
    mudarPagina(){
      this.$router.push({
        path: '/criarreceita'
      })
    },
    buscarReceitas(){
      listAllRecipe().then(({ data }) => {
        this.listaReceita = data
        // this.loading = false
      }).catch((error) => {
        console.log(error)
        this.triggerMensagem('negative', 'Não foi possível obter a receitas')
        // this.loading = true
      })
    },
    triggerMensagem (type, menssage) {
      this.$q.notify({
        type: type,
        message: menssage
      })
    }
  },
  mounted(){
    this.buscarReceitas()
  }
}
</script>
<style lang="sass">
.busca
  display: flex
  width: 100%

.btn
  margin: 15px
</style>
