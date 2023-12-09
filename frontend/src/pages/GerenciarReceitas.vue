<template lang="pug">
q-page
  section.q-pa-xl.column
    div.caixa-branca.column
      h4 Página de Administrador
      q-btn(@click="mudarPagina" color="black" text-color="white" no-caps).btn Criar Receita
    h4.q-pt-lg Editar Receitas Existentes:
    div(v-for="(receita, index) in listaReceita")
      CardReceita(:id="receita.id" :titulo="receita.titulo" :instrucoes="receita.instrucoes" :foto="transformarPath(receita.foto)" @click="irParaReceita(receita.id)")
</template>

<script>
import CardReceita from '../components/CardReceita.vue'
import { listAllRecipe } from '../services/recipe'

export default {
  name: 'GerenciarReceitas',
  components: { CardReceita },
  data() {
    return {
      listaReceita: [],
      foto: 'uploads/testeunb.jpeg'
    }
  },
  methods: {
    mudarPagina() {
      this.$router.push({
        path: '/criarreceita'
      })
    },
    buscarReceitas() {
      listAllRecipe().then(({ data }) => {
        this.listaReceita = data
        // this.loading = false
        this.triggerMensagem('positive', 'Todas receitas listadas.')
      }).catch((error) => {
        console.log(error)
        this.triggerMensagem('negative', 'Não foi possível obter a receitas')
        // this.loading = true
      })
    },
    triggerMensagem(type, menssage) {
      this.$q.notify({
        type: type,
        message: menssage
      })
    },
    transformarPath(uploads) {
      const backendURL = 'http://localhost:5000'
      const nomeArquivo = uploads.substring(uploads.lastIndexOf('/') + 1)

      return `${backendURL}/images/${nomeArquivo}`
    }
  },
  mounted() {
    this.buscarReceitas()
  }
}
</script>
<style lang="sass" scoped>
.busca
  display: flex
  width: 100%

.btn
  margin: 15px
  width: 300px

.caixa-branca
  background-color: white
  border-radius: 20px
  padding: 10px
  align-items: center
  justify-content: center
</style>
